
from multiprocessing import Pool
import random
import numpy as np
import time
from __future__ import division
import time



def fcn(x):
	x = (x * x) // (2)
	time.sleep(2)
	return x



dataIn = range(2,10)


procs = 8
dataIn = []
for i in xrange(procs):
	dataIn.append(np.random.randint(0, 10, [1000,1000]))

pool = Pool(processes=procs)
results = pool.map_async(fcn, dataIn)
resultsOut = results.get(timeout=2.5)

