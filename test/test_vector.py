from src.core.vector import Vector


def main():
    import numpy as np

    dim = 128
    num_elements = 3000

    # Generating sample data
    ids = [f'test-{i}' for i in range(num_elements)]
    data = np.float32(np.random.random((num_elements, dim)))

    # for i, j in zip(ids, data):
    #     print(f'id: {i}, vector: {j}')

    index = Vector(dim, metrics='l2')
    index.add(ids, data)

    # print(index.get(ids=['test-0']))
    # print(index.get_all())

    labels, distances = index.search(data)
    for l, d in zip(labels, distances):
        print(l, d)

    print('test-debug')


if __name__ == '__main__':
    main()
