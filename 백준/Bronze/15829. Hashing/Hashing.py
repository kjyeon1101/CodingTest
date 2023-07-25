import sys
input = sys.stdin.readline

L = int(input())
string = input().strip()

H = sum([(ord(s)-96) * (31**i) for i, s in enumerate(string)]) % 1234567891
print(H)