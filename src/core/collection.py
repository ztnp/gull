# -*- coding:utf-8 -*-
from src.core.vector import Vector


class Collection(object):

    def __init__(self, name, dimension, metrics='l2'):
        self._name = name
        self._dimension = dimension
        self._metrics = metrics

        self._ids_mapping = dict()
        # self._ids_int_mapping = dict()

        self._vector = Vector(dimension, metrics=metrics)

    def get_info(self):
        return {
            'name': self._name,
            'dimension': self._dimension,
            'metrics': self._metrics,
            'count': self.get_count()
        }

    def get_count(self):
        pass

    def add(self, ids, embeddings, metadatas=None):
        _ids_int = range(len(ids))
        self._ids_mapping.update(list(zip(_ids_int, ids)))
        # self._ids_int_mapping.update(list(zip(ids, _ids_int)))

        self._vector.add(_ids_int, embeddings)

    def search(self, embeddings, top_k=5, fileter_param=None):
        self._vector.search(embeddings, top_k=top_k)

    def drop(self):
        self._vector.drop()
