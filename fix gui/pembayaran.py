# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pembayaran.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import register
import login
import ulasan
import DB
import pencarian
import registerKendaraan
class pembayaran(object):
    def openWindowLogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = login.login()
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.close()
    def openWindowRegister(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = register.register()
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.close()
    def openWindowUlasan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ulasan.ulasan()
        self.ui.setupUi(self.window,self.username)
        self.window.show()
        self.MainWindow.close()
    def openWindowPencarian(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pencarian.pencarian()
        self.ui.setupUi(self.window,self.username)
        self.window.show()
        self.MainWindow.close()
    def openWindowRegisterKendaraan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = registerKendaraan.registerKendaraan()
        self.ui.setupUi(self.window,self.username)
        self.window.show()
        self.MainWindow.close()
    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def pushUlasan(self):
        self.database=DB.DB("Password0","rpl")
        id_transaksi = int(self.lineEdit.text())
        nominal = self.lineEdit_2.text()
        result=[]
        self.database.getData("select IDTransaksi,nominal from transaksi where IDTransaksi LIKE {}".format(id_transaksi),result)
        if(result!=[]):
            self.database.navigateDatabase("UPDATE transaksi SET konfirmasi=1 WHERE IDTransaksi={}".format(id_transaksi))
            self.database.navigateDatabase("UPDATE transaksi SET status='DITERIMA' WHERE IDTransaksi={}".format(id_transaksi))
            self.messageBox("Pembayaran verified","Pembayaran sudah terkonfirmasi!")
            self.openWindowUlasan()
        else:
            self.messageBox("Pembayaran verified","Data yang anda masukan salah!")
    def pushLogin(self):
        self.openWindowLogin()
    def pushSignUp(self):
        self.openWindowRegister()
    def setupUi(self, MainWindow, username):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 789, 244))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(558, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_3.clicked.connect(self.pushLogin)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.pushButton.clicked.connect(self.pushSignUp)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem2, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_4.clicked.connect(self.pushUlasan)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.splitter_2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Segoe UI Semilight")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(40, 510, 211, 51))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.clicked.connect(self.openWindowPencarian)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(310, 510, 221, 51))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.clicked.connect(self.openWindowRegisterKendaraan)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(560, 510, 221, 51))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.clicked.connect(self.openWindowUlasan)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow=MainWindow
        self.username=username
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "Signed in as User"))
        self.label.setText(_translate("MainWindow", "Pinjam.in"))
        self.label_2.setText(_translate("MainWindow", " Bayar Kuy!"))
        self.pushButton_4.setText(_translate("MainWindow", "Bayar"))
        self.lineEdit_2.setText(_translate("MainWindow", "Masukkan Nominal"))
        self.lineEdit.setText(_translate("MainWindow", "Masukkan ID Transaksi"))
        self.commandLinkButton.setText(_translate("MainWindow", "pencarian"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "registrasi kendaraan"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "ulasan"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = pembayaran()
    ui.setupUi(MainWindow,"aaaa")
    MainWindow.show()
    sys.exit(app.exec_())
