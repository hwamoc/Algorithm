'''
# 예제 입력 1
3
4
7
10
'''
from sys import stdin
input = stdin.readline

def plusW123(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 4
  else:
    return plusW123(n-1) + plusW123(n-2) + plusW123(n-3)

n = int(input())

for _ in range(n):
  print(plusW123(int(input())))