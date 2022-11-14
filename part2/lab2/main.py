from prettytable import PrettyTable
import numpy as np
from numpy import power

def f(x):
    # return power(x[0], 2) + power(x[1], 2)
    # return 8*power(x[0], 2) + 4*x[0]*x[1] + 5*power(x[1], 2)
    return 4 * (x[0] - 5)**2 + (x[1] - 6)**2
    # return 9 - 25*x[0] + power(x[0], 2) - 22*x[1] + power(x[1], 2)

def isStop(dx, eps):
	return 1 if abs(dx[0]) < eps else 0
	# return np.prod([1 if abs(dxi) < eps else 0 for dxi in dx])

def research(x, f_x, dx, a, eps, n):
	for i in range(n):
		tmp_x1 = np.array(x, copy=True, dtype='f')
		tmp_x1[i] += dx[i]
		print(tmp_x1)
		tmp_f1 = f(tmp_x1)
		if tmp_f1 < f_x:
			x[i] = tmp_x1[i]
			print('Успіх', f'x[{i}] = {x[i]}')
		else:
			tmp_x2 = np.array(x, copy=True, dtype='f')
			tmp_x2[i] -= dx[i]
			tmp_f2 = f(tmp_x2)
			if tmp_f2 < f_x:
				x[i] = tmp_x2[i]
				print('Успіх', f'x[{i}] = {x[i]}')
			else:
				print('Не Успіх', f'x[{i}] = {x[i]}')
	return x, f(x)

def calc(x0, dx, a, eps):
	'''
	    x0 - початкова точка
	'''
	prettyTable = PrettyTable()
	prettyTable.field_names = ["№", "x", "f_x", "dx", "eps"]

	n = len(x0)

	x = x0
	f_x = f(x)

	step = 2
	_iter = -1

	# step 2
	while True:
		_iter += 1
		prettyTable.add_row([_iter, x, f_x, dx, eps])
		if step == 2:
			print('step 2')
			tmp_x, tmp_f_x = research(x, f_x, dx, a, eps, n)
			# step 3
			print('step 3')
			if tmp_f_x < f_x:
				x_prev = np.array(x, copy=True, dtype='f')
				f_prev = f_x
				x = np.array(tmp_x, copy=True, dtype='f')
				f_x = tmp_f_x
				step = 5
			else:
				# step 4
				if isStop(dx, eps):
					print(prettyTable)
					return x, f_x # we've found min
				else:
					dx = dx / a
					step = 2
					continue
		# step 5
		if step == 5:
			print('step 5')
			X = x + (x - x_prev)
			f_X = f(X)
		# step 6
		print('step 6')
		tmp_X, tmp_f_X = research(X, f_X, dx, a, eps, n)
		print(tmp_X, tmp_f_X)
		# step 7
		print('step 7')
		if tmp_f_X < f_x:
			x_prev = np.array(x, copy=True, dtype='f')
			f_prev = f_x
			x = np.array(tmp_X, copy=True, dtype='f')
			f_x = tmp_f_X
			step = 5
		else:
			step = 2

if __name__ == '__main__':
	# x0, dx, a, eps = np.array([1, 1], dtype='f'), np.array([-1, 1], dtype='f'), 2, 10e-4
	# x0, dx, a, eps = np.array([-4, -4], dtype='f'), np.array([-1, 1], dtype='f'), 2, 10e-4
	x0, dx, a, eps = np.array([8, 9], dtype='f'), np.array([-1, 1], dtype='f'), 2, 10e-4
	# x0, dx, a, eps = np.array([0, 1], dtype='f'), np.array([-1, 1], dtype='f'), 2, 10e-4
	x, f_x = calc(x0, dx, a, eps)
	print('Min:', x, f_x)