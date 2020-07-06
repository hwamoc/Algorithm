'''
# 예제 입력 1
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
# 예제 입력 2
3
((
))
())(()
'''
from sys import stdin
input = stdin.readline

count = int(input())

for _ in range(count):
    stack = []
    lastStack = []
    inputArr = list(input().rstrip())

    for i in inputArr:
        if i == "(":
            stack.append(i)
        else:
            if len(stack):
                stack.pop()
            else:
                lastStack.append(i)

    if (len(stack) or len(lastStack)):
        print("NO")
    else:
        print("YES")