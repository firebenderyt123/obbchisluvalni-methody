import math

def f(x):
	return pow(x, 2)
	# return 2 * pow(x, 2) - 4 * x + 16 / x
	# return math.exp(2-x)+x*math.atan(x)-0.5*math.log10(1+pow(x, 2))

if __name__ == '__main__':
	x0 = float(input('Input x0: '))
	delta = float(input("Input delta: "))

	k = 0
	p = 0

	Xk = x0
	Xk_1 = Xk + delta

	u = f(Xk)
	v = f(Xk_1)

	a, b = 0, 0

	while True:
		if v < u:
			while v < u:
				k += 1
				Xk = Xk_1
				Xk_1 = Xk + pow(2, k)*delta
				u = v
				v = f(Xk_1)
				print(k, Xk, u)
			a = Xk - delta
			b = Xk_1
			break
		else:
			if p == 0:
				delta = -delta
				p = 1
			else:
				a = x0 + delta
				b = x0 - delta
				break

	print(a, b)