# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = [2, -3, 5, 9, 3]
count = 1
sum = 0
while count < len(n):
    sum += n[count]
    count += 2
print(sum)

