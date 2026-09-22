import os
from typing import Sequence

import torch
import torch.nn.functional as F
from langchain_core.documents import Document
from langchain_core.documents.compressor import BaseDocumentCompressor
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import AutoModel, AutoTokenizer

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7897'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7897'
os.environ['NO_PROXY'] = 'dashscope.aliyuncs.com'
os.environ['no_proxy'] = 'dashscope.aliyuncs.com'

INDEX_DIR = "./faiss_index"


def create_embeddings():
    return HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-zh-v1.5",
        model_kwargs={'device': 'cpu'}
    )


class ColBERTReranker(BaseDocumentCompressor):
    """优化后的ColBERT重排器，修复维度计算问题，支持批量处理"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        model_name = kwargs.get("model_name", "bert-base-chinese")
        device = kwargs.get("device", "cuda" if torch.cuda.is_available() else "cpu")

        object.__setattr__(self, 'tokenizer', AutoTokenizer.from_pretrained(model_name))
        object.__setattr__(self, 'model', AutoModel.from_pretrained(model_name).to(device))
        object.__setattr__(self, 'device', device)
        self.model.eval()
        print(f"ColBERT模型加载完成，运行设备: {device}")

    def encode_text(self, texts, batch_size=8):
        all_embeddings = []
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i + batch_size]
            inputs = self.tokenizer(
                batch_texts,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=128
            ).to(self.device)

            with torch.no_grad():
                outputs = self.model(**inputs)
                embeddings = F.normalize(outputs.last_hidden_state, p=2, dim=-1)
            all_embeddings.append(embeddings.cpu())

        return torch.cat(all_embeddings, dim=0)

    def calculate_colbert_similarity(self, query_emb, doc_embs, query_mask, doc_masks):
        scores = []

        for i, doc_emb in enumerate(doc_embs):
            doc_mask = doc_masks[i:i+1]
            similarity_matrix = torch.matmul(query_emb, doc_emb.unsqueeze(0).transpose(-2, -1))
            doc_mask_expanded = doc_mask.unsqueeze(1)
            similarity_matrix = similarity_matrix.masked_fill(~doc_mask_expanded.bool(), -1e9)
            max_sim_per_query_token = similarity_matrix.max(dim=-1)[0]
            query_mask_expanded = query_mask.unsqueeze(0)
            max_sim_per_query_token = max_sim_per_query_token.masked_fill(~query_mask_expanded.bool(), 0)
            colbert_score = max_sim_per_query_token.sum(dim=-1).item()
            scores.append(colbert_score)

        return scores

    def compress_documents(
            self,
            documents: Sequence[Document],
            query: str,
            callbacks=None,
    ) -> Sequence[Document]:
        if len(documents) == 0:
            return documents

        query_embeddings = self.encode_text([query])
        query_inputs = self.tokenizer(
            [query],
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=128
        )

        doc_texts = [doc.page_content for doc in documents]
        doc_embeddings = self.encode_text(doc_texts)
        doc_inputs = self.tokenizer(
            doc_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=128
        )

        scores = self.calculate_colbert_similarity(
            query_embeddings,
            doc_embeddings,
            query_inputs['attention_mask'],
            doc_inputs['attention_mask']
        )

        scored_docs = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in scored_docs[:5]]
