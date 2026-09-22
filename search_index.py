import re
import sys
import os

from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

from rag_common import INDEX_DIR, ColBERTReranker, create_embeddings


COLOR_ALIASES = {
    "红色": ["红色", "酒红", "勃艮第", "粉色", "橙色"],
    "蓝色": ["蓝色", "天蓝", "雾蓝", "深蓝"],
    "黑色": ["黑色", "午夜色", "深空黑色", "夜空色"],
    "白色": ["白色", "云白", "星白"],
    "银色": ["银色"],
    "金色": ["金色", "浅金", "星光色"],
    "紫色": ["紫色", "薰衣草紫"],
    "绿色": ["绿色", "鼠尾草绿"],
    "黄色": ["黄色"],
    "橙色": ["橙色", "星宇橙"],
}

CATEGORY_ALIASES = {
    "手机": ["手机", "iPhone"],
    "电脑": ["电脑", "Mac", "MacBook", "iMac"],
    "平板": ["平板", "iPad"],
    "耳机": ["耳机", "AirPods"],
    "手表": ["手表", "Apple Watch"],
    "显示器": ["显示器", "Display"],
    "音箱": ["音箱", "HomePod"],
    "电视盒子": ["电视盒子", "Apple TV"],
    "头戴式": ["头戴式", "VR", "空间计算", "Vision"],
}


def normalize_year(year_text):
    year = int(year_text)
    if year < 100:
        return 2000 + year
    return year


def parse_query(query):
    years = []
    for match in re.finditer(r"(\d{2,4})\s*年", query):
        years.append(str(normalize_year(match.group(1))))

    months = []
    for match in re.finditer(r"(\d{1,2})\s*月", query):
        month = int(match.group(1))
        months.extend([f"{month} 月", f"{month}月"])

    colors = []
    for base_color, aliases in COLOR_ALIASES.items():
        if base_color in query or any(alias in query for alias in aliases):
            colors.extend(aliases)

    categories = []
    for category, aliases in CATEGORY_ALIASES.items():
        if category in query or any(alias.lower() in query.lower() for alias in aliases):
            categories.extend(aliases)

    wants_price = any(word in query for word in ["价格", "多少钱", "售价", "配置"])
    wants_image = any(word in query for word in ["图片", "图", "照片"])

    return {
        "years": sorted(set(years)),
        "months": sorted(set(months)),
        "colors": sorted(set(colors)),
        "categories": sorted(set(categories)),
        "wants_price": wants_price,
        "wants_image": wants_image,
    }


def doc_text(doc):
    metadata = doc.metadata
    return "\n".join(
        [
            doc.page_content,
            metadata.get("product_name", ""),
            metadata.get("category", ""),
            metadata.get("series", ""),
            metadata.get("release_date", ""),
            metadata.get("colors", ""),
            metadata.get("price_lines", ""),
        ]
    )


def matches_constraints(doc, constraints):
    text = doc_text(doc)
    metadata = doc.metadata

    if constraints["years"] and not any(year in metadata.get("release_date", "") for year in constraints["years"]):
        return False

    if constraints["months"] and not any(month in metadata.get("release_date", "") for month in constraints["months"]):
        return False

    if constraints["colors"] and not any(color in metadata.get("colors", "") for color in constraints["colors"]):
        return False

    if constraints["categories"] and not any(category in text for category in constraints["categories"]):
        return False

    return True


def explain_rules(constraints):
    parts = []
    if constraints["years"]:
        parts.append(f"年份={','.join(constraints['years'])}")
    if constraints["months"]:
        readable_months = sorted({month.replace("月", "月") for month in constraints["months"]})
        parts.append(f"月份={','.join(readable_months)}")
    if constraints["colors"]:
        parts.append(f"颜色词={','.join(constraints['colors'])}")
    if constraints["categories"]:
        parts.append(f"分类词={','.join(constraints['categories'])}")
    return "；".join(parts) if parts else "无显式规则，使用向量相似度检索"


