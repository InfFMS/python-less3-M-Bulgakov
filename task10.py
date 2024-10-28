# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
import math
n = int(input())
x = int(input())
k = 0
l = 0
s = 0
M = x
m = x
r = x
z = 0
for i in range(int((math.sqrt(x)))):
    if x % (i+1) == 0:
        s += 1
if x == 1:
    l += 1
elif s == 1:
    k += 1
    M = r
    m = r
    z +=1
else:
    l += 1

for j in range(n-1):
    s = 0
    r = x
    for i in range((math.sqrt(x))):
        if x % (i+1) == 0:
            s += 1
    if x == 1:
        l += 1
    elif s == 1:
        k += 1
        if M < r:
            M = r
        if m > r:
            m = r
        z +=1
    else:
        l += 1

    x = int(input())
if z == 0:
    print('Нет')
else:
    print(f'Максимальное простое число:{M}, составных чисел:{m}')

