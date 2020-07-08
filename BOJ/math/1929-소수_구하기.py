'''
# 예제 입력 1
3 16
'''
from sys import stdin
input = stdin.readline

num_list = list(map(int, input().split()))
n = num_list[0]
m = num_list[1]

# 에라토스테네스의 체 (최대 값 이하에서 소수 찾기)
a = [False, False] + [True] * (m - 1)
primes = []  # 소수를 담는 배열 생성
for i in range(2, m + 1):
  if a[i]:  # a[i]이 소수일 때 아래 실행 (초기에 2 들어감. 다음은 3 들어감)
    primes.append(i)  # 소수를 primes 배열에 추가
    for j in range(2 * i, m + 1, i):  # 소수의 배수들을 걸러준다. (소수의 2배수 부터 시작 n+1까지)
      a[j] = False  # (초기에 2배수 모두 false, 다음은 3배수 false로..
# print(primes)                             # 다음은 5, 7, 11의 배수를 false.. 계속..!)

for i in range(len(primes)):
  if primes[i] > n-1:
    primes = primes[i:]
    print(primes)
    break

for num in primes:
  print(num, end='\n')
