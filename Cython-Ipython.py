
'''
Compares speed of cython versus python. Run this in IPython.

Does gibbs sampling for equation f(x,y) = x x^2 \exp(-xy^2 - y^2 + 2y - 4x)

with conditional distributions:

x|y ~ Gamma(3, y^2 +4)
y|x ~ Normal( 1/(1+x), 1/(2(1+x)) )


Takes ~1.25 seconds with cython and around a minute with python
'''



''' Cython version '''
%load_ext cythonmagic

%%cython -lgsl -lgslcblas
import numpy as np

%%cython
cimport cython
from cython_gsl cimport *#gsl_ran_gamma, gsl_ran_gaussian
from libc.math cimport sqrt
import numpy as np
cimport numpy as np
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def gibbs(int N=20000, int thin=500):
	cdef:
		double x = 0
		double y = 0
		gsl_rng *r = gsl_rng_alloc(gsl_rng_mt19937)
		Py_ssize_t i,j
		np.ndarray[np.float64_t, ndim=2] samples = np.empty((N,2), dtype=np.float64)

	for i in range(N):
		for j in range(thin):
			# r = random.rand()
			x = gsl_ran_gamma(r, 3, 1.0/(y*y+4))
			y = gsl_ran_gaussian(r,1.0/sqrt(x+1))
		samples[i,0] = x
		samples[i,1] = y
	return samples

p = gibbs()

plt.hexbin(posterior[:, 0], posterior[:, 1])


''' Raw version '''

import random, math

def gibbs_python(N=20000, thin=500):
	x = 0
	y = 0
	samples = np.empty([N,2])

	for i in range(N):
		for j in range(thin):
			x = random.gammavariate(3, 1.0/(y*y+4))
			y = random.gauss(1.0/(x+1), 1.0/math.sqrt(x+1))
			samples[i] = [x,y]
	return samples




