'''
# 예제 입력 1
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
'''
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
ns = [input() for _ in range(n)]
ms = [input() for _ in range(m)]
ns.sort()

cnt, ans = 0, []
for target in ms:
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if ns[mid] == target:
            cnt += 1
            ans.append(target)
            break
        elif ns[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
ans.sort()
print(cnt)  # len을 사용해도 되지만 cnt 세는게 더 빠름
print(''.join(ans))
# input().rstrip() 써서 인풋받으면 출력할 때 '\n'.join 해줘야 함
# sys.stdout.write("{0}\n".format(len(noHearNoSee)))
# print(*sorted(res), sep="\n")

# 파사기
'''by shg9411
import sys
n, m = map(int, input().split())
person = sys.stdin.read().splitlines()
hear = set(person[:n])
see = set(person[n:])
ret = list(hear & see)
ret.sort()
print(len(ret))
for i in ret:
    print(i)
'''

'''by jhb1365
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
a,b = set([input() for _ in range(N)]), set([input() for _ in range(M)])
c = sorted(a.intersection(b))       # intersection 이라는 내장함수가 있구나
print(len(c))
print("".join(c))
'''

'''by tjtjdals
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
a = set(read() for _ in range(n))
b = set()
for _ in range(m):
    c = read()
    if c in a:      # 두번째 인풋 리스트를 받을 때 판별
        b.add(c.strip('\n'))

print(len(b))
for i in sorted(b):
    print(i)    
'''

'''시간초과
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
ns = [input().rstrip() for _ in range(n)]
ms = [input().rstrip() for _ in range(m)]
cnt, ans = 0, ""
for i in ns:
    if i in ms:
        cnt += 1
        ans += i + '\n'
print(cnt)
print(ans)
'''