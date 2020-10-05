'''
# 예제 입력 1
5
20 10 35 30 7
'''
import sys
input = sys.stdin.readline

input()
l = list(map(int, input().split()))
print(min(l),max(l))

'''
# 가변 변수 인자 사용하면 시간을 줄일 수 있다
import sys

a, *b = map(int, sys.stdin.read().split())
print(min(b), max(b))
'''