def print_product_card(index, doc, constraints, score=None):
    metadata = doc.metadata
    print(f"\n[{index}] {metadata.get('product_name', '未知产品')}")
    print(f"分类: {metadata.get('category', '')}")
    print(f"系列: {metadata.get('series', '')}")
    print(f"发布时间: {metadata.get('release_date', '')}")
    print(f"颜色: {metadata.get('colors', '')}")
    print(f"文档: {metadata.get('source', '')}")
    if score is not None:
        print(f"相似度距离: {score:.4f}")

    if constraints["wants_image"] or True:
        print(f"图片: {metadata.get('image', '')}")

    price_lines = metadata.get("price_lines", "")
    if constraints["wants_price"] or price_lines:
        print("价格配置:")
        for line in price_lines.splitlines():
            print(f"  {line}")


def build_answer_context(docs):
    blocks = []
    for index, doc in enumerate(docs, start=1):
        metadata = doc.metadata
        blocks.append(
            "\n".join(
                [
                    f"[{index}]",
                    f"产品名: {metadata.get('product_name', '')}",
                    f"分类: {metadata.get('category', '')}",
                    f"系列: {metadata.get('series', '')}",
                    f"发布时间: {metadata.get('release_date', '')}",
                    f"颜色: {metadata.get('colors', '')}",
                    f"图片: {metadata.get('image', '')}",
                    f"文档: {metadata.get('source', '')}",
                    "价格配置:",
                    metadata.get("price_lines", ""),
                ]
            )
        )
    return "\n\n".join(blocks)


def build_answer_prompt(query, constraints, docs):
    return f"""
你是 Apple 产品检索助手。根据已经检索出的商品信息回答用户问题。

用户问题：
{query}

规则解析：
{explain_rules(constraints)}

注意：
1. 只能使用下面商品信息回答。
2. 必须保留产品名、分类、发布时间、颜色、图片路径、文档路径。
3. 如用户问价格或配置，必须列出价格配置。
4. 如命中来自色系规则，比如“红色系列”匹配到“星宇橙色、粉色、勃艮第酒红色”，要说明匹配原因。
5. 如果没有商品，回答没有匹配产品。

商品信息：
{build_answer_context(docs)}
""".strip()


query = " ".join(sys.argv[1:]).strip() or "25年9月发布的产品有哪些"
constraints = parse_query(query)
dashscope_api_key = os.environ.get("DASHSCOPE_API_KEY")
if not dashscope_api_key:
    raise RuntimeError("请先设置 DASHSCOPE_API_KEY 环境变量。")

embeddings = create_embeddings()
vectorstore = FAISS.load_local(
    INDEX_DIR,
    embeddings,
    allow_dangerous_deserialization=True
)

base_results_with_scores = vectorstore.similarity_search_with_score(query, k=500)
filtered_base_results = [
    (doc, score)
    for doc, score in base_results_with_scores
    if matches_constraints(doc, constraints)
]

base_results = filtered_base_results or base_results_with_scores[:8]
base_docs = [doc for doc, _ in base_results]

reranker = ColBERTReranker()
reranked_docs = list(reranker.compress_documents(base_docs, query))

llm = ChatOpenAI(
    model="qwen-plus",
    temperature=0.1,
    api_key=dashscope_api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
final_answer = llm.invoke(build_answer_prompt(query, constraints, reranked_docs))

print(f"\n{'=' * 20} 产品检索 {'=' * 20}")
print(f"查询: {query}")
print(f"检索规则: {explain_rules(constraints)}")
if constraints and not filtered_base_results:
    print("规则过滤无结果，已回退到向量相似度 Top 8。")

print("\n--- (1) 基础检索结果 ---")
for i, (doc, score) in enumerate(base_results[:8], start=1):
    print_product_card(i, doc, constraints, score)

print("\n--- (2) ColBERT重排结果 ---")
for i, doc in enumerate(reranked_docs, start=1):
    print_product_card(i, doc, constraints)

print("\n--- (3) LLM最终回答 ---")
print(final_answer.content)
