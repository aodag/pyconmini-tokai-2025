# be_iterable.py
import sys
from collections.abc import Iterable
sys.modules[__name__].__class__ = Iterable
