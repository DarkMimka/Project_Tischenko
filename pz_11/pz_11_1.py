#В последовательности на n целых чисел умножить все элементы на последний минимальный элемент.

def multiply_by_last_min(sequence):
    if not sequence:
        return []

    min_val = min(sequence)

    last_min_index = max(
        filter(lambda idx: sequence[idx] == min_val, range(len(sequence))),
        default=None
    )

    if last_min_index is None:
        return sequence

    multiplier = sequence[last_min_index]

    result = list(map(lambda x: x * multiplier, sequence))

    return result

numbers = [3, -2, 7, -2, 5, 1, -2, 4]
print('Исходная последовательность', numbers)
print('Результат умножения на последний минимальный элемент:', multiply_by_last_min(numbers))