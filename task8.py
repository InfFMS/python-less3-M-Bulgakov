# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить, сколько было введено положительных и
# сколько отрицательных чисел (нули не считать!).

n = int(input())
k=0
l=0
for i in range(n):
    a = int(input())
    if a > 0:
        k+=1
    if a<0:
        l+=1
print(f'Больше 0: {k}, меньше 0: {l}')