import sys
from PyQt4 import QtGui

class example(QtGui.QMainWindow):
	"""docstring for example"""
	def __init__(self):
		super(example, self).__init__()
		self.setWindowTitle('TreeView tester')

def main():
	app = QtGui.QApplication(sys.argv)
	ex = example()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()
		