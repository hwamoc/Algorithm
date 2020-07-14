'''
# 예제 입력 1
6
10 20 10 30 20 50
6
50 40 20 10 50 60
'''
from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = [1] * n

for i in range(1, n):
  for j in range(i):
    if arr[j] < arr[i]:
      result[i] = max(result[i], result[j]+1)
      
print(result, max(result))