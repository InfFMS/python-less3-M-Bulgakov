#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
x = int(input())
k = 0
l = 0
while x != 0:
    if x > 0:
        k += 1
    if x < 0:
        l += 1
    x = int(input())
print(f'Положительных чисел:{k}, отрицательных чисел:{l}')