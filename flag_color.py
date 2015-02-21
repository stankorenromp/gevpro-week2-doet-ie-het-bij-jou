import sys
from random import randrange
from PyQt4.QtGui import *

class FlagColor(QColor):
	def __init__(self):
		super(FlagColor,self).__init__()
		red = self.red
		green = self.green
		blue = self.blue
	
	def SetColor(self):
		redrand = randrange(1,255)
		greenrand = randrange(1,255)
		bluerand = randrange(1,255)
	
		return redrand,greenrand,bluerand
