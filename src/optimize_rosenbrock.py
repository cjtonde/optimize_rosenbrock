import numpy as np
from scipy.optimize import minimize

def rosen(x):
	"""
		The Rosenbrock's function of N variables
		f(x) =  100*(x_i - x_{i-1}^2)^2 + (1- x_{1-1}^2)
	"""
	return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)


def rosen_der(x):
	"""
		Gradient of the Rosenbrock function of for gradient descent.
	"""
	xm = x[1:-1]
	xm_m1 = x[:-2]
	xm_p1 = x[2:]
	der = np.zeros_like(x)
	der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
	der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
	der[-1] = 200*(x[-1]-x[-2]**2)
	return der

def rosen_hess(x):
	"""
		Hessian of the Rosenbrock's function.
	"""
	x = np.asarray(x)
	H = np.diag(-400*x[:-1],1) - np.diag(400*x[:-1],-1)
	diagonal = np.zeros_like(x)
	diagonal[0] = 1200*x[0]**2-400*x[1]+2
	diagonal[-1] = 200
	diagonal[1:-1] = 202 + 1200*x[1:-1]**2 - 400*x[2:]	
	H = H + np.diag(diagonal)
	return H

def main():
	# initial starting point 
	x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
	print("Initial Start point %f")
	print(x0)
	# minimize function
	res = minimize(rosen, x0, method='Newton-CG',
		jac=rosen_der, hess=rosen_hess,
		options={'xtol': 1e-8, 'disp': True})
	print("Solution: ")
	print(res.x)
 
if __name__ == '__main__':
    main() 
