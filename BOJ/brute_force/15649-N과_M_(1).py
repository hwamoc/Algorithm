'''
# 예제 입력 1
3 1
# 예제 입력 2
4 2
# 예제 입력 3
4 4
'''
from sys import stdin
from itertools import permutations
input = stdin.readline

n, m = map(int, input().split())
items = [i for i in range(1, n+1)]

perm = []
for i in list(permutations(items, m)):
    perm.append(i)

for i in perm:
    print(' '.join(map(str, i)))  # tuple -> str

'''
from itertools import permutations

N, M = map( int, input().split() )
nums = [ str(x) for x in range( 1, N + 1 ) ]

print( '\n'.join( [ ' '.join( perm ) for perm in permutations( nums, M ) ] ) )
'''
'''
from itertools import permutations

N, M = map(int, input().split())
li = map(str, range(1, N+1))
print('\n'.join(list(map(' '.join,permutations(li, M)))))
'''