# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 371, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.idEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.idEdit.setObjectName("idEdit")
        self.verticalLayout.addWidget(self.idEdit)
        self.nameEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout.addWidget(self.nameEdit)
        self.degreeEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.degreeEdit.setObjectName("degreeEdit")
        self.verticalLayout.addWidget(self.degreeEdit)
        self.typeEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.typeEdit.setObjectName("typeEdit")
        self.verticalLayout.addWidget(self.typeEdit)
        self.descriptionEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.verticalLayout.addWidget(self.descriptionEdit)
        self.priceEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.priceEdit.setObjectName("priceEdit")
        self.verticalLayout.addWidget(self.priceEdit)
        self.volumeEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.volumeEdit.setObjectName("volumeEdit")
        self.verticalLayout.addWidget(self.volumeEdit)
        self.applyButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.applyButton.setObjectName("applyButton")
        self.verticalLayout.addWidget(self.applyButton)
        self.exitButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())