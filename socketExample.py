''' For kinect, grab time when you start receiving data
'''

##---Server---##
from socket import *
import time
#Settings
host = ''
port = 29862
# port = 5001
addr = (host, port)
buffSize = 4096/2
timeout = .01

#Setup
server = socket(AF_INET, SOCK_STREAM)

server.bind((addr))
server.listen(5) # max 5 connections
server.settimeout(timeout)
# conn, connAddr = server.accept()

clients = []
clientAddresses = []
t1 = time.time()
while time.time() - t1 < 5:
	try:
		conn, connAddr = server.accept()
	except:
		pass
	finally:
		if connAddr not in clientAddresses:
			clients.append(conn)
			clientAddresses.append(connAddr)

# conn.send("Test")

imTypes = {'color':921600, 'depth':307200}
imSize = 99999
imsRaw = []
for i in xrange(len(clients)):
	data = ''
	time_ = time.time()
	imStarted = 0
	while len(data) < imSize and time.time()-time_ < timeout:
		# data_str = clients[i].recv(bufferSize)

		try:
			data_str = clients[i].recv(bufferSize)
		except:
			# print "Buffer is empty"
			pass
		finally:
			# Check for start of image
			imNew = 0
			for type_ in imTypes:
				if type_ in data_str:
					data = data_str[data_str.find(type_):]
					imSize = imTypes[type_]
					imType = type_
					imStarted = 1
					imNew = 1
					time_ = time.time()
					print "Found start of ", type_
			if imStarted == 1 and imNew == 0:
				data += data_str
				if data > imSize:
					data = data[:imSize]
				time_ = time.time()

	if imSize != 99999 and len(data) == imSize:
		if imType == 'depth':
			d = np.fromstring(str(data), dtype=np.uint8).reshape([480,640])
		else:
			d = np.fromstring(str(data), dtype=np.uint8).reshape([480,640, 3])
		imsRaw.append(d)
		print 'New image'
	






conn.close()



d.reshape([480, 640])

# imshow(data)

# data = server.recv(bufferSize)
# imshow(data)

# conn.close()

##---Client---##
from socket import *
#Settings
host = 'localhost'
# port = 5001
port = 29991
addr = (host, port)
bufferSize = 4096

#Setup
client = socket(AF_INET, SOCK_STREAM)
client.connect((addr))

if 0:
	im_str = "depth"
	im_str += im.tostring()
else:
	im_str = "color"
	im_str += im3.tostring()
imSize = sys.getsizeof(im_str)

i = 0
data = ''
while i < imSize+bufferSize:
	c = client.send(im_str[i:i+bufferSize])
	# print c
	data += im_str[i:i+bufferSize]
	i += bufferSize
print 'Done'

d = np.fromstring(data[5:], dtype=np.uint8).reshape([480,640])
# data_str = client.recv(bufferSize)

client.close()



#
import numpy as np
import scipy.misc as sm
import sys

im = sm.imread('depthImage.jpg')
im3 = np.dstack([im, im, im])
buffSize = sys.getsizeof(im)