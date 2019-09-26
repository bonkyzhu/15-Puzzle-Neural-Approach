import numpy as np


class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent

    def child(self, data):
        return Node(data, self)

    def path(self):
        """
        返回链表所有元素
        """
        node = self
        path_to_head = []

        while node:
            path_to_head.append(node.data)
            node = node.parent

        return list(reversed(path_to_head))


class PriorityQueue:

    def __init__(self):
        '''
        根据权值排序
        '''
        self.data = []
        self.values = []

    def pop(self):
        '''
        出队列
        '''
        index = np.argmin(self.values)
        self.values.pop(index)
        element = self.data.pop(index)
        return element

    def add(self, data, value):
        '''
        入队列
        '''
        self.data.append(data)
        self.values.append(value)

    def has_next(self):
        '''
        判断是否为空
        '''
        return self.data != []

    def has(self, data):
        return data in self.data

    def get_value(self, data):
        return self.values[self.data.index(data)]

    def remove(self, data):
        i = self.data.index(data)
        del self.data[i]
        del self.values[i]

    def size(self):
        return len(self.data)

