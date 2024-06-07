import unittest
from bst import *

class Test(unittest.TestCase):
    def test_prefix_iterator(self):
        bt = Node(6, Node(3, Node(2, None, None), Node(4, None, None)),
                   Node(9, Node(7, None, None), None))
        bst = BinarySearchTree(bt,to_the_left)
        vals = []
        for i in prefix_iterator(bst):
            vals.append(i)
        self.assertEqual(vals, [6,3,2,4,9,7])
    def test_infix_iterator(self):
        bt = Node(6, Node(3, Node(2, None, None), Node(4, None, None)),
                  Node(9, Node(7, None, None), None))
        bt2 = Node(10,Node(5, None,None),Node(15,None,Node(20,None,None)))
        bst = BinarySearchTree(bt, to_the_left)
        bst2 = BinarySearchTree(bt2, to_the_left)
        vals = []
        vals2 = []
        for i in infix_iterator(bst):
            vals.append(i)
        self.assertEqual(vals, [2,3,4,6,7,9])
    def test_infix_iterator2(self):
        bt2 = Node(10,Node(5, None,None),Node(15,None,Node(20,None,None)))
        bst2 = BinarySearchTree(bt2, to_the_left)
        vals2 = []
        for i in infix_iterator(bst2):
            vals2.append(i)
        self.assertEqual(vals2, [5,10,15,20])
    def test_postfix_iterator(self):
        bt = Node(6, Node(3, Node(2, None, None), Node(4, None, None)),
                  Node(9, Node(7, None, None), None))
        bst = BinarySearchTree(bt, to_the_left)
        vals = []
        for i in postfix_iterator(bst):
            vals.append(i)
        self.assertEqual(vals, [2,4,3,7,9,6])
