import numpy as np

from src.core.vector import Vector


def main():
    dim = 128
    num_elements = 300

    # Generating sample data
    ids = [f'test-{i}' for i in range(num_elements)]
    data = np.float32(np.random.random((num_elements, dim)))

    # print('################################')
    # for i, j in zip(ids, data):
    #     print(f'id: {i}, vector: {j}')

    index = Vector(dim, metrics='l2')
    # index.add(ids, data)
    index.add(ids=ids, vector=data)

    # print('################################')
    # print(index.get(ids=['test-0']))
    # print(index.get_all())

    # for l, v in zip(*index.get_all()):
    #     print(l, v)
    #
    # # print('################################')
    # test_ids = f'test-{num_elements - 1}'
    # vector = np.float32(np.random.random((1, dim)))
    #
    # print('update vector:', vector)
    # print(vector.shape)
    #
    # print('################################')
    #
    # index.add(ids=[test_ids], vector=vector)
    # for l, v in zip(*index.get_all()):
    #     print(l, v)

    print('################################')

    # labels, distances = index.search(data)
    labels, distances = index.search(data[3], top_k=5)

    for l, d in zip(labels, distances):
        print(l, d)

    print('test-debug')


if __name__ == '__main__':
    main()
