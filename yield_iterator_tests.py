import unittest
from iterator import *


def summ(ll: ListIter) -> int:
    num = 0
    for i in ll:
        num += i
    return num

def to_list(ll: ListIter) -> list[int]:
    lst = []
    for i in ll:
        lst.append(i)
    return lst

class Test(unittest.TestCase):
    def test_summ(self):
        I1 = ListIter(Node(4, Node(3, Node(5, Node(7, Node(1, None))))))
        I2 = ListIter(None)
        I3 = ListIter(Node(10, Node(10, None)))
        self.assertEqual(summ(I1), 20)
        self.assertEqual(summ(I2), 0)
        self.assertEqual(summ(I3), 20)
    def test_to_list(self):
        I1 = ListIter(Node(4, Node(3, Node(5, Node(7, Node(1, None))))))
        I2 = ListIter(None)
        I3 = ListIter(Node(10, Node(10, None)))
        self.assertEqual(summ(I1), 20)
        self.assertEqual(summ(I2), 0)
        self.assertEqual(summ(I3), 20)
