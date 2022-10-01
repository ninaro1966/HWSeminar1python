# 2.Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Решение из  Google, которое понравилось, но оно не для всех значений предикат было.

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a
#
#
# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left = right
#     return result
#
#
# statement = inputNumbers(3)
#
# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
           if  not (x or y or z) != (not x and not y and not z ):
              print('Не выполняется')
              break

else:
    print('Выполняется')