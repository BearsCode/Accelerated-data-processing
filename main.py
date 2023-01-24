# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

numbers = [1, 2, 3, 4, 22, 234, 24]
result = list(filter(lambda x: x >= 10 and x < 100, numbers))
print(" ".join(map(str, result)))


# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

lst = [12,'sadf',5643]

letters = list(filter(lambda x: type(x) == str, lst))
numbers = list(filter(lambda x: type(x) == int, lst))

print("Letters: ", letters)
print("Numbers: ", numbers)


# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float (input("Введите число: "))
digits = [int (d) for d in str (number)]
sum_of_digits = sum (digits)
print("Сумма цифр ", number, "равно: ", sum_of_digits)
