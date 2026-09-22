import re
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from rag_common import INDEX_DIR, create_embeddings


DOCS_DIR = Path("./docs")


def extract_field(text, field_name):
    match = re.search(rf"\| {re.escape(field_name)} \| ([^|]+) \|", text)
    return match.group(1).strip() if match else ""


def extract_image(text):
    match = re.search(r"!\[[^\]]*\]\(([^)]+)\)", text)
    if not match:
        return ""
    image_path = match.group(1).strip()
    return str(DOCS_DIR / image_path).replace("\\", "/")


def extract_price_lines(text):
    section_match = re.search(
        r"## 可选配置及中国价格\s+(.+?)(?:\n## |\Z)",
        text,
        flags=re.S,
    )
    if not section_match:
        return ""
    lines = []
    for line in section_match.group(1).splitlines():
        line = line.strip()
        if line.startswith("|") and "RMB" in line:
            lines.append(line)
    return "\n".join(lines)


documents = []
for md_path in sorted(DOCS_DIR.glob("*.md")):
    text = md_path.read_text(encoding="utf-8")
    product_name = extract_field(text, "产品名") or md_path.stem
    category = extract_field(text, "分类")
    series = extract_field(text, "系列")
    release_date = extract_field(text, "发布时间")
    colors = extract_field(text, "同期发布颜色")
    image = extract_image(text)
    price_lines = extract_price_lines(text)

    searchable_text = f"""
产品名：{product_name}
分类：{category}
系列：{series}
发布时间：{release_date}
同期发布颜色：{colors}
图片：{image}
价格：
{price_lines}

全文：
{text}
""".strip()

    documents.append(
        Document(
            page_content=searchable_text,
            metadata={
                "source": str(md_path).replace("\\", "/"),
                "file_name": md_path.name,
                "product_name": product_name,
                "category": category,
                "series": series,
                "release_date": release_date,
                "colors": colors,
                "image": image,
                "price_lines": price_lines,
            },
        )
    )

if not documents:
    raise RuntimeError(f"未在 {DOCS_DIR} 找到 Markdown 文档。")

embeddings = create_embeddings()
vectorstore = FAISS.from_documents(documents, embeddings)
vectorstore.save_local(INDEX_DIR)

print(f"索引已保存到: {INDEX_DIR}")
print(f"产品文档数量: {len(documents)}")
