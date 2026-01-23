#Дано вещественное число X и целое число N (> 0).
# Найти значение выражения X - X³/(3!) + X⁵/(5!) - ... + (-1)n-X2-n+1/((2-N+1)!) (N! = 12 ... N).
# Полученное число является приближенным значением функции sin в точке X.

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

x = 0.5
n = 12
res = x
while n:
    res += (-1)**n - x**(2-n+1) / (fact(2-n+1))
    n -= 3
print(f"n19_1: {res} for n = 12")