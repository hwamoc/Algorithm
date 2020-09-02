'''
# 예제 입력 1
adaabc aababbc
'''
from sys import stdin
input = stdin.readline

a,b = map(str, input().split())
al, bl = len(a), len(b)
l = bl - al

cnts = []
for i in range(l+1):
    cnt = 0
    temp = '0'*i + a + '0'*(l-i)
    for i,j in zip(temp, b):
        if i == j:
            cnt += 1
    cnts.append(cnt)

print(al-max(cnts))
# i = cnts.index(max(cnts))
# a = b[:i] + a + b[al+i:]

'''by bjchae9627
x, y = input().split()
minimum = 50

for i in range(len(y) - len(x) + 1):
    temp = 0
    for j in range(len(x)):
        if x[j] != y[i + j]:
            temp += 1
    if temp < minimum:
        minimum = temp

print(minimum)
'''

'''by gryps
A, B = input().split(" ")

a = len(A)
b = len(B)

counts = []
for i in range(b-a+1):
    count = 0
    for j in range(a):
        if A[j] != B[i+j]:
            count += 1
    counts.append(count)
print(min(counts))
'''

'''by skyisclear
X,Y=input().split()
a=len(X)
print(min(sum(X[j]!=Y[i+j]for j in range(a))for i in range(len(Y)-a+1)))
'''