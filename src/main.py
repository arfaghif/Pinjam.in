from PyQt5 import QtCore, QtGui, QtWidgets
import halamanDepan
import DB
if __name__ == "__main__":
    import sys
    database=DB.DB("password","rpl")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = halamanDepan.halamanDepan()
    ui.setupUi(MainWindow,database)
    MainWindow.show()
    sys.exit(app.exec_())
