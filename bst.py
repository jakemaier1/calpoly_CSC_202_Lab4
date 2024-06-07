import unittest
from dataclasses import *
from typing import *

BinTree: TypeAlias = Union[None, 'Node']

@dataclass
class Node:
    val: int
    l: BinTree
    r: BinTree


@dataclass(frozen = True)
class BinarySearchTree:
    tree: BinTree
    comes_before: Callable[[int, int], bool]

def to_the_left(a: int, b: int) -> bool:
    return a < b

# return true if BST is empty
def is_empty(t: BinarySearchTree) -> bool:
    if t.tree is None:
        return True
    else:
        return False
def insert(t: BinarySearchTree, v: int) -> BinarySearchTree:
    return BinarySearchTree(insert_helper(t.tree, v, t.comes_before), t.comes_before)
def insert_helper(bt: BinTree, v: int, func: Callable[[int, int], bool]) -> BinTree:
    if bt is None:
        return Node(v, None, None)
    elif func(v, bt.val):
        return Node(bt.val, insert_helper(bt.l, v, func), bt.r)
    else:
        return Node(bt.val, bt.l, insert_helper(bt.r, v, func))
# return true if value is in tree, false if not
def lookup(t: BinarySearchTree, v: int) -> bool:
    binT = t.tree
    return binLookup(binT, v, t.comes_before)
# helper function that does the job of lookup when given a binTree
def binLookup(t: BinTree, v: int, func: Callable[[int, int], bool]) -> bool:
    if t is None:
        return False
    if equality(v, t.val, func):
        return True
    else:
        if func(v, t.val):
            return binLookup(t.l, v, func)
        else:
            return binLookup(t.r, v, func)

# use the comes before function to determine equality of two values
def equality(a: int, b: int, func: Callable[[int, int], bool]) -> bool:
    if not (func(a,b)) and not (func(b,a)):
        return True
    else:
        return False

def delete(t: BinarySearchTree, v:int) -> BinarySearchTree:
    if not lookup(t, v):
        return t
    else:
        return BinarySearchTree(deleteBin(t.tree,v,t.comes_before), t.comes_before)

# find the value, remove it, and re-balance the tree
def deleteBin(t: BinTree, v: int, func: Callable[[int,int],bool]) -> BinTree:
    if t.val == v:
        return remove_largest(t, find_largest(t))
    else:
        if func(v,t.val):  # if v < val
            return Node(t.val,deleteBin(t.l,v,func), t.r)
        else:
            return Node(t.val,t.l, deleteBin(t.r,v,func))
# find the largest value in the tree
def find_largest(t: BinTree) -> int:
    if t.r is None:
        return t.val
    else:
        return find_largest(t.r)
# remove the largest value, if it has a child node, replace that value with child node
def remove_largest(t: BinTree, v: int) -> BinTree:
    if t.val == v:
        if t.l is None:
            return None
        else:
            value = Node(t.l.val, None, None)
            return value
    else:
        return Node(t.val, t.l, remove_largest(t.r, v))
# turn a Binary Search Tree into a BinTree
def unwrap(t: BinarySearchTree) -> (BinTree, Callable[[int,int],bool]):
    binT = t.tree
    func = t.comes_before
    return (binT,func)
def wrap(t: BinTree, func: Callable[[int,int],bool]) -> BinarySearchTree:
    return BinarySearchTree(t,func)

# return a generator for preorder traversal of a binary search tree
def prefix_iterator(tree: BinarySearchTree) -> Generator:
    (t,func) = unwrap(tree)
    if t is None:
        return None
    else:
        yield t.val
        yield from prefix_iterator(wrap(t.l,func))
        yield from prefix_iterator(wrap(t.r,func))

# return a generator for in order traversal of a binary search tree
def infix_iterator(tree: BinarySearchTree) -> Generator:
    (t,func) = unwrap(tree)
    if t is None:
        return None
    else:
        yield from infix_iterator(wrap(t.l, func))
        yield t.val
        yield from infix_iterator(wrap(t.r, func))

# return a generator for a post order traversal of a binary search tree
def postfix_iterator(tree:BinarySearchTree) -> Generator:
    (t,func) = unwrap(tree)
    if t is None:
        return None
    else:
        yield from postfix_iterator(wrap(t.l, func))
        yield from postfix_iterator(wrap(t.r,func))
        yield t.val
