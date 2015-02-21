import sys
from country import *
from PyQt4 import QtGui, QtCore


class UserInterface(QWidget):
	def __init__(self):
		super(UserInterface, self).__init__()
		self.initUI()
		
	def initUI(self):
		countrylist = readcountry()
		
		self.setGeometry(300,300,280,170)
		self.setWindowTitle('Landen met vlag')
		self.show()
		
		self.dropdown = QComboBox(self)
		for item in countrylist:
			self.dropdown.addItem(item.getName())
		self.dropdown.setGeometry(20,10,240,30)
		self.dropdown.show()
		
		self.dropdown.currentIndexChanged.connect(self.updateUi)
		
		self.bier = QFrame(self)
		self.bier.setGeometry(20,50,240,100)
		self.bier.show()
		
	def updateUi(self):
		countrylist = readcountry()
		nummer = self.dropdown.currentIndex()
		index = countrylist[nummer]
		schermkleur = index.getKleuren()
		self.bier.setStyleSheet("QFrame { background-color: %s }" % schermkleur.name())

def main():
	app = QtGui.QApplication(sys.argv)
	userinterface = UserInterface()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
