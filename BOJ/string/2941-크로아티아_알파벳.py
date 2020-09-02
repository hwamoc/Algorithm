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

'''by zzt
c=input().count;print(c('')-1-sum(map(c,['-','=','nj','lj','dz='])))
'''

'''by chsun0303
w=input();print(len(w)-sum(w.count(a)for a in['=','-','lj','nj','dz=']))
'''

'''by jhmoon2000
s=input()
print(len(s)-sum(map(s.count,['c=','c-','dz=','d-','lj','nj','s=','z='])))
'''

'''by texz
sep = ['=', '-', 'dz=', 'lj', 'nj']
s = input()
print(len(s) - sum(s.count(c) for c in sep))
'''

'''by macoto35
t=input()
for i in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
    t=t.replace(i,'0')
print(len(t))
'''

'''by sggunha
l=['c=','c-','dz=','d-','lj','nj','s=','z='];a=input();print(len(a)-sum([a.count(i) for i in l]))
'''

'''by sang0130
n=input()
m=len(n)
for i in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
    m-=n.count(i)
print(m)
'''

'''by wwiiiii
a = input()
for b in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
	a = a.replace(b, '0')
print(len(a)) 
'''