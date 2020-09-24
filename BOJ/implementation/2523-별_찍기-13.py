'''
# 예제 입력 1
3
'''
n = int(input())
for i in range(n):
	print('*'*(i+1))
for i in range(n-1):
	print('*'*(n-i-1))

'''
a = int(input())
for i in range(a):
    print('*' * (i+1))
for i in reversed(range(a-1)):
    print('*' * (i+1))
'''

'''by randoms
n=int(input())
for i in range(-n+1,n):
    print('*'*(n-abs(i)))
'''