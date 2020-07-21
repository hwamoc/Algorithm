'''
# 예제 입력 1
3 1
# 예제 입력 2
4 2
# 예제 입력 3
4 4
'''
from itertools import combinations

N, M = map(int, input().split())
li = map(str, range(1, N+1))
print('\n'.join(list(map(' '.join,combinations(li, M)))))