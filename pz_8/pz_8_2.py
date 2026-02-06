s = 'Изучаем язык Питон.'
pre = s.split()

unik = {}

for a in pre:
    if a in unik.keys():
        unik[a] += 1
    else:
        unik[a] = 1

for x in unik.keys():
    print(x, ':', unik[x])