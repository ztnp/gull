# -*- coding:utf-8 -*-

import hnswlib


class HNSWIndex(object):
    """
    Squared L2	'l2'	d = sum((Ai-Bi)^2)
    Inner product	'ip'	d = 1.0 - sum(Ai*Bi)
    Cosine similarity	'cosine'	d = 1.0 - sum(Ai*Bi) / sqrt(sum(Ai*Ai) * sum(Bi*Bi))
    """

    def __init__(self,
                 dimension,
                 metrics='l2',
                 num_thread=-1,
                 m=16,
                 ef=100,
                 ef_construction=100,
                 default_capacity=10000):
        self._space = metrics
        self._dimension = dimension

        self._M = m
        self._ef = ef
        self._ef_construction = ef_construction
        self._default_capacity = default_capacity

        self._num_thread = num_thread
        self._index = self.__init_index()

    def __init_index(self, not_initialized=False):
        _index = hnswlib.Index(space=self._space, dim=self._dimension)

        if not not_initialized:
            _index.init_index(
                max_elements=self._default_capacity,
                ef_construction=self._ef_construction,
                M=self._M)

        _index.set_ef(self._ef)
        _index.set_num_threads(self._num_thread)
        return _index

    def get_count(self):
        return self._index.get_current_count()

    def expansion(self):
        self._default_capacity *= 2
        self._index.resize_index(new_size=self._default_capacity)

    def add(self, ids, data):
        self._index.add_items(data, ids)

    def search(self, data, top_k=5, k_neighbors=5, filter_param=None):
        labels, distances = self._index.knn_query(data, k=k_neighbors, filter=filter_param)
        labels_sorted, distances_sorted = zip(
            *sorted(
                zip(distances.reshape(1, -1).tolist()[0], labels.reshape(1, -1).tolist()[0]),
                reverse=True))
        return labels_sorted[:top_k], distances_sorted[:top_k]
