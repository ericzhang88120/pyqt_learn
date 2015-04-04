#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from learnui import Ui_MainWindow

class example(QtGui.QMainWindow):
	"""docstring for example"""
	def __init__(self, parent=None):
		super(example, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = example()
    MainWindow.show()
    sys.exit(app.exec_())
