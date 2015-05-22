.. -*- mode: rst -*-

optimize_rosenbrock
============

A simple python code for minimize the Rosenbrock function. 

The Rosenbrock's function of N variables,
	
	$$f(x) =  \sum_{i=1}^{N-1}100*(x_i - x_{i-1}^2)^2 + (1- x_{i-1}^2)$$


Dependencies
============

The code is tested to work under Python 3.4. 

The required dependencies to build the software are NumPy >= 1.6.2,
SciPy >= 0.9 and a working C/C++ compiler.

Running
=======

To run just use::

  python ./src/optmize_rosenbrock.py


