# Copyright 2020 Wilmer Krisp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Core class and functions """

# ABCMeta, abstractmethod
import abc
# binary search algo
import bisect
# defaultdict OrderedDict deque namedtuple
import collections
# deepcopy
import copy
# dataclass, field - for simple comparable value-object
import dataclasses
# Enum
import enum
# reduce lru_cache
import functools
# ratio=Fraction
import fractions
# heappush, heappop, heapify
import heapq
# product permutations combinations chain chain.from_iterable  islice count cycle takewhile dropwhile groupby repeat
import itertools
# log2(aryhm) ceil-floor-trunc dist(euclidian) factorial  gcd(greatest common divisor)  perm(utations)
import math
# add  mul sub abs index mod concat contains countOf getitem setitem iadd METHODCALLER ITEMGETTER
import operator
# rnd
import random
# regular expressions
import re
# setrecursionlimit
import sys
# TODO(wilmer.krisp@yahoo.com) in python 3.9 delete List, Tuple, Set, Dict, Deque
from typing import Any, Final, Union, Optional, Iterable, Collection, Hashable, Callable, List, Tuple, Set, Dict, Deque, Generator
# warn
import warnings
# TODO(wilmer.krisp@yahoo.com)  delete after leetcode
#import wilmerlibrary
#import sortedcontainers

chain = itertools.chain.from_iterable
sys.setrecursionlimit(10 ** 7)
print("Program is started. Recursion limit=", sys.getrecursionlimit())

chain = itertools.chain.from_iterable


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press <no shortcut> to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

a=2
a=3