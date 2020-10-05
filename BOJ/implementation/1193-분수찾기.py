'''
# 예제 입력 1
14
'''
n = int(input())
cnt = 0

while n>0:
    cnt += 1
    n -= cnt

if cnt % 2 == 0:
    print(str(cnt+n) + '/' + str(1-n))
else:
    print(str(1-n) + '/' + str(cnt+n))

'''by qazxcv6090
X=int(input())
cnt=1
while(X>0):
    X-=cnt
    cnt+=1
if cnt%2==1:
    print(X+cnt-1,'/',-X+1,sep='')  # 이렇게 프린트해도 된다. 
else:
    print(-X+1,'/',cnt+X-1,sep='')
'''



'''by egas
n = int(input())
add = 1
while n > add:
    n = n - add
    add += 1
a = n
b = add - n + 1
if add % 2 == 1:
    a, b = b, a     # 이렇게 처리한 부분이 간결해 보인다. 파이썬을 잘 활용한 거 같다
print(str(a)+"/"+str(b))
# print("%d/%d"%(d,e))    # 혹은 이렇게 프린트 할 수도 있다 by bds511 
'''

'''by kiera
X=int(input())
i=1
x=X
while(x>i):
	x-=i
	i+=1
a=str(i+1-x)
b=str(x)
print(a+"/"+b if i&1 else b+"/"+a)  # if else문으로 출력해도 괜찮은 거 같다
'''

'''by mellonggo
# 2 곱하고  1/2 제곱해서 풀기 
a=float(input())
b=(a*2)**(0.5)//1
if (a*2)>b*(b+1) : b+=1
n=a-(b-1)*b/2
c=b-n+1
if b%2==1: n,c=c,n
print(str(int(n))+'/'+str(int(c)))
'''