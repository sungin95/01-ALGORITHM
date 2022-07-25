# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()
result = ""
for chr in (a):
    result = chr + result
a = int(result)
result = ""
for chr in (b):
    result = chr + result
b = int(result)

print(a) if a > b else print(b)
