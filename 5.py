# Задание 5.
# Вычислить сумму 1 - A + A² - A³ + ... ± A^N.

a = float(input("Введите A: "))
n = int(input("Введите N: "))

if n <= 0:
    print("Ошибка! N должно быть положительным.")
else:
    total = 1.0
    term = 1.0
    sign = -1.0

    for i in range(1, n + 1):
        term *= a
        total += sign * term
        sign *= -1

    print("Значение выражения =", total)