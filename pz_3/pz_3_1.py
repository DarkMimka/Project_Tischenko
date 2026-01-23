#Проверить истинность высказывания среди трех данных целых чисел есть хотя бы одна пара совпадающих.

def check_duplicate(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False
num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
num3 = int(input("Введите третье число:"))

if check_duplicate(num1, num2, num3):
    print("Среди трёх данных чисел есть хотя бы одна пара совпадающих.")
else:
    print("Среди трёх данных чисел нет пар совпадающих.")