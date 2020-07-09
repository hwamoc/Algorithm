'''
# 예제 입력 1
3
4 10 20 30 40
3 7 5 12
3 125 15 25
'''
from itertools import combinations
from sys import stdin
input = stdin.readline

def gcd(a, b):
  return gcd(b, a % b) if b else a

t = int(input())
for i in range(t):
  num_list = list(map(int, input().split()))
  num_list = num_list[1:]
  ans = 0
  for a, b in combinations(num_list, 2):
    ans += gcd(a, b)
  print(ans)