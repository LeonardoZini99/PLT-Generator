from plt_w import plt_writer
import sys
from PyQt4 import QtGui, QtCore # importiamo i moduli necessari


class PLTWindow(QtGui.QMainWindow):
  	def __init__(self):
			self.check=False
			self.text_entered=False
			QtGui.QMainWindow.__init__(self) # da porre sempre all'inizio
			self.setWindowTitle('PLT Generator')

	  		self.button = QtGui.QPushButton('Generate')
			self.button2 = QtGui.QPushButton('Load')
			self.filechoise = QtGui.QFileDialog()
			self.filechoise.setFileMode(QtGui.QFileDialog.AnyFile)
			self.filechoise.setFilter("CSV file (*.csv)")
			cWidget = QtGui.QWidget(self)
			grid = QtGui.QGridLayout(cWidget)
			self.button.clicked.connect(self.load_csv)
			self.textBox=QtGui.QLineEdit()
			self.lbl = QtGui.QLabel('Nome del condominio: ')
			self.lbl2 = QtGui.QLabel('Numero Colonna:')
			self.clm=QtGui.QLineEdit()
			self.clm.textChanged.connect(self.column)
	   		grid.addWidget(self.button, 2,0,1,1)
			grid.addWidget(self.textBox,1,0,1,1)
			grid.addWidget(self.lbl,0,0,1,1)
			grid.addWidget(self.lbl2,0,1,1,1)
			grid.addWidget(self.clm,1,1,1,1)

			self.textBox.textChanged.connect(self.text_changed)
			cWidget.setLayout(grid)
			self.setCentralWidget(cWidget)


	def column(self,text):
		self.n_column=text
	

	def text_changed(self,text):
		self.test=text

	def load_csv(self):
	   	if self.filechoise.exec_():
	   		filename=self.filechoise.selectedFiles()
			plt_writer(filename[0],self.test,int(self.n_column))	###inserire 3 parametri

def run():
	plt_window = PLTWindow()
	plt_window.show()
	plt_window.exec_()

if __name__ == "__main__":
	cont=False
	app = QtGui.QApplication(sys.argv)
	main = MainWindow()
	main.show()
	app.exec_()