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

def sum_too_long(li: ListIter) -> int:
    num = 0
    for i in range(100):
        if li.ll is not None:
            num += li.ll.first
            li.ll = li.ll.rest
    return num

class Test(unittest.TestCase):
    def test_iterator_objects_elements(self):
        I1 = ListIter(Node(4, Node(3, Node(5, Node(7, Node(1, None))))))
        I2 = ListIter(None)
        I3 = ListIter(Node(10, Node(10, None)))
        self.assertEqual(to_list(I1), [4,3,5,7,1])
        self.assertEqual(to_list(I2), [])
        self.assertEqual(to_list(I3), [10,10])

    def test_iterator_objects_sum(self):
        I1 = ListIter(Node(4, Node(3, Node(5, Node(7, Node(1, None))))))
        I2 = ListIter(None)
        I3 = ListIter(Node(10, Node(10, None)))
        self.assertEqual(summ(I1), 20)
        self.assertEqual(summ(I2), 0)
        self.assertEqual(summ(I3), 20)
    def test_sum_too_long(self):
        I1 = ListIter(Node(4, Node(3, Node(5, Node(7, Node(1, None))))))
        I2 = ListIter(None)
        I3 = ListIter(Node(10, Node(10, None)))
        self.assertEqual(sum_too_long(I1), 20)
        self.assertEqual(sum_too_long(I2), 0)
        self.assertEqual(sum_too_long(I3), 20)
