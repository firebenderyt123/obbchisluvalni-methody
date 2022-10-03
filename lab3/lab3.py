import math

def toFixed(num, digits = 2):
    return f"{num:6.{digits}f}".format(12)

def f(x):
    return pow(x, 2)
    # return 2*pow(x, 2) - 4*x + 16/x
    # return pow(100-x, 2)
    # return math.exp(2-x)+x*math.atan(x)-0.5*math.log10(1+pow(x, 2))

def calc(a, b, eps):
    L = b - a
    while L > eps:
        x1 = a + 0.25 * L
        x2 = b - 0.25 * L
        xm = (a + b) / 2
        print(
            'x1:', toFixed(x1), 'xm:', toFixed(xm),
            'x2:', toFixed(x2), 'f(x1):', toFixed(f(x1)),
            'f(x2):',toFixed(f(x2)), 'a:', toFixed(a),
            'b:', toFixed(b), 'L:', toFixed(L)
        )
        if (f(x1) < f(xm)):
            b = xm
            xm = x1
        else:
            if (f(x2) < f(xm)):
                a = xm
                xm = x2
            else:
                a = x1
                b = x2
        L = b - a
    return xm, f(xm), L

if __name__ == '__main__':
    x, y, L = calc(-10, 15, 1e-3)
    print('\n\nx:', x, 'y:', y, 'Точність:', L)