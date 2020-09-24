'''
# 예제 입력 1
0 32
3 13
28 25
39 0
'''
l = []
t = 0
for _ in range(4):
    n, m = map(int, input().split())
    t += m - n
    l.append(t)
print(max(l))

'''
cnt = M = 0
for i in range(4):
    a, b = map(int, input().split())
    cnt += b-a
    M = max(M, cnt) # if m<cnt: m=cnt
print(M)
'''