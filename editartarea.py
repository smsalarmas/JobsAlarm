
from PyQt4 import QtGui, QtCore
from DialogEditarTarea import Ui_Dialog_EditarTarea

class DialogEditarTarea(QtGui.QDialog):
	def __init__(self,parent,tareaeditar):
		QtGui.QDialog.__init__(self, parent)
		self.DialogEditarTarea = Ui_Dialog_EditarTarea()
		self.DialogEditarTarea.setupUi(self)
		self.setAttribute(QtCore.Qt.WA_QuitOnClose,False)
		self.TareaSeleccionada = tareaeditar
		self.parent = parent
		self.connect(self.DialogEditarTarea.pushButton_Guardar, QtCore.SIGNAL("clicked()"),self.GuardarTarea)

		self.CargarDatos()
	def CargarDatos(self):
		self.DatosTarea = self.parent.BD.Seleccionar('SELECT nombre,query,params FROM t365_Jobs WHERE id_tarea = ?',str(self.TareaSeleccionada))
		if self.DatosTarea:
			for job in self.DatosTarea:				
				self.NombreSeleccionado = job.nombre
				self.QuerySeleccionado = job.query
				self.ParametrosSeleccionados = job.params

		if not self.NombreSeleccionado:
			self.NombreSeleccionado = ''
		if not self.QuerySeleccionado:
			self.QuerySeleccionado = ''
		if not self.ParametrosSeleccionados:
			self.ParametrosSeleccionados = ''

		self.DialogEditarTarea.lineEdit_Descripcion.setText(self.NombreSeleccionado)
		self.DialogEditarTarea.lineEdit_Ejecucion.setText(self.QuerySeleccionado)
		self.DialogEditarTarea.lineEdit_Parametros.setText(self.ParametrosSeleccionados)

	def GuardarTarea(self):
		self.Nombre = self.DialogEditarTarea.lineEdit_Descripcion.text()
		self.Query = self.DialogEditarTarea.lineEdit_Ejecucion.text()
		self.Parametros = self.DialogEditarTarea.lineEdit_Parametros.text()

		if self.Nombre != '' and self.Query != '':
			self.parent.BD.Actualizar('UPDATE t365_Jobs SET nombre=?, query=?, params=?) VALUES (?,?,?)',[unicode(self.Nombre,'Latin-1'), unicode(self.Query,'Latin-1'), unicode(self.Parametros,'Latin-1')])
			self.close()

