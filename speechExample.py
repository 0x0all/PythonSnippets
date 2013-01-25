
'''
Only works on a mac
'''

import sys
from Foundation import *
import AppKit

from datetime import datetime
import time

global trigger
global synth
trigger = 0

timeToRespond = 8

synth = AppKit.NSSpeechSynthesizer.alloc().initWithVoice_(None)
synth.startSpeakingString_("Did someone just observe the patient?")

class SRDelegate(NSObject):
        def speechRecognizer_didRecognizeCommand_(self,sender,cmd):
            print "speechRecognizer_didRecognizeCommand_", cmd
            if cmd == "Yes": 
            	print "YAYA"
            	global trigger
            	trigger = 1
            	# break
            	# CFRunLoopStop(sender)
            	# sys.exit()

# synth = AppKit.NSSpeechSynthesizer.alloc().initWithVoice_(None)
# synth.startSpeakingString_("hello")

recog = AppKit.NSSpeechRecognizer.alloc().init()
recog.setCommands_( [
        "Yes",
        "No"])

recog.setListensInForegroundOnly_(False)
# recog.setBlocksOtherRecognizers_(True)
d = SRDelegate.alloc().init()
recog.setDelegate_(d)

print "Listening..."
recog.startListening()
runLoop = NSRunLoop.currentRunLoop()

''' Get time offset '''
now = datetime.utcfromtimestamp(time.time()+timeToRespond)
string = unicode(now.strftime("%Y-%m-%dT%H:%M:%S +0000"))
now_NSDate = NSDate.dateWithString_(string)

# runLoop.runUntilDate_(now_NSDate)

t1 = time.time()
while (time.time()-t1 < timeToRespond) and not trigger:
	ret = runLoop.runBeforeDate_(now_NSDate)
	time.sleep(.1)


if trigger == 1:
	time.sleep(1)
	synth.startSpeakingString_("Thank you")
else:
	synth.startSpeakingString_("I didn't hear you.")
