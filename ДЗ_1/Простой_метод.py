import random as r

def f(n, arr):
    ans = 0
    for i in range(len(arr)):
        ans += n**i*arr[i]
    return ans

def dih(a, b, arr):

    x_i = 0
    x_l = []
    e = 10**-15

    #1
    x_0 = r.randint(a, b)
    x_1 = r.randint(a, b)
    while f(x_0, arr) * f(x_1, arr) >= 0:
        x_0 = r.randint(a, b)
        x_1 = r.randint(a, b)

    #2-4
    x_2 = (x_0 + x_1)/2
    
    while abs(abs(x_2) - abs(x_1)) > e and (f(x_0, arr)*f(x_2, arr)<0 or f(x_2, arr)*f(x_1, arr)< 0):
        x_0 = x_1
        x_1 = x_2
        x_2 = (x_0 + x_1) / 2

    if (f(x_0, arr)*f(x_2, arr)<0 or f(x_2, arr)*f(x_1, arr)< 0):
        return 'Алярм'
    return f'{x_2}'


a = int(input('A: '))
b = int(input('B: '))

print(dih(a, b, [2, 1, 2, 3]))
