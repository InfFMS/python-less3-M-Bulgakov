# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.

x = int(input())
k = 0
l = 0
while x != 0:
    s = 0
    if x == 4:
        l +=1
    elif x ==2:
        k +=1
    else:
        for i in range(1,((x-1)//2)+1):
            if x % i == 0:
                s += 1
        if x == 1:
            l += 1
        elif s == 1:
            k += 1
        else:
            l += 1

    x = int(input())
print(f'Простых чисел: {k} и Cоставных чисел: {l}')