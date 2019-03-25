# coding=utf-8
__author__ = 'zs'
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
        self._parent = None

    def __repr__(self):
        return ("Node({!r})".format(self._value))

    def add_child(self, node):
        self._children.append(node)
        node._parent = self

    def __iter__(self):
        return iter(self._children)

if __name__ == '__main__':
    root = Node(0)
    kid1 = Node(1)
    kid2 = Node(2)
    root.add_child(kid1)
    root.add_child(kid2)

    for k in root:
        print(k, 'of', k._parent)