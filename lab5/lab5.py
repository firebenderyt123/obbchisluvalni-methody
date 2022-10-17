import math
from prettytable import PrettyTable

def f(x):
    # return 2*x**2 - 4*x + 16 / x
    # return math.sin(x)
    # return math.exp(2-x)+x*math.atan(x)-0.5*math.log10(1+pow(x, 2))

def calc(a, b, eps):
    prettyTable = PrettyTable()
    prettyTable.field_names = ["n", "x1", "x2", "f(x1)", "f(x2)", "a", "b", "L"]

    L = b - a
    num = L / eps

    fib1 = 1
    fib2 = 1
    i = 0
    while num >= fib2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1

    k = i
    R = fib1/fib2
    n = 0
    x2 = a + R*L
    x1 = a + b - x2
    f1 = f(x1)
    f2 = f(x2)

    prettyTable.add_row([0, "", "", "", "", a, b, L])
    while k >= n:
        try:
            if f1 < f2:
                b = x2
                x2 = x1
                f2 = f1
                x1 = a + b - x2
                f1 = f(x1)
            else:
                a = x1
                x1 = x2
                f1 = f2
                x2 = a + b - x1
                f2 = f(x2)
            n += 1
            L = b - a
            prettyTable.add_row([n, x1, x2, f1, f2, a, b, L])
        except Exception as e:
            print("Error:", e)
            print(prettyTable)
            return

    x = (a + b) / 2
    print(prettyTable)
    print('Result:', x, f(x))

if __name__ == '__main__':
    # a, b, eps = 1.5, 2.4, 0.1
    # a, b, eps = -3*math.pi, math.pi, 0.1
    # a, b, eps = 0.9, 2.9, 1e-3
    calc(a, b, eps)