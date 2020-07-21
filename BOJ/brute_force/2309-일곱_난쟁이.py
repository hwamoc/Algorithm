'''
# 예제 입력 1
20
7
23
19
10
15
25
8
13
'''
from sys import stdin, stdout
input = stdin.readline

nanj = []
for _ in range(9):
  nanj.append(int(input()))
diff = sum(nanj) - 100

def two_sum(nums, target):
  for i in range(len(nums)):
    num = nums[i]
    pair = target - num
    hash = [x for x in nums[i+1:]]

    if pair in hash:
      nanj.remove(num)
      nanj.remove(pair)
      return nanj
  return None

answer = two_sum(nanj, diff)

print(*sorted(answer),sep='\n')

'''
l=sorted(int(input())for i in range(9))
for i in l:
 for j in l:
  if i+j==sum(l)-100:
    l.remove(i);
    l.remove(j);
  break
for i in l:
  print(i)
'''
'''
from itertools import *
a=[int(input()) for i in range(9)]
p=list(combinations(a,7))
for i in p:
    if sum(i)==100:
        print(*sorted(i),sep='\n')
        break
'''