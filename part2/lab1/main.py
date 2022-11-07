from prettytable import PrettyTable
import numpy as np
from numpy import sqrt, power
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def draw_plot(x):
    ax.cla()
    ax.scatter(x[:, 0], x[:, 1], s = 1)
    t1 = plt.Polygon(x[:3,:])
    plt.gca().add_patch(t1)
    ax.axis([-20, 100, -5, 60])
    plt.pause(0.05)

def f(x):
    return power(x[0], 2) + power(x[1], 2)
    # return power(1-x[0], 2) + power(2-x[1], 2)
    # return 9 - 25*x[0] + power(x[0], 2) - 22*x[1] + power(x[1], 2)
    # return power(x[0], 2) + power(x[1], 2) + power(x[2], 2) + power(x[3], 2)

def custom_sort(list_x, list_y):
    '''
    return max, after_max, min values for x and f(x)
    '''
    max_index = None
    after_max_index = None
    min_index = None
    max_val= float('-inf')
    after_max_val = float('-inf')
    min_val = float('inf')
    for i, y in enumerate(list_y):
        if y > max_val:
            after_max_val = max_val
            after_max_index = max_index
            max_index = i
            max_val = y
        elif y > after_max_val:
            after_max_val = y
            after_max_index = i
        if y < min_val:
            min_index = i
            min_val = y
    res_x = list_x[[max_index, after_max_index, min_index]]
    res_y = list_y[[max_index, after_max_index, min_index]]
    return res_x, res_y

def build_simplex(x0, N, p1, p2):
    list_x = np.zeros((N+1, N))
    list_x[0] = x0
    for i in range(N):
        tmp_x = np.zeros(N)
        for j in range(N):
            if j != i:
                tmp_x[j] = x0[j] + p1
            else:
                tmp_x[j] = x0[j] + p2
        list_x[i+1] = tmp_x
    list_y = f(list_x.T)
    return list_x, list_y

def compression(list_x, list_y, xc):
    '''
    return list_x, list_y, xs, ys
    '''
    xs = 0.5 * list_x[0] + 0.5 * xc
    ys = f(xs)
    if ys < list_y[0]:
        list_x[0] = xs
        list_y[0] = ys
    elif ys > list_y[0]:
        for i in range(2):
            list_x[i] = list_x[2] + (list_x[i] - list_x[2]) / 2
        list_y = f(list_x.T)
    return list_x, list_y, xs, ys

def calc(x0, a, sig):
    '''
        x0 - початкові точки
        а - масштабний множник
        sig - допустиме квадратичне відхилення
    '''
    prettyTable = PrettyTable()
    prettyTable.field_names = ["№", "x1", "x2", "x3", "y1", "y2", "y3", "D"]

    # Підготовка
    N = len(x0)
    M = round(1.65 * N + 0.05 * power(N, 2))
    p1 = ((sqrt(N+1) + N - 1) / (N * sqrt(2))) * a # приріст
    p2 = ((sqrt(N+1) - 1) / (N * sqrt(2))) * a # приріст

    list_x, list_y = build_simplex(x0, N, p1, p2)
    # print("List X:", list_x)
    # print("List Y:", list_y)

    # Сортування
    yr = None
    _iter = 0
    D = float('inf')
    not_changed = np.zeros(N+1) # кол-во неизменчивости каждой точки
    while D >= sig:
        prev_y = list_y
        list_x, list_y = custom_sort(list_x, list_y)
        # print('\n', list_x, list_y)

        if yr == list_y[0]:
            print('«Накрытие» точки минимума')
            list_x, list_y = build_simplex(list_x[1], N, p1, p2)
            list_x, list_y = custom_sort(list_x, list_y)
            prev_y = list_y

        prettyTable.add_row([
            _iter,
            list_x[0], list_x[1], list_x[2],
            list_y[0], list_y[1], list_y[2],
            D
        ])

        xc = 1/N * np.sum(list_x[1:], axis=0)
        xr = 2 * xc - list_x[0]
        yr = f(xr)
        if yr < list_y[2]:
            xe = -1 * xc + 2 * xr
            ye = f(xe)
            if ye < yr:
                list_x[0] = xe
                list_y[0] = ye
            elif yr < ye:
                list_x[0] = xr
                list_y[0] = yr
        elif list_y[2] < yr and yr < list_y[1]:
            list_x[0] = xr
            list_y[0] = yr
        elif list_y[1] < yr and yr < list_y[0]:
            xr, list_x[0], yr, list_y[0] = list_x[0], xr, list_y[0], yr
            list_x, list_y, xs, ys = compression(list_x, list_y, xc)
        elif list_y[0] < yr:
            list_x, list_y, xs, ys = compression(list_x, list_y, xc)

        for i, y in enumerate(prev_y):
            if y == prev_y[i]:
                not_changed[i] += 1
                if not_changed[i] > M:
                    print("Циклическое движение")
                    for i in range(2):
                        list_x[i] = list_x[2] + (list_x[i] - list_x[2]) / 2
                    list_y = f(list_x.T)
                    not_changed = np.zeros(N+1)
                    break
            else:
                not_changed[i] = 0

        # f_line = np.sum(list_y / (N+1))
        # D = np.sum(power(list_y - f_line, 2) / (N+1))
        D = np.var(list_y) # дисперсия

        draw_plot(np.array(list_x))

        print(_iter, list_y, D)
        # print("List X:", list_x)
        # print("List Y:", list_y)

        _iter += 1

    list_x, list_y = custom_sort(list_x, list_y)
    prettyTable.add_row([
        _iter,
        list_x[0], list_x[1], list_x[2],
        list_y[0], list_y[1], list_y[2],
        D
    ])
    print(prettyTable)

    return list_x[2], list_y[2], D

if __name__ == '__main__':
    x0, a, sig = np.array([100, 100]), 2, 1e-16
    # x0, a, sig = np.array([0, 0]), 2, 1e-16
    # x0, a, sig = np.array([0, 1]), 2, 1e-16
    # x0, a, sig = np.array([100, 50, 50, 10]), 2, 1e-16
    result = calc(x0, a, sig)
    print(result)