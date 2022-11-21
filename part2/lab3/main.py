from prettytable import PrettyTable
import numpy as np
from numpy import linalg
from sympy import symbols, diff, Function

def f(x):
    # return np.power(x[0], 2) + np.power(x[1], 2)
    # return 4 * (x[0] - 5)**2 + (x[1] - 6)**2
    return 9 - 25*x[0] + np.power(x[0], 2) - 22*x[1] + np.power(x[1], 2)

def calc(x, alpha, beta, eps):

	prettyTable = PrettyTable()
	prettyTable.field_names = ["№", "x", "f_x", "dx", "dx2", "g", "H", "s", 'alpha', 'beta']

	len_x = len(x) # кол-во переменных
	E = np.diag(np.ones(len_x)) # создаем единичную матрицу
	print('E:', E)

# step 1
	f_x = f(x)

	_iter = 0
	prettyTable.add_row([_iter, x, f_x, '', '', '', '', '', alpha, beta])

	# ебашим массив с переменными (x1, x2 ...) в str формате
	mx = np.array(symbols([f'x{i+1}' for i in range(len_x)]))

	step = 2

	while step != -1:
# step 2
		_iter += 1
		'''
		Сделаем словарь где сопоставим названия переменных и их значения
		{
			x1: 10.0,
			x2: 10.0,
			...
			...
		}

		mx - наши ключи
		x - значения
		dx - производные
		'''
		if step == 2:
			dic = {}
			for key, value in zip(mx, x):
				dic[key] = value
			print("Dictionary:", dic)

			# находим частные производные
			dx = np.array([diff(f(mx), mx[i]) for i in range(len_x)])
			print("dx:", dx)
			# подставим иксы и получим наше бля
			g = np.array([f_.subs(dic) for f_ in dx], dtype="float")
			print("g:", g)

			# берем вторую производную
			dx2 = np.zeros([len(dx), len(dx)], dtype="float") # заполняем матрицы 0
			H = np.copy(dx2)
			for i, f_ in enumerate(dx): # берем первую производную из списка
				for j in range(len(dx)): # берем вторую производную
					dx2[i][j] = diff(f_, mx[j])
					if not isinstance(dx2[i][j], np.float64):
						H[i][j] = Function(str(dx2[i][j]))(dic)
					else:
						H[i][j] = dx2[i][j]
			print("dx2:", dx2)
			print("H:", H)
			step = 3
# step 3
		if step == 3:
			s = linalg.inv(H + alpha * E).dot(-g.T)
			print(s)

		prettyTable.add_row([_iter, x, f_x, dx, dx2, g, H, s, alpha, beta])
# step 4
		y = x.T + s.T
		f_y = f(y)
		print(y, f_y)
# step 5
		if f_y >= f_x:
			alpha = alpha / beta
			step = 3
			print("Ебашим на шаг 3")
			continue
# step 6
		x = y
		f_x = f_y
		alpha = alpha * beta
# step 7
		# если хотя бы один больше погрешность то ебашим на 2
		if (np.absolute(s) > eps).any():
			step = 2
			print("Ебашим на шаг 2")
			continue
		else:
			step = -1

	print(prettyTable)

	return x, f_x

if __name__ == '__main__':
	x0, alpha, beta, eps = np.array([10, 10], dtype="float"), 100, 0.5, 10e-3
	x, f_x = calc(x0, alpha, beta, eps)
	print('Min:', x, f_x)