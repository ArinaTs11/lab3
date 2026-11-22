# Задание 3.
# Вычислить квадрат числа N как сумму первых N
# нечётных чисел и выводить промежуточные суммы.

n = int(input("Введите N: "))

if n <= 0:
    print("Ошибка! N должно быть положительным.")
else:
    total = 0

    for i in range(1, n + 1):
        odd_number = 2 * i - 1
        total += odd_number
        print("После добавления", odd_number, "сумма =", total)

    print("Квадрат числа", n, "=", total)