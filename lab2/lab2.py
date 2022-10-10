import math

def test_f(x):
    return math.sin(x)

def f(x):
    return math.exp(2-x)+x*math.atan(x)-0.5*math.log10(1+pow(x, 2))

def calc(func, a, b, sigma, eps):
    L = b - a
    print('[' + str(a) + ';', str(b) + ']', round(L, 3))

    while (L > sigma):

        x1 = ((a + b)/2) - eps/2
        x2 = x1 + eps
        func_x1 = func(x1)
        func_x2 = func(x2)

        if func_x1 > func_x2:
            a = x1
        elif func_x1 < func_x2:
            b = x2
        else:
            a = x1
            b = x2
        L = b - a
        print(
            round(x1, 3), round(x2, 3),
            round(func_x1, 3), round(func_x2, 3),
            '[', round(a, 3), round(b, 3), ']', round(L, 3)
        )
    return a, b

def test():
    a = -2*math.pi
    b = 0
    sigma = 0.1
    eps = 0.01

    newA, newB = calc(test_f, a, b, sigma, eps)

    x = (newA + newB) / 2

    return x, test_f(x)

def prod():
    a = 0.9
    b = 2.9
    sigma = 0.1
    eps = 0.01

    newA, newB = calc(f, a, b, sigma, eps)

    x = (newA + newB) / 2

    return x, f(x)

if __name__ == '__main__':

    # x, y = test()
    x, y = prod()

    print('\n', x, y)