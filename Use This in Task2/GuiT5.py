# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiT5.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow



class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1294, 1191)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Newtabbtn = QtWidgets.QPushButton(self.centralwidget)
        self.Newtabbtn.setGeometry(QtCore.QRect(100, 11, 93, 28))
        self.Newtabbtn.setObjectName("Newtabbtn")
        self.Removetabbtn = QtWidgets.QPushButton(self.centralwidget)
        self.Removetabbtn.setGeometry(QtCore.QRect(280, 11, 93, 28))
        self.Removetabbtn.setObjectName("Removetabbtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 10, 400, 28))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 1291, 971))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()

        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 29, 1251, 798))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Graph1 = PlotWidget(self.layoutWidget)
        self.Graph1.setObjectName("Graph1")
        self.gridLayout_2.addWidget(self.Graph1, 2, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 2)
        self.Graph1_3 = PlotWidget(self.layoutWidget)
        self.Graph1_3.setObjectName("Graph1_3")
        self.gridLayout_2.addWidget(self.Graph1_3, 6, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 2)
        self.Graph1_2 = PlotWidget(self.layoutWidget)
        self.Graph1_2.setObjectName("Graph1_2")
        self.gridLayout_2.addWidget(self.Graph1_2, 4, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(910, 920, 131, 20))
        self.label_9.setObjectName("label_9")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(20, 830, 1121, 86))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider_11 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_11.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_11.setObjectName("verticalSlider_11")
        self.horizontalLayout.addWidget(self.verticalSlider_11)
        self.verticalSlider = QtWidgets.QSlider(self.widget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout.addWidget(self.verticalSlider)
        self.verticalSlider_2 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout.addWidget(self.verticalSlider_2)
        self.verticalSlider_3 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout.addWidget(self.verticalSlider_3)
        self.verticalSlider_4 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.horizontalLayout.addWidget(self.verticalSlider_4)
        self.verticalSlider_5 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.horizontalLayout.addWidget(self.verticalSlider_5)
        self.verticalSlider_6 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.horizontalLayout.addWidget(self.verticalSlider_6)
        self.verticalSlider_7 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.horizontalLayout.addWidget(self.verticalSlider_7)
        self.verticalSlider_8 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.horizontalLayout.addWidget(self.verticalSlider_8)
        self.verticalSlider_9 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.horizontalLayout.addWidget(self.verticalSlider_9)
        self.verticalSlider_10 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_10.setObjectName("verticalSlider_10")
        self.horizontalLayout.addWidget(self.verticalSlider_10)
        self.verticalSlider_12 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_12.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_12.setObjectName("verticalSlider_12")
        self.horizontalLayout.addWidget(self.verticalSlider_12)
        #self.verticalSlider_13 = QtWidgets.QSlider(self.widget)
        #self.verticalSlider_13.setOrientation(QtCore.Qt.Vertical)
        #self.verticalSlider_13.setObjectName("verticalSlider_13")
        #self.horizontalLayout.addWidget(self.verticalSlider_13)
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab, "222")

        # self.CompareButton = QtWidgets.QPushButton(self.centralwidget)
        # self.CompareButton.setGeometry(QtCore.QRect(190, 10, 93, 28))
        # self.CompareButton.setObjectName("CompareButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1294, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.tabs = QtWidgets.QTabWidget()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Newtabbtn.setText(_translate("MainWindow", "New tab"))
        self.Removetabbtn.setText(_translate("MainWindow", "Remove tab"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">SIGNAL VIEWER & EQUALIZER</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Signal"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label_5.setText(_translate("MainWindow", "To PDF"))
        self.pushButton_3.setText(_translate("MainWindow", "Convert to PDF"))
        self.label_3.setText(_translate("MainWindow", "zoom in"))
        self.pushButton_5.setText(_translate("MainWindow", "Zoom in"))
        self.label_7.setText(_translate("MainWindow", "Start"))
        self.pushButton_4.setText(_translate("MainWindow", "Starting"))
        self.label_4.setText(_translate("MainWindow", "sampling rate(Hz)"))
        self.label_6.setText(_translate("MainWindow", "update interval(ms)"))
        self.pushButton_7.setText(_translate("MainWindow", "add to pdf"))
        self.pushButton_6.setText(_translate("MainWindow", "Zoom Out"))
        self.pushButton_8.setText(_translate("MainWindow", "Scroll"))
        self.pushButton_2.setText(_translate("MainWindow", "Pause"))
        self.label_8.setText(_translate("MainWindow", "After"))
        self.label_10.setText(_translate("MainWindow", "Spectrogram"))
        self.label_9.setText(_translate("MainWindow", "SpectroGram Sliders"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        # self.CompareButton.setText(_translate("MainWindow", "Compare"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
