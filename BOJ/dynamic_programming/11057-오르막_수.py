'''
# 예제 입력 1
1
# 예제 입력 2
2
# 예제 입력 3
3
'''
from sys import stdin
input = stdin.readline

# 끝자리가 0~9인 개수를 모두 따져본다.
# nc[i][j]는 i자리 수에서 j로 끝나는 수들의 총 개수
# nc[i][j] = nc[i-1] + nc[i][j-1] 라는 점화식을 가진다.
N = int(input())
nc = [[1]*10 for _ in range(N+1)]
mod = 10007
print(nc)

for i in range(2, N+1):
  for j in range(1, 10):
    nc[i][j] = (nc[i-1][j] + nc[i][j-1]) % mod
  print(nc)
print(sum(nc[N])%mod)

'''
N = int(input())
nums = [1] * 10
mod = 10007

for _ in range(N-1):
  for i in range(1, 10):
    nums[i] = (nums[i] + nums[i-1]) % mod
    print(nums[i])
  print("--------------")
sys.stdout.write(str(sum(nums) % mod))
'''

'''
k=int(input())
result=1
for i in range(9+k,9,-1):
    result*=i
for i in range(1,k+1):
    result//=i
print(result%10007)
'''