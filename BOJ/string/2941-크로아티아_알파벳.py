'''
# 예제 입력 1
ljes=njak
# 예제 입력 2
ddz=z=
# 예제 입력 3
nljj
# 예제 입력 4
c=c=
'''
from sys import stdin
input = stdin.readline

x = input().rstrip()
cnt, idx = 0, True
target = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

while True:
    while idx:
        for i in target:
            if x.find(i) == 0:
                cnt += 1
                x = x.replace(i, "", 1)
                break
            if i == target[-1]:
                idx = False
    if x:
        cnt += 1
        x = x[1:]
        idx = True
    else:
        break

cnt += len(x)
print(cnt)