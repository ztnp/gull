# -*- coding:utf-8 -*-

import hnswlib


class HNSWIndex(object):

    def __init__(self,
                 name,
                 dimension,
                 space='l2',
                 num_thread=-1,
                 m=16,
                 ef=100,
                 ef_construction=100,
                 default_capacity=10000):
        self._name = name
        self._space = space
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

    def add(self, data, ids=None):
        self._index.add_items(data, ids)

    def search(self, data, top_k=5, k_neighbors=5, filter_param=None):
        labels, distances = self._index.knn_query(data, k=k_neighbors, filter=filter_param)
        labels_sorted, distances_sorted = zip(
            *sorted(
                zip(distances.reshape(1, -1).tolist()[0], labels.reshape(1, -1).tolist()[0]),
                reverse=True))
        return labels_sorted[:top_k], distances_sorted[:top_k]


def main():
    import numpy as np

    dim = 128
    num_elements = 10000

    # Generating sample data
    ids = np.arange(num_elements)
    data = np.float32(np.random.random((num_elements, dim)))

    index = HNSWIndex('test-index', dim, space='cosine')

    index.add(data, ids)
    labels, distances = index.search(data)

    for d, l in zip(distances, labels):
        print(l, d)


if __name__ == '__main__':
    main()
