from typing import *
from dataclasses import *

IntList: TypeAlias = Union[None,'Node']

@dataclass
class Node:
    first: int
    rest: IntList

@dataclass
class ListIter:
    ll: IntList
    def __next__(self):
        match self.ll:
            case None:
                raise StopIteration
            case Node(f, r):
                self.ll = r
                return f
    def __iter__(self):
        return self

def yield_iterator(ll: IntList) -> Generator:
    if ll is None:
        return None
    else:
        yield from yield_iterator(ll.rest)



