'''
# 예제 입력 1
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
'''
from sys import stdin
input = stdin.readline

t = int(input())

for _ in range(t):
    ans = "YES"
    n = int(input())
    phoneNo = [int(input()) for _ in range(n)]
    # print(phoneNo)
    # phoneNo.sort()
    l = len(str(phoneNo[0]))
    for i in phoneNo[1:]:
        if int(str(i)[:l]) == phoneNo[0]:
            print(int(str(i)[:l]))
            ans = "NO"
            break

    print(ans)

