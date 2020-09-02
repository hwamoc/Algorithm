'''
# 예제 입력 1
5
4 1 5 2 3
5
1 3 7 9 5
'''
from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()
print(N, A, M, B)


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in range(M):
    result = binary_search(A, B[i], 0, N-1)
    if result == None:
        print(0)
    else:
        print(1)


'''
def main():
    input()
    n = input().strip().split(' ')
    input()
    
    s = set(n)
    r = ''
    for k in input().strip().split(' '):
        r += '1\n' if k in s else '0\n'
    print(r)

if __name__ == "__main__":
    main()
'''

'''
import sys
input = sys.stdin.readline

def BOJ_1920():
    n,A,m = input(),set(input().split()),input()
    res=""
    for i in input().split():
        res += "1\n" if i in A else "0\n"
    print(res)
BOJ_1920()
'''

'''
import sys
input = sys.stdin.readline
input()
num = set(input().split())
input()
res = []
for n in input().split():
    res.append(n in num)
print('\n'.join(['1' if r else '0' for r in res]))
'''