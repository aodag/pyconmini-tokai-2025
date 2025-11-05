import sys
from collections.abc import Iterable
from types import ModuleType

class IterableModule(ModuleType, Iterable):

    def __iter__(self):
        yield self
        n = __import__(__name__ + "$")
        self.n = n
        n.p = self
        yield from n

self = sys.modules[__name__]
self.__class__ = IterableModule
sys.modules[__name__ + "$"] = self
raise Exception()
