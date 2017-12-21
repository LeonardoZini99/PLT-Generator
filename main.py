from PyQt4 import QtGui
import sys
import design1

class ExampleApp(QtGui.QMainWindow, design1.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()
