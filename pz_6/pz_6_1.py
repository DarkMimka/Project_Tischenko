#Дан список размера N и целые числа K и L (1 < K < L < N).
# Найти сумму элементов списка с номерами от K до L включительно.

len_n = 20
k = 5
l = 7

if 1 < k < l < len_n:
    print(f'Условие соблюдено: N={len_n}, k={k}, l={l}')

n = [x for x in range(k, l+1)]
sum = 0
for x in n:
    sum += x
print('Сумма элементов от k до l:', sum)