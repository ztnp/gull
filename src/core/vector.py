# -*- coding:utf-8 -*-
from src.core.index.hnsw import HNSWIndex


class Vector(object):

    def __init__(self, dimension, metrics):
        self._metrics = metrics
        self._dimension = dimension
        self._index = HNSWIndex(dimension=dimension, metrics=metrics)

    def drop(self):
        pass

    def add(self, ids, vector):
        self._index.add(ids, vector)

    def search(self, vector, top_k=5, k_neighbors=5):
        return self._index.search(vector, top_k=top_k, k_neighbors=k_neighbors)


def main():
    import numpy as np

    dim = 128
    num_elements = 10000

    # Generating sample data
    ids = np.arange(num_elements)
    data = np.float32(np.random.random((num_elements, dim)))

    index = Vector(dim, metrics='cosine')

    index.add(ids, data)
    labels, distances = index.search(data)

    for d, l in zip(distances, labels):
        print(l, d)


if __name__ == '__main__':
    main()
