# https://www.acmicpc.net/problem/2577
import sys


sys.stdin = open("0_숫자의개수.txt")
A = int(input())
B = int(input())
C = int(input())


str_result = str(A*B*C)

result = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for chr in str_result:
    result[f"{chr}"] += 1
# 딕셔너리를 넣으면 len화 되네
for i in result:
    print(result[i])
    