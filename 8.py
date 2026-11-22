# Задание 8.
# Найти наименьшее K, при котором сумма
# 1 + 2 + ... + K не меньше N.

n = int(input("Введите N: "))

if n <= 1:
    print("Ошибка! N должно быть больше 1.")
else:
    k = 0
    total = 0

    while total < n:
        k += 1
        total += k

    print("Минимальное K =", k)
    print("Сумма =", total)