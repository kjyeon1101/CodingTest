import sys
input = sys.stdin.readline

from math import ceil

A, B, V = map(int, input().split())
print(ceil((V-B)/(A-B)))