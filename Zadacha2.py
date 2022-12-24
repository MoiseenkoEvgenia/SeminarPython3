# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
res_list = []
left = 0
right = len(my_list)-1
while left < right:
    res_list.append(my_list[left] * my_list[right])
    left += 1
    right -= 1
else:
    if left == right:
        res_list.append(my_list[left] * my_list[right])
print(res_list)
