'''
# 예제 입력 1
3
29
38
12
57
74
40
85
61
'''
# input은 항상 string 타입임을 명심 :)
import sys
input = sys.stdin.readline
l = []
for _ in range(9):
    l.append(int(input()))
print(max(l))
print(l.index(max(l))+1)

'''
l=[int(input())for i in range(9)]
print(max(l),l.index(max(l))+1)
'''

'''by bds511
print(*sorted([[int(input()),i+1]for i in range(9)])[-1],sep="\n")
'''

'''by felis
l=[0]
exec("l.append(int(input()));"*9)   # exec 라는 명령어를 사용한 풀이
m=max(l)
print(m,l.index(m))
'''