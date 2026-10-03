import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))

from fractions import Fraction

from decimal import Decimal, getcontext
getcontext().prec = 50

import sys
sys.setrecursionlimit(100_000)