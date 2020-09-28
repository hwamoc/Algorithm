'''
# 예제 입력 1
1 1
2 3
3 4
9 8
5 2
'''
import sys
input = sys.stdin.readline

while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

'''by totomo
import sys

for line in sys.stdin:
    print(sum(map(int,line.split())))
'''

'''by tinygun
import sys
for i in sys.stdin:
    a,b=map(int,i.split())
    print(a+b)
'''