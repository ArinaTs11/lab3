# Задание 2.
# Вычислить произведение:
# 1,1 * 1,2 * ... * (1 + N / 10).

n = int(input("Введите N: "))

if n <= 0:
    print("Ошибка! N должно быть положительным.")
else:
    product = 1.0

    for i in range(1, n + 1):
        factor = 1 + i / 10
        product *= factor

    print("Произведение =",round(product,3))