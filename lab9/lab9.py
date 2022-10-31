from prettytable import PrettyTable
from sympy import diff, symbols, sin, atan, exp, log, ln

def f(x):
    return sin(x)
    # return exp(2-x)+x*atan(x)-0.5*ln(1+pow(x, 2))
    # return 1.5*pow((x+1.5), 2)*(x-1.1)*(x-0.75)

def f_():
	x = symbols('x')
	return diff(f(x))

def f__():
	return diff(f_())


def calc(x0, sigma):
    prettyTable = PrettyTable()
    prettyTable.field_names = ["№", "xk", "f'(xk)"]
    k = 0
    xk = x0
    fs = f_().subs('x', xk)
    fss = f__().subs('x', xk)
    prettyTable.add_row([k, xk, fs])

    while (abs(fs) > sigma):
        xk = xk - fs/fss
        fs = f_().subs('x', xk)
        k = k + 1
        prettyTable.add_row([k, xk, fs])

    print(prettyTable)
    return xk


if __name__ == '__main__':
    x0, sigma = 4.094, 0.01
    # x0, sigma = 0.9, 0.01
    # x0, sigma = -1.55, 0.01
    result = calc(x0, sigma)
    print(result)