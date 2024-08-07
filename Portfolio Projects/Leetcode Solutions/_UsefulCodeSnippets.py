# https://www.techinterviewhandbook.org/grind75
# https://link.excalidraw.com/readonly/PFnrctDhQfDOn3eFl7Tq
import os
import sys
import typing
from typing import List

''' Dynamic programming breaks the problem down into smaller pieces then solves those to solve the whole.
'''
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
class Tree:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
    def _add(self, val, node):
        if val < node.value:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None
    def _find(self, val, node):
        if val == node.value:
            return node
        elif (val < node.value and node.left is not None):
            self._find(val, node.left)
        elif (val > node.value and node.right is not None):
            self._find(val, node.right)
    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.value) + ' ')
            self._printTree(node.right)
class DepthFirstSearch:
    def dfs():
        pass
class BreadthFirstSearch:
    def bfs():
        pass

class BreadthFirstSearch:
    def search():
        pass


def test_binary_tree():
    #     3
    # 0     4
    #   2      8
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.printTree()
    print(tree.find(3).value)
    print(tree.find(10))
    tree.deleteTree()
    # ============
    tree.printTree()


def main():
    test_binary_tree()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
