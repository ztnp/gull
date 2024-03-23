from typing import List

from pydantic import BaseModel


class CreateCollectionModel(BaseModel):
    dimension: int
    metrics: str | None = None


class CreatePointModel(BaseModel):
    ids: str
    embeddings: List[float]
    metadatas: dict | None = None


class CreatePointModelBatch(BaseModel):
    ids: List[str]
    embeddings: List[List[float]]
    metadatas: List[dict] | None = None


class SearchPointModel(BaseModel):
    embeddings: List[float] | List[List[float]]
    filter: dict | None = None
