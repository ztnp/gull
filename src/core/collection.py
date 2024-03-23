# -*- coding:utf-8 -*-


class Collection(object):

    def __init__(self, name, dimension, metrics=None):
        self._name = name
        self._dimension = dimension
        self._metrics = metrics or 'l2'

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
        pass

    def get(self, embeddings, fileter_param=None):
        pass

    def drop(self):
        pass
