from Node import *


class BST():

    def __init__(self):
        self.root = None

    def insert(self, keys: list):
        for element in keys:
            if self.root is None:
                self.root = Node(element)
            else:
                self._insert(self.root, element)

    def _insert(self, node: Node, key: int):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, node: Node):
        if node:
            print(node.key)
            self._pre_order(node.left)
            self._pre_order(node.right)

    
    def in_order(self):
        pass
    
    def _in_order(self, node: Node):
        pass

    