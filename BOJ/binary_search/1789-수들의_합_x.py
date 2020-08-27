'''
# 예제 입력 1
200
'''
from sys import stdin
input = stdin.readline

S = int(input())

start, end, = 1, S-1
while start <= end:
    if end - start > 1:
        start += 1
    end -= start

if start > S-start:
    print(start)
else:
    print(S-start)
