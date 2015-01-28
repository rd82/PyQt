#!/usr/bin/python 

import sys
from PyQt4 import  QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example,self).__init__()

		self.initUI()

	def initUI(self):
		qBtn = QtGui.QPushButton('Quit',self)
		qBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		qBtn.resize(qBtn.sizeHint())
		qBtn.move(50,50)

		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Quit Button')
		
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)

	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

