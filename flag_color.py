import sys
from random import randrange
from PyQt4.QtGui import *

class FlagColor(QColor):
	def __init__(self):
		super(FlagColor,self).__init__()
	
	def SetColor(self):
		red=randrange(1,255)
		green=randrange(1,255)
		blue=randrange(1,255)
		setred=self.setRed(red)
		setgreen=self.setGreen(green)
		setblue=self.setBlue(blue)
		
	
