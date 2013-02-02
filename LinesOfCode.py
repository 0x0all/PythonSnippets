'''
Go into the root directory you want to check and run this.

Removes c files, build directories, profiling and storage file types.

Adapted from https://gist.github.com/1228095 
'''

import sys, os


def file_len(fname):
	i = -1
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i+1

def count(fname):
	_count = 0
	dirList = os.listdir(fname)
	for d in dirList:
	    if os.path.isdir(fname+"/"+d) == True:
			_count += count(str(fname+"/"+d))
	    elif fname[-5:]!='build' and d[-1]!='c' and d[-3:]!='xml' and d[-3:]!='png'\
	    and d[-5:]!='Store' and d[-1]!='~' and d[-7:]!='profile' and d[-3:]!='txt'\
	    and fname.find('_Dijkstras')< 0 and d[-3:]!='npz' and d[-3:]!='npy'\
	     and d[-3:]!='pkl' and d[-3:]!='csv' and d.find('__')< 0\
	     and d.find('dijkProfile')< 0:
   			filelen = file_len(fname+"/"+d)
   			print "%s: %d" % (fname+"/"+d, filelen)
   			all_files.append((fname+"/"+d, filelen))
   			_count += filelen
	return _count

all_files = []
count('.')
inds = argsort([x[1] for x in all_files])

sum = 0
for i in inds:
	sum += all_files[i][1]
	print sum, all_files[i][1], all_files[i][0]