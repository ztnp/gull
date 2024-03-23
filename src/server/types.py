from typing import List

from pydantic import BaseModel


class CreateCollection(BaseModel):
    dimension: int
    metrics: str | None = None


class CreatePoint(BaseModel):
    ids: List[str]
    embeddings: List[List[float]]
    metadatas: List[dict] | None = None


class SearchPoint(BaseModel):
    embeddings: List[float] | List[List[float]]
    filter: dict | None = None
