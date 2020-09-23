'''
# 예제 입력 1
2
6 12 10
30 50 72
# 예제 입력 2
2
6 12 12
30 50 72
'''
import sys
input = sys.stdin.readline
t = int(input())
def acm_hotel():
    h, w, n = map(int, input().split())     # (1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W)
    y = n % h
    x = n // h + 1

    if y == 0:
        y = h
        x -= 1
    print(y*100 + x)

for _ in range(t):
    acm_hotel()

'''by ksuk6603  # 나머지가 없을 때 필터링을 안해줘도 되는군
import sys

n = int(sys.stdin.readline())

for o in range(n):
    h, w, n = map(int, sys.stdin.readline().split())
    n -= 1
    c = (n // h) + 1
    r = ((n % h) + 1) * 100
    print(c + r)
'''

'''by byran1302
import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    h,w,n = map(int,input().split())
    print(str((n-1)%h+1) + str((n-1)//h+1).rjust(2,'0')) # rjust 라는 메서드가 인상적이군
'''

'''by his4000
import sys
T = int(sys.stdin.readline())

for t in range(T):
    h, w, n = map(int, sys.stdin.readline().split())
    print("%d%02d" % ((n-1)%h+1, (n-1)//h+1))   # "%02d" 이부분이 인상적 - 2자리 못채울시 0 채워넣는다
'''