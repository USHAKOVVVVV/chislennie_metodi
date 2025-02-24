import random as r

# Нахождение знач-а ф-ии
def f(n, arr):
    ans = 0
    for i in range(len(arr)):
        ans += n**i*arr[i]
    return ans

# Шарарам
def f_d(n, arr):
    ans = 0
    for i in range(len(arr)):
        ans += n**(i-1)*arr[i]*i
    return ans

def dih(a, b, arr):

    e = 10**-15

    x_0 = r.randint(a, b)

    while True:
        x_1 = x_0 - f(x_0, arr)/f_d(x_0, arr)

        if abs(abs(x_1) - abs(x_0)) < e:
            return (x_1)

        x_0 = x_1

a = int(input('A: '))
b = int(input('B: '))

print(dih(a, b, [2, 1, 2, 3]))
