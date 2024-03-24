import json

from src.core.metadata import Metadata


def main():
    test_input = [
        {
            "item": "journal",
            "qty": 25,
            "status": "A",
        },
        {
            "item": "notebook",
            "qty": 50,
            "status": "A",
        },
        {
            "item": "paper",
            "qty": 100,
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "status": "A",
        },
    ]

    metadata = Metadata()
    metadata.add(ids=[f'test-{i}' for i in range(len(test_input))], metadatas=test_input)
    print(json.dumps(metadata.get_all(), ensure_ascii=False))

    result = metadata.search(filter_param={'item': 'notebook'})
    print(json.dumps(result, ensure_ascii=False))

    print('test-debug')


if __name__ == '__main__':
    main()
