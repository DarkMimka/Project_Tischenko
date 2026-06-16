#В последовательности на n целых чисел умножить все элементы на последний минимальный элемент.

a = [1, 2, 3, 100, 6, 7, 8, 9, 10, -2]
a = [x * a[-1] for x in a]

def gen_lower(s: str):
    for x in s:
        yield x.lower()

b = "АБРИКОСЫЫЫ"
mygen = gen_lower(b)
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
