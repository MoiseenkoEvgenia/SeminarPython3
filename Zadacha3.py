# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов, 
# отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
my_list = []
for _ in range (5):
    amount = random.randint(0, 3)
    number = round(random.uniform(-5, 5), amount)
    if number == int(number):
        my_list.append(int(number))
    else:
        my_list.append(number)

print(my_list)
res_list = []
for el in my_list:
    res_list.append(str(el).split('.'))
print(res_list)
max = 0
min = 99
for res in res_list:
    if len(res) < 2:
        break
    elif int(res[1]) > int(max):
        max = int(res[1])
    elif int(res[1]) < int(min):
        min = int(res[1])
result = max - min
print(result)
