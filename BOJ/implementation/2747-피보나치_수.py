'''
# 예제 입력 1
10
'''
# [참고] https://shoark7.github.io/programming/algorithm/피보나치-알고리즘을-해결하는-5가지-방법

# for문을 활용한 반복적 풀이: 시간 복잡도는 O(n)
def fibo(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return b
print(fibo(int(input())))


'''
# 반복적 동적 계획법
def fibo(n):
    if n < 2:
        return n

    cache = [0 for _ in range(n+1)]
    cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]

print(fibo(int(input())))
'''

'''
# 재귀적 동적 계획법
def fibo(n):
    cache = [-1 for _ in range(n+1)]

    def iterate(n):
        if n < 2:   # 기저 사례 1 (탈출 조건)
            return n

        if cache[n] != -1:  # 기저 사례 2 (탈출 조건 2)
            return cache[n]

        cache[n] = iterate(n-1) + iterate(n-2)
        return cache[n]
    return iterate(n)

print(fibo(int(input())))
'''

'''
n = int(input())
A = [0,1]
if n < 2:
    print(n)
else:
    for i in range(2, n+1):
        A.append(A[i-2]+A[i-1])
    print(A[n])
'''

'''
# 파이썬 함수의 동작방식을 활용한 방법
def fibo(n, __cache={0: 0, 1: 1}):
    """Get nth fibonacci number"""
    if n in __cache:
        return __cache[n]

    __cache[n] = fibo(n-1) + fibo(n-2)
    return __cache[n]

print(fibo(int(input())))

# 함수 정의부에 적으면 그 자료구조는 함수가 정의될 때 생성되어 함수가 호출될 때나, 종료될 때나 상관없이 함수 자체가 메모리에서 지워지기 전까지는 값이 유지된다
'''

'''
# 행렬 곱셈을 활용한 풀이
def fibo(n):
    SIZE = 2
    ZERO = [[1, 0], [0, 1]] # 행렬의 항등원
    BASE = [[1, 1], [1, 0]] # 곱셈을 시작해 나갈 기본 행렬

    # 두 행렬의 곱을 구한다
    def square_matrix_mul(a, b, size=SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += a[i][k] * b[k][j]
        return new

    # 기본 행렬을 n번 곱한 행렬을 만든다
    def get_nth(n):
        matrix = ZERO.copy()
        k = 0
        tmp = BASE.copy()

        while 2 ** k <= n:
            if n & (1 << k) != 0:
                matrix = square_matrix_mul(matrix, tmp)
            k += 1
            tmp = square_matrix_mul(tmp, tmp)
        return matrix

    return get_nth(n)[1][0]


print(fibo(int(input())))
'''

'''
# 일반항 사용
def fibo(n):
    sqrt_5 = 5 ** (1/2)
    ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )
    return int(ans)

print(fibo(int(input())))
'''

''' # 시간초과: 시간 복잡도는 함수가 한 번 호출되면 다시 두 번 호출되기 때문에 지수적으로 증가해 O(2의 n승)이 된다. 
def fibo(n):
    return fibo(n-1) + fibo(n-2) if n >= 2 else n
'''