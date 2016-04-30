
from PyQt4 import QtGui, QtCore
from DialogAgregarTarea import Ui_Dialog_AgregarTarea

class DialogAgregarTarea(QtGui.QDialog):
	def __init__(self,parent):
		QtGui.QDialog.__init__(self, parent)
		self.DialogAgregarTarea = Ui_Dialog_AgregarTarea()
		self.DialogAgregarTarea.setupUi(self)
		self.setAttribute(QtCore.Qt.WA_QuitOnClose,False)

		self.parent = parent
		self.connect(self.DialogAgregarTarea.pushButton_Guardar, QtCore.SIGNAL("clicked()"),self.GuardarTarea)

		

	def GuardarTarea(self):
		self.Nombre = self.DialogAgregarTarea.lineEdit_Descripcion.text()
		self.Query = self.DialogAgregarTarea.lineEdit_Ejecucion.text()
		self.Parametros = self.DialogAgregarTarea.lineEdit_Parametros.text()

		if self.Nombre != '' and self.Query != '':
			self.parent.BD.Insertar('INSERT INTO t365_Jobs (nombre,query,params) VALUES (?,?,?)',[unicode(self.Nombre,'Latin-1'), unicode(self.Query,'Latin-1'), unicode(self.Parametros,'Latin-1')])
			self.close()

