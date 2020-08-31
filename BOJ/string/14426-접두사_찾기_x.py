'''
# 예제 입력 1
5 10
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
star
start
code
sunday
coding
cod
online
judge
plus
'''
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
s = [input().rstrip() for _ in range(n)]
check = tuple([input().rstrip() for _ in range(m)])
s.sort()
# check.sort()
print(s)
print(check)
cnt = 0
# for i in check:
for st in s:
    l = len(check)
    if check == st[:l]:
        cnt += 1
        break
print(cnt)


'''시간초과1
for i in check:
    for st in s:
        l = len(i)
        if i == st[:l]:
            cnt += 1
            break
'''
'''시간초과1
for i in check:
    for st in s:
        if st.startswith(i):
            cnt += 1
            break
'''