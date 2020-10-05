'''
# 예제 입력 1
The Curious Case of Benjamin Button
# 예제 입력 2
Mazatneunde Wae Teullyeoyo
# 예제 입력 3
Teullinika Teullyeotzi
'''
import sys
l = sys.stdin.readline().split()
print(len(l))

'''
l = input().split()
print(len(l))
'''

'''by jamesujeon
s = input().strip()
print(s.count(' ') + 1 if s else 0)
'''

'''by theblinds
import sys
s = sys.stdin.read().strip()
if not s:
    print("0")
else:
    print(len(s.split(" ")))
'''