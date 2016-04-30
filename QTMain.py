# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTMain.ui'
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
        MainWindow.resize(537, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tableWidget_Tareas = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidget_Tareas.setObjectName(_fromUtf8("tableWidget_Tareas"))
        self.tableWidget_Tareas.setColumnCount(4)
        self.tableWidget_Tareas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Tareas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Tareas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Tareas.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_Tareas.setHorizontalHeaderItem(3, item)
        self.gridLayout_4.addWidget(self.tableWidget_Tareas, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tableWidget_TareasConfig = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_TareasConfig.setObjectName(_fromUtf8("tableWidget_TareasConfig"))
        self.tableWidget_TareasConfig.setColumnCount(4)
        self.tableWidget_TareasConfig.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TareasConfig.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TareasConfig.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TareasConfig.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_TareasConfig.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tableWidget_TareasConfig, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAgregar_Tarea = QtGui.QAction(MainWindow)
        self.actionAgregar_Tarea.setObjectName(_fromUtf8("actionAgregar_Tarea"))
        self.actionProgramar_Tareas = QtGui.QAction(MainWindow)
        self.actionProgramar_Tareas.setObjectName(_fromUtf8("actionProgramar_Tareas"))
        self.actionProgramar_Tarea = QtGui.QAction(MainWindow)
        self.actionProgramar_Tarea.setObjectName(_fromUtf8("actionProgramar_Tarea"))
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAgregar_Tarea)
        self.menuMenu.addAction(self.actionProgramar_Tarea)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "365Jobs", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Listado de Tareas", None))
        item = self.tableWidget_Tareas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tableWidget_Tareas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Query", None))
        item = self.tableWidget_Tareas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Parametros", None))
        item = self.tableWidget_Tareas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Acciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tareas", None))
        self.groupBox.setTitle(_translate("MainWindow", "Listado de Tareas Programadas", None))
        item = self.tableWidget_TareasConfig.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tableWidget_TareasConfig.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo", None))
        item = self.tableWidget_TareasConfig.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prox Ejec", None))
        item = self.tableWidget_TareasConfig.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Acciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tareas Programadas", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.actionAgregar_Tarea.setText(_translate("MainWindow", "Agregar Tarea", None))
        self.actionProgramar_Tareas.setText(_translate("MainWindow", "Programar Tareas", None))
        self.actionProgramar_Tarea.setText(_translate("MainWindow", "Programar Tarea", None))

import recursos_rc
