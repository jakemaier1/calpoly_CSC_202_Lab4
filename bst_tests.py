from bst import *


class Test(unittest.TestCase):
    def test_is_empty(self):
        bst = BinarySearchTree(Node(6, Node(3, Node(2, None,None),Node(4,None,None)), Node(9, Node(7,None,None), Node(10,None,None))), to_the_left)
        self.assertEqual(is_empty(bst), False)
        self.assertEqual(is_empty(BinarySearchTree(None, to_the_left)), True)
    def test_insert_helper(self):
        bst = Node(3, Node(2, None,None),Node(4,None,None))
        bst_result = Node(3, Node(2, Node(1, None, None),None),Node(4,None,None))
        self.assertEqual(insert_helper(bst,1,to_the_left),bst_result)
    def test_insert(self):
        bst = BinarySearchTree(Node(3, Node(2, None,None),Node(5,None,None)), to_the_left)
        bst_result = BinarySearchTree(Node(3, Node(2, None,None),Node(5,None,Node(6,None,None))), to_the_left)
        self.assertEqual(insert(bst, 6), bst_result)
    def test_equality(self):
        self.assertEqual(equality(4,2, to_the_left),False)
        self.assertEqual(equality(5, 5, to_the_left), True)
    def test_binLookup(self):
        bst = Node(6,Node(3,Node(2,None,None),Node(4,None,None)),Node(9,Node(7,None,None),Node(10,None,None)))
        self.assertEqual(binLookup(bst,5, to_the_left),False)
        self.assertEqual(binLookup(bst,9, to_the_left),True)
    def test_lookup(self):
        bst = Node(6,Node(3,None,Node(5,None,None)),Node(9,Node(7,None,None),Node(10,None,None)))
        bstTree = BinarySearchTree(bst, to_the_left)
        self.assertEqual(lookup(bstTree, 5), True)
    def test_find_largest(self):
        bst = Node(6, Node(3, Node(2, None, None), Node(4, None, None)),
                   Node(9, Node(7, None, None), Node(10, None, None)))
        self.assertEqual(find_largest(bst), 10)
    def test_remove_largest(self):
        bst = Node(6, Node(3, Node(2, None, None), Node(4, None, None)),
                   Node(9, Node(7, None, None), None))
        bst_result = Node(6, Node(3, Node(2, None, None), Node(4, None, None)),Node(7, None, None))
        self.assertEqual(remove_largest(bst,9), bst_result)
    def test_delete(self):
        bst = Node(6, Node(3, Node(2, None, None), Node(4, None, None)),
                   Node(9, Node(7, None, None), None))
        bst_result = bst_result = Node(6, Node(3, Node(2, None, None), Node(4, None, None)),Node(7, None, None))
        bstTest = BinarySearchTree(bst, to_the_left)
        bstChallenger = BinarySearchTree(bst_result, to_the_left)
        self.assertEqual(delete(bstTest, 9), bstChallenger)
    def test_deleteBin(self):
        bst = Node(6, Node(3, Node(2, None, None), Node(4, None, None)),
                   Node(9, Node(7, None, None), None))
        bst_result = Node(6, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, None, None))
        self.assertEqual(deleteBin(bst, 9, to_the_left), bst_result)
