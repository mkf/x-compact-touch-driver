import evdev
import os
from evdev import *
from Xlib import X, display
d = display.Display()
s = d.screen()
root = s.root

device = evdev.InputDevice('/dev/input/event7')
finger = "0"
x_coord = "0"
y_coord = "0"



for event in device.read_loop():
	if "code 53" in str(event):
		x_coord = str(event).split(" ")[8]
		#print("X variable: "+str(event).split(" ")[8])
	elif "code 54" in str(event): 
		y_coord = str(event).split(" " )[8]	
	root.warp_pointer(int(x_coord), int(y_coord))
#	ext.xtest.fake_input(d, X.ButtonPress,1)
#	ext.xtest.fake_input(d, X.ButtonRelease,1)
	d.sync()


