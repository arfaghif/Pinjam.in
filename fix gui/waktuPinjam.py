# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waktuPinjam.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pembayaran

class waktuPinjam(object):
    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def openWindowPembayaran(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pembayaran.pembayaran()
        self.ui.setupUi(self.window,self.username)
        self.window.show()
        self.Dialog.close()
    def pushPembayaran(self):
        text="Anda telah membuat pesanan dengan rincian:\nID Transaksi: "
        pesanan=[]
        self.database.getData("select COUNT(*) from transaksi",pesanan)
        num=int(pesanan[0][0]) + 1
        text+= str(num) + "\n"
        result=[]
        self.database.getData("select namakendaraan,tahun,alamat,harga,deskripsi,tambahan,username from kendaraan where IDKend LIKE {}".format(self.mobil),result)
        text+="Nama mobil: "+ str(result[0][0]) +"\n"
        text+="Tahun: "+ str(result[0][1]) +"\n"
        text+="Alamat: "+ str(result[0][2]) +"\n"
        text+="Harga Sewa: "+ str(result[0][3]) +"\n"
        text+="Deskripsi: "+ str(result[0][4]) +"\n"
        text+="Tambahan Supir: "+ str(result[0][5]) +"\n"
        lamaWaktu=int(self.lineEdit.text())
        biaya_total=0
        if(self.supir):
            biaya_total=int(lamaWaktu*(((int(result[0][5])/100) + 1)*int(result[0][3])))
        else:
            biaya_total=int(result[0][3])*lamaWaktu
        
        text+="Total biaya peminjaman: " + str(biaya_total) +"."
        
        sql = "INSERT INTO transaksi (IDKend,nominal,unamepenyewa,unamepembeli,konfirmasi,status) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.mobil, biaya_total,str(result[0][6]),self.username,0,"NULL")
        self.database.insertDatabase(sql,val)
    
        self.messageBox("pesanan verified", text)
        self.openWindowPembayaran()
    def setupUi(self, Dialog, mobil, database, supir, username):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 381, 241))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton.clicked.connect(self.pushPembayaran)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog=Dialog
        self.mobil=mobil
        self.database=database
        self.supir=supir
        self.username=username
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Pinjam.in"))
        self.label_2.setText(_translate("Dialog", "Masukkan waktu pinjam kendaraan"))
        self.lineEdit.setText(_translate("Dialog", "waktu pinjam kendaraan"))
        self.pushButton.setText(_translate("Dialog", "Submit"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = waktuPinjam()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''