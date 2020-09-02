'''
# 예제 입력 1
3
happy
new
year
# 예제 입력 2
4
aba
abab
abcabc
a
'''
from sys import stdin
input = stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
print(words)

for w in words:
    group = []
    print(w)
    for i in range(1, len(w)):
        group.append(w[0])
        if w[i] in group:
            if w[i] != w[i-1]:
                print(w[i])
                n -= 1
                break
        else:
            group.append(w[i])
            print(group)
            print("????",w[i])
print(n)

'''by baek4055
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):       #  if list(word) == sorted(word, key=word.index):
        result += 1
print(result)   
'''

'''by wnstj444
word=[]

num=int(input(""))

for i in range(num):
    word=input("")
    for j in range(1,len(word)):
        if word.find(word[j-1])>word.find(word[j]):
           num-=1
           break

print(num)
'''

'''by love94610
def group_word(s):
    l = []
    for i in s:
        k = s.find(i)
        if k not in l or k == l[-1]:
            l.append(k)
        else:
            return False
    return True

t = int(input())
sum = 0
for i in range(t):
    if group_word(input()):
        sum +=1
print(sum)
'''