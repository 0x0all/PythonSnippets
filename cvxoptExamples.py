''' Example programs for cvxopt
Adapted from cvxopt tutorials: http://abel.ee.ucla.edu/cvxopt/examples/tutorial/qp.html
 '''

''' Quadratic program '''
'''
Find solution to: min 2*x1^2 + x2^2 + x1*x2 + x1 + x2
				s.t. x1 >= 0, x2 >= 0, x1+x2 = 1

qp doc: http://abel.ee.ucla.edu/cvxopt/userguide/coneprog.html#quadratic-programming
'''


from cvxopt import matrix, solvers

# quadradic min terms: (??)
Q = 2*matrix([[2, .5],  #2x1^2 + x1
			  [.5, 1]]) #x2^2 + x2
# linear min terms
p = matrix([1.,1.])

# x1 >= 0, x2 >= 0
G = matrix([[-1., 0.],
			[ 0.,-1.]])
h = matrix([0.,0.])

# x1 + x2 = 1
A = matrix([1.,1.], (1,2))
b = matrix(1.)

sol = solvers.qp(Q,p,G,h,A,b)

''' Linear program 

min 2*x1 + x2
s.t. -x1 + x2 <= 1
	x1+x2 >= 2
	x2 >= 0
	x1 - 2*x2 <= 4
'''

c = matrix([2.,1.]) # Min 2*x1 + x2
A = matrix( [-1., -1.,  0.,  1.], # x1 +
			[ 1., -1., -1., -2.]) # x2
B = matrix( [ 1., -2.,  0.,  4.]) # <= this

