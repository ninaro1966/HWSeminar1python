# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Ввведите число от 1 до 7: '))
if number > 5:
    print ('Да')
else:
    print("Нет")
