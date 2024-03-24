import numpy as np

from src.core.collection import Collection


def main():
    dim = 128
    num_elements = 300

    ids = [f'test-{i}' for i in range(num_elements)]
    data = np.float32(np.random.random((num_elements, dim)))
    metadata = [{'item': f'journal-{i}', 'qty': 2 * i, 'status': f'A-{i * 2}'} for i in range(num_elements)]

    # print('#############################')
    # print('ids:', ids)
    # print('data:', data)
    # print('metadata:', metadata)

    collection = Collection(name='my-collection', dimension=dim, metrics='l2')
    collection.add(ids=ids, embeddings=data, metadatas=metadata)

    # print('#############################')
    # print(collection.get_count())

    print('#############################')
    print(collection.get_info())

    print('#############################')
    result = collection.search(embeddings=data[3], top_k=5)
    for l, d, m in zip(*result):
        print(l, d, m)

    print('#############################')
    result = collection.search(embeddings=data[3], filter_param={'item': 'journal-3'})
    for l, d, m in zip(*result):
        print(l, d, m)


if __name__ == '__main__':
    main()
