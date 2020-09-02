'''
# 예제 입력 1
5
2
2 4
# 예제 입력 2
3
1
0
'''
from sys import stdin
input = stdin.readline
n, m = int(input()), int(input())
x = list(map(int, input().split()))
# 첫번째 & 마지막 거리 초기화
df = set([x[0], n-x[-1]])
# 가로등 사이 거리 / 2
for i in range(1, m):
    df.add((x[i]-x[i-1]+1) // 2)
print(max(list(df)))
# print(list(df)[-1]) 틀렸던 이유...
'''by hek0628
from sys import stdin
n = int(input())
m = int(input())
location = list(map(int, stdin.readline().split()))
gap = []
gap.append((location[0] - 0) * 2)
for i in range(1, m):
    gap.append(location[i] - location[i - 1])
gap.append((n - location[-1]) * 2)
a, b = divmod(max(gap), 2)  #나누는걸 max 찾고 딱 한번만 진행하는 거 참신..,
if b == 0:
    print(a)
else:
    print(a + 1)
'''

'''
from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))
# 첫번째 & 마지막 거리 초기화
ans = max(x[0], n-x[-1])
# 가로등 사이 거리 / 2
for i in range(1, m):
    ans = max(ans, (x[i]-x[i-1]+1)//2)
print(ans)
'''