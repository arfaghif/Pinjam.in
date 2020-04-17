# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerKendaraan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import register 
import login 
import pencarian
import DB
import hargaTambahan
import pembayaran
import ulasan
class registerKendaraan(object):
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
    def openHargaTambahan(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = hargaTambahan.hargaTambahan()
        self.ui.setupUi(self.dialog,self.database,self.nama_kendaraan,self.tahun,self.alamat,self.harga,self.deskripsi, self.ada_supir,self.username)
        self.dialog.show()
        self.MainWindow.close()
    def openWindowPencarian(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pencarian.pencarian()
        self.ui.setupUi(self.window,self.username)
        self.window.show()
        self.MainWindow.close()
    def openWindowPembayaran(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pembayaran.pembayaran()
        self.ui.setupUi(self.window,self.username)
        self.window.show()
        self.MainWindow.close()
    def openWindowUlasan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ulasan.ulasan()
        self.ui.setupUi(self.window,self.username)
        self.window.show()
        self.MainWindow.close()
    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    
    def pushHargaTambahan(self):
        self.nama_kendaraan=self.lineEdit.text()
        self.tahun=self.lineEdit_2.text()
        self.alamat=self.lineEdit_3.text()
        self.harga=self.lineEdit_4.text()
        self.deskripsi=self.lineEdit_5.text()
        if(self.ada_supir=='n'):
            self.database.navigateDatabase("INSERT INTO kendaraan(username,namakendaraan,tahun,alamat,harga,deskripsi,tersediasupir,tambahan) VALUES ('{}','{}',{},'{}',{},'{}','{}',{}".format(self.username ,self.nama_kendaraan,self.tahun,self.alamat,self.harga,self.deskripsi,self.tersedia_supir,0))
            self.openWindowPencarian()
        else:
            self.openHargaTambahan()
    def pushLogin(self):
        self.openWindowLogin()
    def pushSignUp(self):
        self.openWindowRegister()
    def handleActivated(self, index):
        self.ada_supir=str(self.comboBox.itemText(index))
        if(self.ada_supir=="YA"):
            self.ada_supir='y'
        else:
            self.ada_supir='n'
    def setupUi(self, MainWindow,username):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 794, 299))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(558, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_3.clicked.connect(self.pushLogin)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.pushButton.clicked.connect(self.pushSignUp)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
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
        self.widget1 = QtWidgets.QWidget(self.splitter_2)
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.widget1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.splitter)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated.connect(self.handleActivated)
        self.gridLayout_2.addWidget(self.splitter, 5, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter_2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton_2, 7, 0, 1, 1)
        self.pushButton_2.clicked.connect(self.pushHargaTambahan)
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
        self.commandLinkButton_2.clicked.connect(self.openWindowPembayaran)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(560, 510, 221, 51))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.clicked.connect(self.openWindowUlasan)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow=MainWindow
        self.database=DB.DB("Password0","rpl")
        self.username=username
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pinjam.in"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "Signed in as User"))
        self.label_2.setText(_translate("MainWindow", "Mulai Menyewakan!"))
        self.lineEdit_4.setText(_translate("MainWindow", "harga"))
        self.lineEdit.setText(_translate("MainWindow", "nama kendaraan"))
        self.lineEdit_5.setText(_translate("MainWindow", "deskripsi"))
        self.lineEdit_2.setText(_translate("MainWindow", "tahun"))
        self.label_4.setText(_translate("MainWindow", "Tersedia supir?"))
        self.comboBox.setItemText(0, _translate("MainWindow", "YA"))
        self.comboBox.setItemText(1, _translate("MainWindow", "TIDAK"))
        self.lineEdit_3.setText(_translate("MainWindow", "alamat"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))
        self.commandLinkButton.setText(_translate("MainWindow", "pencarian"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "pembayaran"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "ulasan"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = registerKendaraan()
    ui.setupUi(MainWindow,"aaaa")
    MainWindow.show()
    sys.exit(app.exec_())
