def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial(0))
print(factorial(5))
print(factorial(-1))

def arrangements(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return factorial(n) // factorial(n - k)

print(arrangements(13, 6))
print(arrangements(4, 2))
print(arrangements(5, 5))
print(arrangements(3, 5))

def combinations(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

print(combinations(13, 6))
print(combinations(4, 2))
print(combinations(64, 0))
print(combinations(5, 0))
