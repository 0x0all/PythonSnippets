import numpy as np
import visvis as vv
from IPython import embed

# import scipy.misc as sm
im = vv.imread('/Users/colin/Desktop/hog.png')

# win = vv.imshow(im)
# vv.processEvents()

import time

class VideoViewer:

	open_windows = []

	def __init__(self):
		pass

	def getWindow(self, name):
		names = [x['name'] for x in self.open_windows]
		try:
			index = names.index(name)
			return self.open_windows[index]
		except:
			return None

	def getWindowFromFigure(self, figure):
		figs = [x['figure'] for x in self.open_windows]
		try:
			index = figs.index(figure)
			return self.open_windows[index]
		except:
			return None			

	def keyHandler(self, event):
		# embed()
		win = self.getWindowFromFigure(event.owner)
		win['keyEvent'] = event.key
		print event.text, event.key
		
	def createWindow(self, name, im, axis):

		vv.figure()
		vv.gca()
		vv.clf()
		fig = vv.imshow(im)
		dims = im.shape

		''' Change color bounds '''
		if im.dtype == np.uint8:
			fig.clim.Set(0, 255)
		else:
			fig.clim.Set(im.min(), im.max())
		
		fig.GetFigure().title = name
		
		''' Show ticks on axes? '''

		if not axis:
			fig.GetAxes().axis.visible = False
			bgcolor = (0.,0.,0.)
		else:
			fig.GetAxes().axis.showBox = False
			bgcolor = (1.,1.,1.)

		fig.GetFigure().bgcolor = bgcolor
		fig.GetAxes().bgcolor = bgcolor



		fig.eventKeyUp.Bind(self.keyHandler)

		win = {'name':name, 'figure':fig, 'shape':dims, 'keyEvent':None}
		self.open_windows.append(win)

		return win


	def destroyWindow(self, name):
		win = self.getWindow(name)
		
		if win is not None:
			win['figure'].Destroy()
		else:
			print "No window found"

		vv.update()

	def imshow(self, name, im, axis=False):
		'''
		Inputs
			name: string with figure name
			im: numpy array
		'''

		win = self.getWindow(name)
		
		if win is None:
			win = self.createWindow(name, im, axis)
		else:	
			''' If new image is of different dimensions we must create new image'''
			if im.shape != win['shape']:
				self.destroyWindow(win['name'])
				win = self.createWindow(name, im)

		win['figure'].SetData(im)
		vv.processEvents()

	
	def update(self):
		''' Does not capture key inputs '''
		vv.processEvents()

	def waitAndUpdate(self, duration=0):
		'''
		Input:
			Duration (in milliseconds)
			If negative it will wait until a key is pressed
		'''
		# vv.clf()
		# time.sleep(.01)
		vv.processEvents()

		''' Reset key events '''
		for i in self.open_windows:
			i['keyEvent'] = None

		''' If negative duration then have infinite loop '''
		if duration < 0:
			duration = np.inf

		start_time = time.time()
		while(time.time()-start_time < duration/1000.):
			vv.processEvents()
			time.sleep(.0001)

			keys = [x['keyEvent'] for x in self.open_windows if x['keyEvent'] is not None]
			if len(keys) > 0:
				return keys[0]

		for i in self.open_windows:
			i['keyEvent'] = None

		return 0



w = VideoViewer()
w.imshow("Hi", np.eye(100, dtype=np.uint8), axis=True)
w.imshow("im", im, axis=False)

for j in range(100):
	key = w.waitAndUpdate(1000)
	w.imshow("im", im+j*5, axis=False)
	print key
	


