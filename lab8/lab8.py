from prettytable import PrettyTable
from sympy import diff, symbols, sin, atan, exp, log, ln, pi

def f(x):
	# return x*atan(x)-0.5*ln(1+pow(x, 2))
    # return sin(x)
    # return exp(2-x)+x*atan(x)-0.5*ln(1+pow(x, 2))
    return 1.5*pow((x+1.5), 2)*(x-1.1)*(x-0.75)

def f_():
	x = symbols('x')
	return diff(f(x))

def f__():
	return diff(f_())

def calc(x0, p, sig):
	prettyTable = PrettyTable()
	prettyTable.field_names = ["k", "xk", "a", "f(xk)", "f'(xk)", "f''(xk)", "sx", "f(sx)", "f'(sx)"]

	# step 1
	k = 0
	xk = x0
	# step 2
	fs = f_().subs('x', xk)
	fss = f__().subs('x', xk)

	if abs(fs) <= sig:
		return x0
	else:
		f_xk, sx, f_sx, f_sx_ = '', '', '', ''
		# step 3
		a = 1
		while True:
			prettyTable.add_row([k, xk, a, f_xk, fs, fss, sx, f_sx, f_sx_])
			# print(k, a)
			# step 4
			sx = xk - a * fs / fss
			# step 5
			f_sx_ = f_().subs('x', sx)
			if abs(f_sx_) <= sig:
				prettyTable.add_row([k, xk, a, f_xk, fs, fss, sx, f_sx, f_sx_])
				print(prettyTable)
				return sx
			# step 6
			f_sx = f(sx)
			f_xk = f(xk)
			# step 7
			if f_sx - f_xk <= -p*a*pow(fs, 2) / fss:
				k += 1
				xk = sx # тута сразу положити xk = xk + 1
				# step 8
				if abs(f_sx_) <= sig:
					prettyTable.add_row([k, xk, a, f_xk, fs, fss, sx, f_sx, f_sx_])
					print(prettyTable)
					return xk
				# step 9
				elif a <= sig:
					prettyTable.add_row([k, xk, a, f_xk, fs, fss, sx, f_sx, f_sx_])
					print(prettyTable)
					return xk
				# step 11, 12
				else:
					fs = f_().subs('x', xk)
					fss = f__().subs('x', xk)
					# do step 3 here and go to step 4
					a = 1
			# step 10
			else:
				a /= 2
				# go to step 4

if __name__ == '__main__':
    # x0, p, sig = -1.6, 0.5, 0.01
    # x0, p, sig = 4.094, 0.5, 0.01
    # x0, p, sig = 0.9, 0.5, 0.01
    x0, p, sig = -1.55, 0.5, 0.01
    result = calc(x0, p, sig)
    print(result)