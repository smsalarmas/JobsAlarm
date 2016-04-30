# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogEditarTarea.ui'
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

class Ui_Dialog_EditarTarea(object):
    def setupUi(self, Dialog_EditarTarea):
        Dialog_EditarTarea.setObjectName(_fromUtf8("Dialog_EditarTarea"))
        Dialog_EditarTarea.resize(340, 119)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_EditarTarea.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog_EditarTarea)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_Descripcion = QtGui.QLineEdit(Dialog_EditarTarea)
        self.lineEdit_Descripcion.setObjectName(_fromUtf8("lineEdit_Descripcion"))
        self.gridLayout.addWidget(self.lineEdit_Descripcion, 0, 1, 1, 1)
        self.lineEdit_Ejecucion = QtGui.QLineEdit(Dialog_EditarTarea)
        self.lineEdit_Ejecucion.setObjectName(_fromUtf8("lineEdit_Ejecucion"))
        self.gridLayout.addWidget(self.lineEdit_Ejecucion, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog_EditarTarea)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog_EditarTarea)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_Parametros = QtGui.QLineEdit(Dialog_EditarTarea)
        self.lineEdit_Parametros.setObjectName(_fromUtf8("lineEdit_Parametros"))
        self.gridLayout.addWidget(self.lineEdit_Parametros, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog_EditarTarea)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton_Guardar = QtGui.QPushButton(Dialog_EditarTarea)
        self.pushButton_Guardar.setObjectName(_fromUtf8("pushButton_Guardar"))
        self.gridLayout.addWidget(self.pushButton_Guardar, 3, 0, 1, 2)

        self.retranslateUi(Dialog_EditarTarea)
        QtCore.QMetaObject.connectSlotsByName(Dialog_EditarTarea)

    def retranslateUi(self, Dialog_EditarTarea):
        Dialog_EditarTarea.setWindowTitle(_translate("Dialog_EditarTarea", "Editar Tarea", None))
        self.lineEdit_Ejecucion.setPlaceholderText(_translate("Dialog_EditarTarea", "store_NombreStoreProcedure", None))
        self.label_2.setText(_translate("Dialog_EditarTarea", "Ejecucion", None))
        self.label.setText(_translate("Dialog_EditarTarea", "Descripcion", None))
        self.lineEdit_Parametros.setPlaceholderText(_translate("Dialog_EditarTarea", "param1,param2,param3,param4", None))
        self.label_3.setText(_translate("Dialog_EditarTarea", "Parametros", None))
        self.pushButton_Guardar.setText(_translate("Dialog_EditarTarea", "Guardar", None))

import recursos_rc
