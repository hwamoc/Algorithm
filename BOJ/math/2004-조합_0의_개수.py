'''
# 예제 입력 1
25 12
'''
from sys import stdin
input = stdin.readline

M, N = map(int, input().split())

def countNum(N, num):
  count = 0
  divNum = num
  while( N >= divNum):
    count = count + (N // divNum)
    divNum = divNum * num
  return count

print(min(countNum(M, 5) - countNum(N, 5) - countNum(M-N, 5), countNum(M, 2) - countNum(N, 2) - countNum(M-N, 2)))

