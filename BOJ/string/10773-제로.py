'''
# 예제 입력 1
4
3
0
4
0
# 예제 입력 2
10
1
3
5
4
0
0
7
0
0
6
'''
from sys import stdin
input = stdin.readline

t = int(input())
accnt = []
for _ in range(t):
    z = int(input())
    if z == 0:
        accnt.pop()
    else:
        accnt.append(z)

print(sum(accnt))


'''by y1346130
from sys import stdin
input()
l=[]
for i in map(int, stdin):
    l.append(i) if i else l.pop()
print(sum(l))
'''

'''by jeukoh
import sys

N = int(input())
stack = []
K = list(map(int,sys.stdin.read().split()))

for i in K:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)
        
print(sum(stack))
'''