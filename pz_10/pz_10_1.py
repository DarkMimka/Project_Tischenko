#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел.
#Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Произведение элементов:
#Количество пар, для которых произведение элементов делится на 3 (элементы пары в последовательности являются соседними):

numbers = ['-5 12 -8 3 6 -9 15 2 -4 7']
f3 = open('data_17.txt', 'w')
f3.writelines(numbers)
f3.close()

f4 = open('result_17.txt', 'w')
f4.write('Исходные данные:')
f4.write('\n')
f4.writelines(numbers)
f4.close()

f3 = open('data_17.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

prod = 1
for i in range(len(k)):
    prod = prod * k[i]

count_pairs = 0
for i in range(len(k) - 1):
    if (k[i] * k[i + 1]) % 3 == 0:
        count_pairs += 1

f4 = open('result_17.txt', 'a')
f4.write('\n')
print('Количество элементов:', len(k), file=f4)
print('Произведение элементов:', prod, file=f4)
print('Количество пар, для которых произведение элементов делится на 3:', count_pairs, file=f4)
f4.close()