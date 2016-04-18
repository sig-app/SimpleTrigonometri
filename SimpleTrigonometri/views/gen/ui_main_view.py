# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimpleTrigometri\views\main_view.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(762, 598)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.comboBox_1 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_1.setObjectName(_fromUtf8("comboBox_1"))
        self.horizontalLayout_1.addWidget(self.comboBox_1)
        self.lineEdit_1 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_1.setMaxLength(15)
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.horizontalLayout_1.addWidget(self.lineEdit_1)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_2.setMaxLength(15)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.horizontalLayout_4.addWidget(self.comboBox_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_3.setMaxLength(15)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_Calculate = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Calculate.setObjectName(_fromUtf8("pushButton_Calculate"))
        self.horizontalLayout_5.addWidget(self.pushButton_Calculate)
        self.comboBox_deg_rad = QtGui.QComboBox(self.centralwidget)
        self.comboBox_deg_rad.setObjectName(_fromUtf8("comboBox_deg_rad"))
        self.comboBox_deg_rad.addItem(_fromUtf8(""))
        self.comboBox_deg_rad.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBox_deg_rad)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.widget_verticalLayout.setObjectName(_fromUtf8("widget_verticalLayout"))
        self.horizontalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TrigomatryATOR", None))
        self.pushButton_Calculate.setText(_translate("MainWindow", "Calculate", None))
        self.comboBox_deg_rad.setItemText(0, _translate("MainWindow", "Degrees", None))
        self.comboBox_deg_rad.setItemText(1, _translate("MainWindow", "Radians", None))

