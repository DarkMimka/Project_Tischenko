#Составить функцию решения задачи.
# Из заданного числа вычли сумму его цифр.
# Из результата вновь вычли сумму его цифр и т. д.
# Через сколько таких действий получится нуль?

def subtract_digits(n):
    num_str = str(n)
    digit_sum = sum(int(digit) for digit in num_str)
    count = 0

    while n != 0:
        n = n - digit_sum
        if n < 0:
            n = -n
        digit_sum = sum(int(digit) for digit in str(n))
        count += 1
    return count

number = int(input("Введите число: "))
result = subtract_digits(number)
print(f"Нуль получился после {result} вычитаний")