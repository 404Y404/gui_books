# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from base import base
import wget

def parse(name, path):
    name,start,stop=name.split(",", maxsplit=3)
    link=base[name.replace("-","—")]
    s=link.split("/")
    link=""
    for i in range(len(s)):
        if i!=6:
            link+=s[i]+"/"
        else:
            link+="{}"+s[i][2:]+"/"
    link=link[:-1]
    for i in range(int(start),int(stop)+1):
        wget.download(link.format("0"+str(i)),out=path+"/"+str(i)+".mp3")
        print(f"\n{i} скачано")


class Ui_mainWindow(object):
    path=""

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(400, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Без названия.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 500, 84, 34))
        self.pushButton.setMaximumSize(QtCore.QSize(84, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 370, 251, 51))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 320, 251, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 70, 251, 91))
        self.textEdit.setObjectName("textEdit")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.add_func()
        self.textEdit.setText("Название,от,до")

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Парсер аудиокниг"))
        self.pushButton.setText(_translate("mainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("mainWindow", "Скачать"))
        self.pushButton_3.setText(_translate("mainWindow", "Выбрать папку"))
    
    def add_func(self):
        self.pushButton_2.clicked.connect(self.download)
        self.pushButton_3.clicked.connect(self.folder)


    def download(self):
        if self.textEdit.toPlainText() == "":
            self.textEdit.setText("Введите название")
        elif self.path == "":
            self.textEdit.setText("не выбрана папка")

        parse(self.textEdit.toPlainText(), self.path)


    def folder(self):
        self.path = QFileDialog.getExistingDirectory()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
