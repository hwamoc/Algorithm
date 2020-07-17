'''
# 예제 입력 1
4
3 5 2 7
# 예제 입력 2
4
9 5 4 8
'''
from sys import stdin
input = stdin.readline

stack = []
num = int(input())
num_list = list(map(int, input().split()))
result = [-1 for _ in range(num)]

for i in range(num):
  try:
    while num_list[stack[-1]] < num_list[i]:
      result[stack.pop()] = num_list[i]
  except:
    pass

  stack.append(i)

for i in range(num):
  print(result[i], end=' ')