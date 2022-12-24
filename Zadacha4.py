# Напишите программу, которая будет преобразовывать десятичное число в 
# двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
string = ''
num_dec = int(input("Введите число в десятичной системе: "))
while num_dec > 0:
    string = str(num_dec % 2) + string
    num_dec = num_dec // 2

print(string)