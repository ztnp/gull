# -*- coding:utf-8 -*-
from typing import Union

from fastapi import FastAPI

from src.core.collection import Collection
from src.server.types import CreateCollectionModel, CreatePointModel, CreatePointModelBatch, SearchPointModel
from src.utils.Exceptions import CreateCollectionException

app = FastAPI()

collections = dict()


@app.get('/collections')
async def list_collection() -> Union[dict]:
    return {'result': list(collections.keys()), 'status': 'ok'}


@app.get('/collections/{collection_name}')
async def get_collection(collection_name: str) -> Union[dict]:
    _collection = collections.get(collection_name)
    if _collection is None:
        return {'result': 'Collection not found', 'status': 'error'}
    return {'result': _collection.get_info(), 'status': 'ok'}


@app.post('/collections/{collection_name}')
async def create_collection(collection_name: str, item: CreateCollectionModel) -> Union[dict]:
    if collection_name in collections.keys():
        return {'result': 'collection exists', 'status': 'error'}

    try:
        _collection = Collection(name=collection_name, dimension=item.dimension, metrics=item.metrics)
    except CreateCollectionException as e:
        return {'result': str(e), 'status': 'error'}

    collections.update({collection_name: _collection})
    return {'result': 'create collection ok', 'status': 'ok'}


@app.delete('/collections/{collection_name}')
async def delete_collection(collection_name: str) -> Union[dict]:
    _collection = collections.get(collection_name)
    if _collection is None:
        return {'result': 'collection not found', 'status': 'error'}

    _collection.drop()
    _collection = []
    collections.pop(collection_name)
    return {'result': 'drop collection', 'status': 'ok'}


#######

@app.get('/collections/{collection_name}/points')
async def get_points_by_filter() -> Union[dict]:
    return {'msg': 'list points', 'status': 200}


@app.get('/collections/{collection_name}/points/{ids}')
async def get_points() -> Union[dict]:
    return {'msg': 'describe point', 'status': 200}


@app.post('/collections/{collection_name}/points')
async def create_points(collection_name: str, item: CreatePointModel) -> Union[dict]:
    _collection = collections.get(collection_name)
    _collection.add(ids=item.ids, embeddings=item.embeddings, metadatas=item.metadatas)
    return {'result': 'create point success', 'status': 'ok'}


@app.post('/collections/{collection_name}/points/batch')
async def create_points_batch(collection_name: str, item: CreatePointModelBatch) -> Union[dict]:
    _collection = collections.get(collection_name)
    _collection.batch_add(ids=item.ids, embeddings=item.embeddings, metadatas=item.metadatas)
    return {'result': 'create point success', 'status': 'ok'}


@app.post('/collections/{collection_name}/points/search')
async def search_points(collection_name: str, item: SearchPointModel) -> Union[dict]:
    _collection = collections.get(collection_name)
    datas = _collection.search(embeddings=item.embeddings, filter_param=item.filter)
    return {'result': datas, 'status': 'ok'}


@app.post('/collections/{collection_name}/points/delete')
async def delete_points() -> Union[dict]:
    return {'msg': 'delete point', 'status': 200}
