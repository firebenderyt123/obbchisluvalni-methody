from prettytable import PrettyTable
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def draw_plot(x):
    plt.figure()
    plt.scatter(x[:, 0], x[:, 1], s = 170)
    t1 = plt.Polygon(x[:3,:])
    plt.gca().add_patch(t1)
    plt.show()

def f(x):
    return (1-x[0])**2 + (2-x[1])**2
    # return 9 - 25*x[0] + x[0]**2 - 22*x[1] + x[1]**2

def calc(x0, a):
    '''
        x0 - початкові точки
        а - масштабний множник
    '''
    prettyTable = PrettyTable()
    prettyTable.field_names = ["№", "xk", "f'(xk)"]
    # prettyTable.add_row([k, xk, fs])
    # print(prettyTable)


    N = len(x0)
    M = round(1.65 * N + 0.05 * N**2)
    p1 = ((sqrt(N+1) + N - 1) / (N * sqrt(2))) * a # приріст
    p2 = ((sqrt(N+1) - 1) / (N * sqrt(2))) * a # приріст

    x1 = np.array([x0[0] + p2, x0[1] + p1]).T
    x2 = np.array([x0[0] + p1, x0[1] + p2]).T
    y0 = f(x0)
    y1 = f(x1)
    y2 = f(x2)

    # Накриття» точки мінімуму
    if y0 > y1 and y0 > y2:
        xc = (1/N) * (x1 + x2)
    x3 = x1 + x2 - x0
    y3 = f(x3)
    print(y0, y1, y2, y3)
    print(x0, x1, x2, x3)
    draw_plot(np.array([x1, x2, x3, xc, x0]))

if __name__ == '__main__':
    x0, a = np.array([0, 0]).T, 2
    # x0, a = [0, 1], 2
    result = calc(x0, a)
    print(result)