import sys
from country import *
from PyQt4 import QtGui, QtCore


class UserInterface(QWidget):
	def __init__(self):
		super(UserInterface, self).__init__()
		self.initUI()
		
	def initUI(self):
		self.countrylist = readcountry()
		
		self.setGeometry(300,300,280,170)
		self.setWindowTitle('Landen met vlag')
		self.show()
		
		self.dropdown = QComboBox(self)
		for item in self.countrylist:
			self.dropdown.addItem(item.getName())
		self.dropdown.setGeometry(20,10,240,30)
		self.dropdown.show()
		
		self.dropdown.currentIndexChanged.connect(self.updateUi)
		
		self.frame = QFrame(self)
		self.frame.setGeometry(20,50,240,100)
		self.frame.show()
		
	def updateUi(self):
		nummer = self.dropdown.currentIndex()
		index = self.countrylist[nummer]
		schermkleur = index.getKleuren()
		self.frame.setStyleSheet("QFrame { background-color: %s }" % schermkleur.name())

def main():
	countrylist = readcountry()
	app = QtGui.QApplication(sys.argv)
	userinterface = UserInterface()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
