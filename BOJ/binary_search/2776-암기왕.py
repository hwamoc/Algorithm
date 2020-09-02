'''
# 예제 입력 1
1
5
4 1 5 2 3
5
1 3 7 9 5
'''
from sys import stdin
input = stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

t = int(input())
for _ in range(t):
    N = int(input())
    num = list(map(int, input().split()))
    M = int(input())
    guess = list(map(int, input().split()))
    num.sort()
    print(N, num, M, guess)

    for i in range(M):
        result = binary_search(num, guess[i], 0, N-1)
        if result == None:
            print(0)
        else:
            print(1)

'''
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = input()
    note = set(input().split())
    m = input()
    print('\n'.join('1' if number in note else '0' for number in input().split()))
# from 	teferi00, thx
'''

'''
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    buf = []
    for i in b:
        if i in a:
            buf.append('1')
        else:
            buf.append('0')
    print('\n'.join(buf))
'''

'''
import sys
input = sys.stdin.readline

def memorize():
    N = int(input())
    numbers = set(map(int, input().split(' ')))
    M = int(input())
    test_numbers = list(map(int, input().split(' ')))
                      
    results = ['1' if number in numbers else '0' for number in test_numbers]
    return results
    
T = int(input())
for test in range(T):
    for result in memorize():
        print(result)
'''

'''
for _ in range(int(input())):
	n = int(input())
	a = set(map(int,input().split()))
	m = input()
	b = list(map(int,input().split()))
	for x in b:
		if x in a:
			print(1)
		else:
			print(0)
'''