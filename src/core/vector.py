# -*- coding:utf-8 -*-
from src.core.index.hnsw import HNSWIndex


class Vector(object):

    def __init__(self, dimension, metrics):
        self._metrics = metrics
        self._dimension = dimension

        # id_int -> id_string
        self._ids_mapping = dict()

        # id_string -> id_int
        self._idt_mapping = dict()

        self._index = HNSWIndex(dimension=dimension, metrics=metrics)

    def drop(self):
        pass

    def get_count(self):
        return self._index.get_count()

    def get(self, ids):
        _idt = [self._idt_mapping.get(i) for i in ids]
        return self._index.get(ids=_idt)

    def get_all(self):
        return self._index.get(ids=list(self._ids_mapping.keys()))

    def add(self, ids, vector):
        _idt = range(len(self._ids_mapping), len(ids))
        self._ids_mapping.update(list(zip(_idt, ids)))
        self._idt_mapping.update(list(zip(ids, _idt)))
        self._index.add(_idt, vector)

    def search(self, vector, top_k=5, k_neighbors=5):
        idt, distances = self._index.search(vector, top_k=top_k, k_neighbors=k_neighbors)
        ids = [self._ids_mapping.get(i) for i in idt]
        return ids, distances
