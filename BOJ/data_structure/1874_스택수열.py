'''
# 예제 입력 1
8
4
3
6
8
7
5
2
1
# 예제 입력 2
5
1
2
5
3
4
'''

from sys import stdin
input = stdin.readline

stack = []
num = int(input())
t = list(range(num, 0, -1))
answer = ""

for _ in range(num):
  i = int(input())
  while len(stack) == 0 or stack[-1] < i:
    stack.append(t.pop())
    answer += '+\n'
  if stack[-1] == i:
    stack.pop()
    answer += '-\n'
if len(stack) or len(t):
    print("NO")
else:
    print(answer)