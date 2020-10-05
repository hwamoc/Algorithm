'''
# 예제 입력 1
2
3 ABC
5 /HTP
'''
t = int(input())
for _ in range(t):
    r, s = input().split()
    ans = ''
    for i in s:
        ans += i * int(r)
    print(ans)

'''by rhino333
t= int(input())
for i in range(t):
    a,b = input().split()
    for x in b:
        print(int(a)*x,end='')  # 이렇게 해도 된당
    print()
'''

'''by soos196   # for문 대신 while문
T = int(input())

while T:
    repeat, string = input().split()
    repeat = int(repeat)
    
    for i in string:
        print(i * repeat, end='')
        
    print("")
    T -= 1
'''