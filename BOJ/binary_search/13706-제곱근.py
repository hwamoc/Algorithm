'''
# 예제 입력 1
36
# 예제 입력 2
81
# 예제 입력 3
226576
'''
from sys import stdin
input = stdin.readline

N = int(input())
start, end = 0, N
while start <= end:
    mid = (start + end) // 2
    if mid**2 <= N:
        if mid**2 == N:
            ans = mid
        start = mid+1
    else:
        end = mid-1

print(ans)

'''by domece
s=input()
i=int(s)
r=int(10**int(len(s)/2))
while r*r!=i:
	r=(r+i//r)//2
print(r)
'''
'''by mksmk606
n = int(input())
s = 1
f = 10**400+1

while s+1 < f:
    mid = (s+f)//2
    if mid*mid <= n:
        s = mid
    else:
        f = mid

print(s)
'''

'''by singun11
n = int(input())
s,e = 0,n
ans = 0
while s <= e:
    mid = (s+e)//2

    if mid*mid <= n:
        if mid >ans:
            ans = mid
        s = mid+1
    else:
        e = mid-1
print(ans)
'''
# 런타임 에러: math.qurt 와 pow 둘다 런타임 에러 발생
# 800자리의 제곱근도 400자리 - double에서 정확도가 떨어지는 수준이 아니고 아예 안 들어가기 때문에 float를 아예 안 쓰고 계산해야 한다.
# 이유: pow(n, 0.5), a**0.5 에서 계산할 때 float가 등장한다.
# from sys import stdin
# input = stdin.readline
#
# ans = pow(int(input()), 0.5)
# if ans == 0:
#     print(0)
# else:
#     print(ans)