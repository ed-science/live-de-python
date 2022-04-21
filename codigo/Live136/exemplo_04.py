from functools import lru_cache, reduce
from operator import mul


@lru_cache
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)


@lru_cache
def fact(k):
    return 1 if k < 2 else reduce(mul, range(2, int(k)+1))
