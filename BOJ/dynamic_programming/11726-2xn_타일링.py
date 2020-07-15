'''
# 예제 입력 1
2
# 예제 입력 2
9
'''
from sys import stdin
input = stdin.readline

n = int(input())
dp = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
  if i == 2:
    dp[i] = dp[i-1] + 1
  else:
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)