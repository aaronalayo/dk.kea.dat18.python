"""
This module holds a Node class for working with a binary tree.

Classes: Node
"""

import math
import random


class Node:
    """ Binary tree node. A root node serves as an entry point for the tree.
    >>> root = Node(values=[5, 1, 7, 8, 2, 3, 0, 9, 6])
    >>> root.subtree()
    [0, 1, 2, 3, 5, 6, 7, 8, 9]
    >>> root.insert([4])
    >>> root.subtree()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> root.remove(0)
    >>> root.subtree()
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    def __init__(self, value=None, values=None):
        """ Class initializer.
        Arguments: value = object | values = sequence of objects.
        """
        assert not (value and values), 'Node only accept one single value or a sequence of values, not both.'
        self.left = None
        self.right = None
        if not value is None:
            self.value = value
        elif values:
            self.value = values[0]
            self.insert(values[1:])
        else:
            self.value = None

    def __repr__(self):
        return str(self.value)

    def __len__(self):
        """ Returns number of nodes in the binary tree.
        """
        return len(self.subtree())

    def insert(self, values):
        """ Insert value into tree.
        """
        for value in values:
            if value < self.value:
                if self.left:
                    self.left.insert([value])
                else:
                    self.left = Node(value=value)
            else:
                if self.right:
                    self.right.insert([value])
                else:
                    self.right = Node(value=value)

    def remove(self, value):
        """ Remove element with value from tree.
        """
        subtree = self.subtree()
        try:
            subtree.remove(value)
        except ValueError:
            raise ValueError(f'Tree does not contain {value}.')
        random.shuffle(subtree)
        self.left = None
        self.right = None
        if subtree:
            self.value = subtree.pop()
            self.insert(subtree)
        else:
            self.value = None

    def subtree(self):
        """ Sorted list of elements.
        """
        if self.left:
            left = self.left.subtree()
        else:
            left = []
        if self.right:
            right = self.right.subtree()
        else:
            right = []
        return left + [self.value] + right

    def height(self):
        """ The height of the tree as understood in graph theory.
        """
        return self._max_depth() - 1

    def _max_depth(self):
        """ Helper function for calculating depth.
        """
        left_depth = self.left._max_depth() if self.left else 0
        right_depth = self.right._max_depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def optimization_level(self):
        """ Gives a measure for how perfectly balanced the binary tree is. Range [0..1], where 1 is perfect.
        """
        return max(0, min(1, math.ceil(math.log2(len(self)))/self.height())) if self.height() > 0 else 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()