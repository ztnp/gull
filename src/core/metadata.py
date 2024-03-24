# -*- coding:utf-8 -*-
import json
from typing import List, Any


class Metadata(object):

    def __init__(self):
        self._metadatas = dict()

    def drop(self):
        pass

    def get_count(self):
        return len(self._metadatas)

    def get(self, ids):
        return self._metadatas[ids]

    def get_all(self):
        return list(zip(*self._metadatas.items()))

    def add(self, ids, metadatas):
        for item in metadatas:
            for value in item.values():
                if not isinstance(value, (str, int, float, bool)):
                    raise ValueError(
                        f'Expected metadata value to be a str, int, float or bool, '
                        f'but got {item} which is of type {type(item)}')
        self._metadatas.update(list(zip(ids, metadatas)))

    def search(self, filter_param):
        if len(filter_param) != 1:
            raise ValueError(
                f'Expected filter parameter is an element, but got f{filter_param} '
                f'which number is f{len(filter_param)}')

        filter_k, filter_v = list(filter_param.items())[0]
        if not isinstance(filter_v, (str, int, float, bool)):
            raise ValueError(f'Expected filter parameter to be a str, int, float or bool, '
                             f'but got {filter_v} which is of type {type(filter_v)}')

        result = []
        for ids, metadata in self._metadatas.items():
            if metadata.get(filter_k) == filter_v:
                result.append([ids, metadata])
        return result
