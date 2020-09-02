'''
# 예제 입력 1
baekjoon
'''
s = input()
sufx = []
for i in range(len(s)):
    sufx.append(s[i:])
for i in sorted(sufx):
    print(i)

'''by doublejy715
data = input()
lists = []
for index in range(len(data)):
    lists.append(data[index:])
print(*sorted(lists),sep='\n')
'''

'''by zox2323
s = input()
print("\n".join(sorted([s[x:] for x in range(len(s))])))
'''

'''by qlqnf16
string = input()
tails = []

for i in range(len(string)):
  tails.append(string[i:])

tails.sort()
print('\n'.join(tails))
'''

'''by kaspee
a=input();print(*sorted([a[i:]for i in range(len(a))]),sep="\n")
'''

'''by ohyuni
s = input()
a = [s[i:] for i in range(len(s))]
for x in sorted(a):
    print(x)
'''

# k=[*input()][::-1]
# 신기한거! *의 의미는 파라미터를 몇개 받을지 모를 경우 사용한대.
# 파라미터는 튜플 형태로 전달된대