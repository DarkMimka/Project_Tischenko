#Дано целое число N (> 0).
# Найти сумму 1n + 2n-1 + ... + N¹.

def _fact(n):
    if n == 0:
        return 1
    if n > 0:
        return n * _fact(n-1)
    else:
        return (n * _fact(n+1))

def fact(n):
    res = _fact(n)
    if n > 0:
        return res
    else:
        return -res

n = 17
c = 1
res = 0
while n:
    res += c**n
    n -= 1
    c += 1
print(f'n19_2: {res} for n = 17')