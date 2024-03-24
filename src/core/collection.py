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

    def peek(self, limit=10):
        pass

    def add(self, ids, embeddings, metadatas=None):
        self._vector.add(ids=ids, vector=embeddings)
        self._metadata.add(ids=ids, metadatas=metadatas)

    def search(self, embeddings, top_k=5, filter_param=None):
        vec_ids, vec_distances = self._vector.search(embeddings, top_k=top_k)

        if filter_param is None:
            result_datas = self._metadata.get(vec_ids)
            return vec_ids, vec_distances, result_datas

        result = self._metadata.search(filter_param)
        meta_ids, meta_data = zip(*result)
        meta_ids_data_mapping = dict(zip(meta_ids, meta_data))

        result_ids = []
        result_vec = []
        result_datas = []
        for item_ids, item_dis in zip(vec_ids, vec_distances):
            if item_ids in meta_ids:
                result_ids.append(item_ids)
                result_vec.append(item_dis)
                result_datas.append(meta_ids_data_mapping[item_ids])
        return result_ids, result_vec, result_datas

    def drop(self):
        self._vector.drop()
        self._metadata.drop()
