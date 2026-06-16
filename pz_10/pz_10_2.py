#Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое,
#количество знаков препинания.
#Сформировать новый файл, в который поместить текст в стихотворной форме предварительно
#поставив последнюю строку между первой и второй.

t = 0
d = 0
punctuation = '.,!?;:-'

for i in open('text18-17.txt', encoding='UTF-8'):
    print(i, end='')
    t += 1
    for j in i:
        if j in punctuation:
            d += 1

print(end='\n')
print('Количество строк:', t, end='\n')
print('Количество знаков препинания:', d, end='\n')

# Читаем все строки в список
f1 = open('text18-17.txt', encoding='UTF-8')
l = f1.readlines()
f1.close()

l = [line.strip() for line in l if line.strip()]

if len(l) >= 3:
    new_l = [l[0], l[-1]] + l[1:-1]
else:
    new_l = l

print("\nНовый порядок строк:")
for line in new_l:
    print(line)

f2 = open('text18-17_new.txt', 'w', encoding='UTF-8')
for line in new_l:
    f2.write(line + '\n')
f2.close()

print('\nНовый файл создан: text18-17_new.txt')