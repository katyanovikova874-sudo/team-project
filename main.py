import temp
import discount

print("Добро пожаловать в программу!")
print("1 - Посчитать цену со скидкой")
print("2 - Перевести градусы Цельсия в Фаренгейты")

choice = input("Выберите номер действия (1 или 2): ")

if choice == "1":
    p = float(input("Введите цену товара: "))
    d = float(input("Введите размер скидки (%): "))
    res = discount.calc_discount(p, d)
    print("Итоговая цена со скидкой:", res)
elif choice == "2":
    c = float(input("Введите температуру в градусах Цельсия: "))
    res = temp.c_to_f(c)
    print("Температура по Фаренгейту:", res)
else:
    print("Неверный выбор")