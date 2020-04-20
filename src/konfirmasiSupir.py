# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'konfirmasiSupir.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import waktuPinjam

class konfirmasiSupir(object):
    def openWindowWaktuPinjamOK(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = waktuPinjam.waktuPinjam()
        self.ui.setupUi(self.window,self.mobil,self.database,True,self.username)
        self.window.show()
        self.Dialog.close()
    def openWindowWaktuPinjamCancel(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = waktuPinjam.waktuPinjam()
        self.ui.setupUi(self.window,self.mobil,self.database,False,self.username)
        self.window.show()
        self.Dialog.close()
    def setupUi(self, Dialog,mobil,database,username):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.splitter_2)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.openWindowWaktuPinjamOK)
        self.buttonBox.rejected.connect(self.openWindowWaktuPinjamCancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog=Dialog
        self.mobil=mobil
        self.database=database
        self.username=username
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Supir verified"))
        self.label.setText(_translate("Dialog", "Pinjam.in"))
        self.label_2.setText(_translate("Dialog", "Apakah anda ingin menambahkan supir?"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = konfirmasiSupir()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''
