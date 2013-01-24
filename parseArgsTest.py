import optparse
parser = optparse.OptionParser(usage="Usage: python %prog [devID] [view toggle] [frameDifferencePercent]")
parser.add_option('-d', '--device', dest='devID', type='int', default=1, help='Device # (eg. 1,2,3)')
parser.add_option('-v', '--view', dest='viz', action="store_true", default=False, help='View video while recording')	
parser.add_option('-f', '--framediff', type='int', dest='frameDiffPercent', default=5, help='Frame Difference percent for dynamic framerate capture')
parser.add_option('-s', '--skel', action="store_true", dest='skel', default=False, help='Capture Skeleton')
parser.add_option('-a', '--anonomize', dest='anonomize', action="store_true", default=False, help='Turn on anonomization')
parser.add_option('-i', '--dir', dest='dir', default=DIR, help='Save directory')
(options, args) = parser.parse_args()

from IPython import embed
# embed()
print 'dev:', int(options.devID)
print 'v:', options.viz
print '%:', options.frameDiffPercent