from PyQt5 import QtCore, QtGui, QtWidgets
import halamanDepan

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = halamanDepan.halamanDepan()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())