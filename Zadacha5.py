# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных 
# индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
k = int(input("Введите целое число: "))
fib_list = [0, 1]
nega_fib_list = [0, 1]
result_list = []
for i in range(2, k+1):
    fib_list.append(fib_list[i-2] + fib_list[i-1])
    nega_fib_list.append(nega_fib_list[i-2] - nega_fib_list[i-1])
nega_fib_list.reverse()
del fib_list[0]
result_list = nega_fib_list + fib_list
print(result_list)
