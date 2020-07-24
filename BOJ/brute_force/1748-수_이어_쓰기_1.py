'''
# 예제 입력 1
120
'''
from sys import stdin, stdout
input = stdin.readline

n = int(input())
l = len(str(n))

ans = 0

for i in range(1, l+1):
  stri = '9'* i
  inti = int(stri)
  if n > inti:
    ans += 10**(i-1) * 9 * i
  else:
    te = n - 10**(i-1)
    ans += te * i
    break

print(ans + l)

'''
n = int(input())

x = 1
ret = 0 

while True:
    if n >= 10**x:
        ret = ret + (10**x - 10**(x-1)) * x
        x += 1
    else:
        ret = ret + (n - 10**(x-1) + 1) * x
        break

print(ret)
'''
'''
n = int(input())
m, i = n, 9
while i < n:
    m += n-i
    i = i*10 + 9
print(m)
'''