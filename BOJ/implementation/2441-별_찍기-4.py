'''
# 예제 입력 1
5
'''
n = int(input())
for i in range(n, 0, -1):
    print(' '*(n-i)+'*'*i)

'''
n = int(input())
for i in range(n):
    print(' '*i+'*'*(n-i))
'''