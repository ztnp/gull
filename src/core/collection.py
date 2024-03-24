# -*- coding:utf-8 -*-
from src.core.metadata import Metadata
from src.core.vector import Vector


class Collection(object):

    def __init__(self, name, dimension, metrics='l2'):
        self._name = name
        self._dimension = dimension
        self._metrics = metrics

        self._metadata = Metadata()
        self._vector = Vector(dimension, metrics=metrics)

    def get_info(self):
        return {
            'name': self._name,
            'dimension': self._dimension,
            'metrics': self._metrics,
            'count': self.get_count()
        }

    def get_count(self):
        if self._vector.get_count() != self._metadata.get_count():
            raise AssertionError(
                f'vector size({self._vector.get_count()}) and metadata size({self._metadata.get_count()}) '
                f'are inconsistent.')
        return self._vector.get_count()

    def add(self, ids, embeddings, metadatas=None):
        self._vector.add(ids=ids, vector=embeddings)
        self._metadata.add(ids=ids, metadatas=metadatas)

    def search(self, embeddings, top_k=5, filter_param=None):
        vector_result = self._vector.search(embeddings, top_k=top_k)

        if filter_param is None:
            metadata_result = []
        else:
            metadata_result = self._metadata.search(filter_param)

    def drop(self):
        self._vector.drop()
        self._metadata.drop()
