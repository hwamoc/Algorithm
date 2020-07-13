'''
# 예제 입력 1
3
'''
from sys import stdin
input = stdin.readline

n = int(input())
dp = [1 for _ in range(n + 1)]

for i in range(3, n + 1):
  if i == 3:
    dp[i] = dp[i-2] * 2
  else:
    dp[i] = dp[i-2] * 2 + dp[i-3]

print(dp[n])