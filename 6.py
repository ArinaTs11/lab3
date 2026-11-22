# Задание 6.
# Вывести числа от A до B.
# Каждое число повторить столько раз, каково его значение.

a = int(input("Введите положительное A: "))
b = int(input("Введите положительное B: "))

if a <= 0 or b <= 0 or a >= b:
    print("Ошибка! Требуется A > 0, B > 0 и A < B.")
else:
    for number in range(a, b + 1):
        for i in range(number):
            print(number, end=" ")
        print()