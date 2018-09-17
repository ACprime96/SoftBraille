# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dia1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import os, errno
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import get_path
from pathlib import Path


# this dialog is for New Project
class Ui_Dialog(object):
    s=""
    f1=""
    config=""
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(406, 135)
        Dialog.setMinimumSize(QtCore.QSize(406, 135))
        Dialog.setMaximumSize(QtCore.QSize(406, 135))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 131, 21))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 311, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.okbtn = QtWidgets.QPushButton(Dialog)
        self.okbtn.setGeometry(QtCore.QRect(280, 80, 113, 32))
        self.okbtn.setObjectName("okbtn")
        self.okbtn.clicked.connect(self.new_Project)
        self.okbtn.clicked.connect(Dialog.close)

        self.cancelbtn = QtWidgets.QPushButton(Dialog)
        self.cancelbtn.setGeometry(QtCore.QRect(160, 80, 113, 32))
        self.cancelbtn.setObjectName("cancelbtn")
        self.cancelbtn.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.label.setText(_translate("Dialog", "Enter Folder Name :"))
        self.okbtn.setText(_translate("Dialog", "OK"))
        self.cancelbtn.setText(_translate("Dialog", "Cancel"))

    def new_Project(self):
        # create new directory
        s = self.lineEdit.text()
        try:
            # rf = open("/Users/adityachandra/Environments/myocr/Gui/config.json")
            # config = json.load(rf)
            # rf.close()
            # wf = open("/Users/adityachandra/Environments/myocr/Gui/config.json","w")
            home = str(Path.home())

            # os.chdir('/Users/adityachandra')
            # os.mkdir(s)
            # os.chdir('/Users/adityachandra/'+s)
            # open("eng.txt","w")
            # open("br.txt","w")
            # os.mkdir('images')
            # os.mkdir('braille_images')
            # f1="/Users/adityachandra/" + s

            # os.chdir(home)
            f1=home + "/" + s
            os.mkdir(f1)
            # print (f1)
            # os.chdir(f1)
            open(f1+"/eng.txt","w")
            open(f1+"/br.txt","w")
            os.mkdir(f1+'/images')
            os.mkdir(f1+'/braille_images')

            # print(f1)


            # print(config)
            # print(f1)
            # config["folder_path"] = f1
            # config["images"] = f1 + "/images"
            # config["english"] = f1 + "/eng.txt"
            # config["braille"] = f1 + "/br.txt"
            #
            #
            # json.dump(config,wf)
            # wf.close()
            get_path.get_file_path(f1)


        except OSError as e:
            if e.errno == errno.EEXIST:
                # Do something
                self.msg = QtWidgets.QMessageBox()
                self.msg.setIcon(QtWidgets.QMessageBox.Critical)
                self.msg.setText("This Folder Already Exists")
                # f=open('/Users/adityachandra/Environments/myocr/Gui/config.json','w')
                # json.dump(config,f)
                # wf.close()
                self.msg.setWindowTitle("ERROR!!")
                self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                self.msg.show()
    def get_stuff(self):
        return self.config

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
