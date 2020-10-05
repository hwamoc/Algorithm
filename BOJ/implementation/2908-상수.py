'''
# 예제 입력 1
734 893
'''
a, b = input().split()
# a = ''.join(reversed(a))
# b = ''.join(reversed(b))
# 이게 대략 8배 정도 빠름 (스트링 길이가 더 길어야 유의미한 차이가 있음)
print(max(int(a[::-1]), int(b[::-1])))


'''by kjh3141
print(max([int(i[::-1]) for i in input().split()]))
'''

'''by lurin
N = input().split()
N = [int(i[::-1]) for i in N]

print(max(N))
'''

'''by pythonhozier
a, b = input().split()
a = a[::-1]
b = b[::-1]

print(a if int(a) > int(b) else b)  # 두 수니까 이렇게 해도 
'''

'''by kdh6975   # 세자리 수니까 이렇게 해도 됨
a = input().split()
print(max(int(a[0][2]+a[0][1]+a[0][0]),int(a[1][2]+a[1][1]+a[1][0])))
'''

'''by arjasc521
a, b =input().split()

def reading(k):
    k = k[::-1]
    return int(k)

print(max([reading(a),reading(b)]))
'''