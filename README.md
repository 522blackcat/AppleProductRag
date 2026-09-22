# AppleProductRag

Apple 产品 RAG 检索问答项目。项目把 `docs/` 中的 Apple 产品 Markdown 文档构建为 FAISS 向量索引，检索时先用向量召回，再用 ColBERT 风格重排，最后调用 DashScope 兼容 OpenAI 接口生成回答。

## 功能

- 基于 Apple 产品文档构建本地 FAISS 索引
- 支持按年份、月份、颜色、品类等规则过滤
- 支持产品价格、配置、图片路径、文档路径输出
- 使用 `BAAI/bge-large-zh-v1.5` 生成向量
- 使用 `bert-base-chinese` 做 ColBERT 风格重排
- 使用 `qwen-plus` 生成最终回答

## 项目结构

```text
.
├── build_index.py          # 从 docs 构建 FAISS 索引
├── search_index.py         # 检索、重排、调用 LLM 回答
├── rag_common.py           # embedding 和 reranker 公共逻辑
├── requirements.txt        # Python 依赖
├── .env.example            # 环境变量示例
├── docs/                   # Apple 产品 Markdown 文档和图片
├── faiss_index/            # 已生成的 FAISS 索引
└── units/                  # 文档生成、图片下载等辅助脚本
```

## 安装

建议使用 Python 3.12。

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 配置 API Key

项目使用 DashScope 的 OpenAI 兼容接口。先设置环境变量：

```bash
set DASHSCOPE_API_KEY=你的DashScope API Key
```

PowerShell：

```powershell
$env:DASHSCOPE_API_KEY="你的DashScope API Key"
```

也可以参考 `.env.example`。

## 构建索引

如果修改了 `docs/` 里的产品文档，重新生成索引：

```bash
python build_index.py
```

索引会保存到 `faiss_index/`。

## 运行检索

直接运行默认问题：

```bash
python search_index.py
```

传入自定义问题：

```bash
python search_index.py "25年9月发布的手机有哪些"
python search_index.py "红色系列的 iPhone 有哪些，多少钱"
python search_index.py "MacBook Pro 的配置和价格"
```

## 检索流程

1. 解析用户问题中的年份、月份、颜色、品类等约束。
2. 使用 FAISS 做第一阶段向量召回。
3. 对召回结果执行规则过滤。
4. 如果规则过滤无结果，回退到向量相似度 Top 8。
5. 使用 ColBERT 风格 reranker 对候选文档重排。
6. 把重排后的文档交给 `qwen-plus` 生成最终回答。

## 注意

- `DASHSCOPE_API_KEY` 不要写进代码，也不要提交到 Git。
- 首次运行会下载 Hugging Face 模型，耗时取决于网络。
- `rag_common.py` 中默认配置了本地代理 `127.0.0.1:7897`，如果你的环境不需要代理，可以自行修改或删除。
