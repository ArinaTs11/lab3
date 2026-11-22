# Задание 1.
# Дана цена 1 кг конфет.
# Вывести стоимость 0,1; 0,2; ...; 1 кг конфет.

price = float(input("Введите цену 1 кг конфет: "))

for tenths in range(1, 11):
    weight = tenths / 10
    cost = price * weight
    print(weight, "кг =", round(cost, 2), "руб.")

