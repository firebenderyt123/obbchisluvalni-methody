import math
from prettytable import PrettyTable

def f(x):
	# return 2*x**2 - 4*x + 16 / x
	# return math.sin(x)
	return math.exp(2-x)+x*math.atan(x)-0.5*math.log10(1+pow(x, 2))

def calc(a, b, eps, R):
	prettyTable = PrettyTable()
	prettyTable.field_names = ["i", "x1", "x2", "f(x1)", "f(x2)", "a", "b", "L"]

	i = 0
	L  = b - a
	x2 = a + R*L
	x1 = a + b - x2
	f1 = f(x1)
	f2 = f(x2)

	prettyTable.add_row([0, "", "", "", "", a, b, L])

	while L > eps:
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
			L = b - a
			i += 1
			prettyTable.add_row([i, x1, x2, f1, f2, a, b, L])
		except Exception as e:
			print("Error:", e)
			print(prettyTable)
			return

	x=(a+b)/2
	print(prettyTable)
	print('Result:', x, f(x))

if __name__ == '__main__':
	R = (5 ** 0.5 - 1) / 2
	# a, b, eps = 1.5, 2.4, 0.1
	# a, b, eps = -3*math.pi, math.pi, 0.1
	# a, b, eps = 0.9, 2.9, 1e-3
	calc(a, b, eps, R)