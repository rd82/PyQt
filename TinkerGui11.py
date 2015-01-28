#!/usr/bin/python 

import sys
from PyQt4 import  QtGui

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example,self).__init__()

		self.initUI()

	def initUI(self):
		okButton = QtGui.QPushButton('OK')
		cancelButton = QtGui.QPushButton('Cancel')

		hBox = QtGui.QHBoxLayout()
		hBox.addStretch(1)
		hBox.addWidget(okButton)
		hBox.addWidget(cancelButton)

		vBox = QtGui.QVBoxLayout()
		vBox.addStretch(1)
		vBox.addLayout(hBox)

		self.setLayout(vBox)

		self.setGeometry(300,300,300,150)
		self.setWindowTitle('Buttons')
		self.show()


def main():
	app = QtGui.QApplication(sys.argv)

	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

