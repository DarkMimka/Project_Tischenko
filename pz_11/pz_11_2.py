#Составить генератор (yield), который переведет символы строки из верхнего регистра в нижний.

def gen_lower(s: str):
    for x in s:
        yield x.lower()

b = "АБРИКОСЫЫ"
mygen = gen_lower(b)
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))