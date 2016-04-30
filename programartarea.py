
from PyQt4 import QtGui, QtCore
from DialogProgramarTarea import Ui_Dialog_ProgramarTarea
import time, datetime

class DialogProgramarTarea(QtGui.QDialog):
	def __init__(self,parent):
		super(DialogProgramarTarea, self).__init__()

		self.DialogProgramarTarea = Ui_Dialog_ProgramarTarea()
		self.DialogProgramarTarea.setupUi(self)
		self.setAttribute(QtCore.Qt.WA_QuitOnClose,False)
		self.setMinimumSize(256, 140)
		self.setMaximumSize(256, 140)
		self.resize(256, 140)
		self.DialogProgramarTarea.groupBox_ConfigCron.hide()
		self.DialogProgramarTarea.groupBox_ConfigInterval.hide()
		self.DialogProgramarTarea.groupBox_ConfigFecha.hide()
		self.DialogProgramarTarea.comboBox_Tipo.setCurrentIndex(-1)
		self.parent = parent
		self.CargarJobsTipos()
		self.TipoSeleccionado = None


		self.CargarTareas()
		self.connect(self.DialogProgramarTarea.comboBox_Tipo, QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.CambiarGroupJobs)
		self.connect(self.DialogProgramarTarea.pushButton_Guardar, QtCore.SIGNAL("clicked()"),self.GuardarProg)
		
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarFinInterval, QtCore.SIGNAL("stateChanged(int)"),self.EstadoFechasInterval)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarInicioInterval, QtCore.SIGNAL("stateChanged(int)"),self.EstadoFechasInterval)
		
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarAnoCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarMesCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarDiaCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarSemanaCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarDiaSemanaCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarHoraCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarMinutoCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarSegundoCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarInicioCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)
		self.connect(self.DialogProgramarTarea.checkBox_HabilitarFinCron, QtCore.SIGNAL("stateChanged(int)"),self.EstadoItemsCron)

		self.DialogProgramarTarea.spinBox_CronAno.setEnabled(False)
		self.DialogProgramarTarea.spinBox_CronMes.setEnabled(False)
		self.DialogProgramarTarea.spinBox_CronDia.setEnabled(False)
		self.DialogProgramarTarea.spinBox_CronSemana.setEnabled(False)
		self.DialogProgramarTarea.spinBox_CronDiaSemana.setEnabled(False)
		self.DialogProgramarTarea.spinBox_CronHora.setEnabled(False)
		self.DialogProgramarTarea.spinBox_CronMinuto.setEnabled(False)
		self.DialogProgramarTarea.spinBox_CronSegundo.setEnabled(False)
		self.DialogProgramarTarea.dateTimeEdit_CronInicio.setEnabled(False)
		self.DialogProgramarTarea.dateTimeEdit_CronFin.setEnabled(False)


		self.DialogProgramarTarea.dateTimeEdit_IntervalInicio.setEnabled(False)
		self.DialogProgramarTarea.dateTimeEdit_IntervalFin.setEnabled(False)
	def CargarTareas(self):
		self.Tareas = self.parent.BD.Seleccionar('SELECT * FROM t365_Jobs')
		self.ListarTareasCombo()		
	def EstadoItemsCron(self):
		if self.DialogProgramarTarea.checkBox_HabilitarAnoCron.isChecked():
			self.DialogProgramarTarea.spinBox_CronAno.setEnabled(True)
		else:
			self.DialogProgramarTarea.spinBox_CronAno.setEnabled(False)

		if self.DialogProgramarTarea.checkBox_HabilitarMesCron.isChecked():
			self.DialogProgramarTarea.spinBox_CronMes.setEnabled(True)
		else:
			self.DialogProgramarTarea.spinBox_CronMes.setEnabled(False)

		if self.DialogProgramarTarea.checkBox_HabilitarDiaCron.isChecked():
			self.DialogProgramarTarea.spinBox_CronDia.setEnabled(True)
		else:
			self.DialogProgramarTarea.spinBox_CronDia.setEnabled(False)

		if self.DialogProgramarTarea.checkBox_HabilitarSemanaCron.isChecked():
			self.DialogProgramarTarea.spinBox_CronSemana.setEnabled(True)
		else:
			self.DialogProgramarTarea.spinBox_CronSemana.setEnabled(False)

		if self.DialogProgramarTarea.checkBox_HabilitarDiaSemanaCron.isChecked():
			self.DialogProgramarTarea.spinBox_CronDiaSemana.setEnabled(True)
		else:
			self.DialogProgramarTarea.spinBox_CronDiaSemana.setEnabled(False)


		if self.DialogProgramarTarea.checkBox_HabilitarHoraCron.isChecked():
			self.DialogProgramarTarea.spinBox_CronHora.setEnabled(True)
		else:
			self.DialogProgramarTarea.spinBox_CronHora.setEnabled(False)


		if self.DialogProgramarTarea.checkBox_HabilitarMinutoCron.isChecked():
			self.DialogProgramarTarea.spinBox_CronMinuto.setEnabled(True)
		else:
			self.DialogProgramarTarea.spinBox_CronMinuto.setEnabled(False)


		if self.DialogProgramarTarea.checkBox_HabilitarSegundoCron.isChecked():
			self.DialogProgramarTarea.spinBox_CronSegundo.setEnabled(True)
		else:
			self.DialogProgramarTarea.spinBox_CronSegundo.setEnabled(False)


		if self.DialogProgramarTarea.checkBox_HabilitarInicioCron.isChecked():
			self.DialogProgramarTarea.dateTimeEdit_CronInicio.setEnabled(True)
		else:
			self.DialogProgramarTarea.dateTimeEdit_CronInicio.setEnabled(False)

		if self.DialogProgramarTarea.checkBox_HabilitarFinCron.isChecked():
			self.DialogProgramarTarea.dateTimeEdit_CronFin.setEnabled(True)
		else:
			self.DialogProgramarTarea.dateTimeEdit_CronFin.setEnabled(False)
	def EstadoFechasInterval(self):
		if self.DialogProgramarTarea.checkBox_HabilitarInicioInterval.isChecked():
			self.DialogProgramarTarea.dateTimeEdit_IntervalInicio.setEnabled(True)
		else:
			self.DialogProgramarTarea.dateTimeEdit_IntervalInicio.setEnabled(False)

		if self.DialogProgramarTarea.checkBox_HabilitarFinInterval.isChecked():
			self.DialogProgramarTarea.dateTimeEdit_IntervalFin.setEnabled(True)
		else:
			self.DialogProgramarTarea.dateTimeEdit_IntervalFin.setEnabled(False)
	def CargarJobsTipos(self):
		self.DictJobsTipos = {}
		self.JobsTipos = self.parent.BD.Seleccionar('SELECT * FROM t365_JobsTipos')
		self.DialogProgramarTarea.comboBox_Tipo.clear()
		for job in self.JobsTipos:
			self.DialogProgramarTarea.comboBox_Tipo.addItem(job.Nombre)
			self.DictJobsTipos[job.Nombre] = job.id_tipo
		self.DialogProgramarTarea.comboBox_Tipo.setCurrentIndex(-1)
	def ListarTareasCombo(self):
		if self.Tareas:
			self.DictTareas = {}
			self.DialogProgramarTarea.comboBox_Tareas.clear()
			for tarea in self.Tareas:
				self.DialogProgramarTarea.comboBox_Tareas.addItem(tarea.nombre)
				self.DictTareas[tarea.nombre] = tarea.id_tarea
	def CambiarGroupJobs(self,nombre):
		if nombre == 'Fecha':
			self.TipoSeleccionado = 'Fecha'
			self.DialogProgramarTarea.groupBox_ConfigCron.hide()
			self.DialogProgramarTarea.groupBox_ConfigInterval.hide()
			self.DialogProgramarTarea.groupBox_ConfigFecha.show()
			self.setMinimumSize(256, 230)
			self.setMaximumSize(256, 230)
			self.resize(256, 230)

		elif nombre == 'Cronometro':
			self.TipoSeleccionado = 'Cronometro'

			self.DialogProgramarTarea.groupBox_ConfigCron.show()
			self.DialogProgramarTarea.groupBox_ConfigInterval.hide()
			self.DialogProgramarTarea.groupBox_ConfigFecha.hide()
			self.setMinimumSize(256, 430)
			self.setMaximumSize(256, 430)
			self.resize(256, 430)
		elif nombre == 'Intervalo':
			self.TipoSeleccionado = 'Intervalo'

			self.DialogProgramarTarea.groupBox_ConfigCron.hide()
			self.DialogProgramarTarea.groupBox_ConfigInterval.show()
			self.DialogProgramarTarea.groupBox_ConfigFecha.hide()
			self.setMinimumSize(256, 355)
			self.setMaximumSize(256, 355)
			self.resize(256, 355)
	def GuardarProg(self):
		TareaSeleccionada = self.DialogProgramarTarea.comboBox_Tareas.currentText()
		if str(self.TipoSeleccionado) == 'Fecha':
			self.FechabyFecha = self.DialogProgramarTarea.dateTimeEditFechaFecha.dateTime().toPyDateTime()
			self.parent.BD.Insertar('INSERT INTO t365_JobsConfig (id_tarea,id_tipo,day_run_date) VALUES (?,?,?)',[str(self.DictTareas[str(TareaSeleccionada)]), str(self.DictJobsTipos['Fecha']),self.FechabyFecha])
			self.pk = self.parent.BD.Seleccionar('SELECT @@identity')
			self.parent.AgregarTareaProgramada(self.pk)
			
		elif str(self.TipoSeleccionado) == 'Cronometro':
			if self.DialogProgramarTarea.checkBox_HabilitarAnoCron.isChecked():
				self.AnobyCron = self.DialogProgramarTarea.spinBox_CronAno.value()
			else:
				self.AnobyCron = None
			if self.DialogProgramarTarea.checkBox_HabilitarMesCron.isChecked():
				self.MesbyCron = self.DialogProgramarTarea.spinBox_CronMes.value()
			else:
				self.MesbyCron = None
			if self.DialogProgramarTarea.checkBox_HabilitarDiaCron.isChecked():
				self.DiabyCron = self.DialogProgramarTarea.spinBox_CronDia.value()
			else:
				self.DiabyCron = None
			if self.DialogProgramarTarea.checkBox_HabilitarSemanaCron.isChecked():
				self.SemanabyCron = self.DialogProgramarTarea.spinBox_CronSemana.value()
			else:
				self.SemanabyCron = None
			if self.DialogProgramarTarea.checkBox_HabilitarDiaSemanaCron.isChecked():
				self.DiaSemanabyCron = self.DialogProgramarTarea.spinBox_CronDiaSemana.value()
			else:
				self.DiaSemanabyCron = None
			if self.DialogProgramarTarea.checkBox_HabilitarHoraCron.isChecked():
				self.HorabyCron = self.DialogProgramarTarea.spinBox_CronHora.value()
			else:
				self.HorabyCron = None
			if self.DialogProgramarTarea.checkBox_HabilitarMinutoCron.isChecked():
				self.MinutobyCron = self.DialogProgramarTarea.spinBox_CronMinuto.value()
			else:
				self.MinutobyCron = None
			if self.DialogProgramarTarea.checkBox_HabilitarSegundoCron.isChecked():
				self.SegundobyCron = self.DialogProgramarTarea.spinBox_CronSegundo.value()
			else:
				self.SegundobyCron = None
			if self.DialogProgramarTarea.checkBox_HabilitarInicioCron.isChecked():
				self.IniciobyCron = self.DialogProgramarTarea.dateTimeEdit_CronInicio.dateTime().toPyDateTime()
			else:
				self.IniciobyCron = None
			if self.DialogProgramarTarea.checkBox_HabilitarFinCron.isChecked():
				self.FinbyCron = self.DialogProgramarTarea.dateTimeEdit_CronFin.dateTime().toPyDateTime()
			else:
				self.FinbyCron = None

			self.parent.BD.Insertar('INSERT INTO t365_JobsConfig (id_tarea, id_tipo, cron_year, cron_month, cron_day, cron_week, cron_day_of_week, cron_hour, cron_minute, cron_second, start_date, end_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',[str(self.DictTareas[str(TareaSeleccionada)]),str(self.DictJobsTipos['Cronometro']),self.AnobyCron, self.MesbyCron, self.DiabyCron, self.SemanabyCron, self.DiaSemanabyCron, self.HorabyCron, self.MinutobyCron, self.SegundobyCron, self.IniciobyCron, self.FinbyCron])
			self.pk = self.parent.BD.Seleccionar('SELECT @@identity')
			self.parent.AgregarTareaProgramada(self.pk)

		elif str(self.TipoSeleccionado) == 'Intervalo':
			self.SemanasbyInter = self.DialogProgramarTarea.spinBox_IntervalSemanas.value()
			self.DiasbyInter = self.DialogProgramarTarea.spinBox_IntervalDias.value()
			self.HorasbyInter = self.DialogProgramarTarea.spinBox_IntervalHoras.value()
			self.MinutosbyInter = self.DialogProgramarTarea.spinBox_IntervalMinutos.value()
			self.SegundosbyInter = self.DialogProgramarTarea.spinBox_IntervalSegundos.value()
			if self.DialogProgramarTarea.checkBox_HabilitarInicioInterval.isChecked():
				self.IniciobyInterval = self.DialogProgramarTarea.dateTimeEdit_IntervalInicio.dateTime().toPyDateTime()
			else:
				self.IniciobyInterval = None
			if self.DialogProgramarTarea.checkBox_HabilitarFinInterval.isChecked():
				self.FinbyInterval = self.DialogProgramarTarea.dateTimeEdit_IntervalFin.dateTime().toPyDateTime()
			else:
				self.FinbyInterval = None
			self.parent.BD.Insertar('INSERT INTO t365_JobsConfig (id_tarea,id_tipo, interval_weeks, interval_days, interval_hours, interval_minutes, interval_seconds, start_date, end_date) VALUES (?,?,?,?,?,?,?,?,?)',[str(self.DictTareas[str(TareaSeleccionada)]),str(self.DictJobsTipos['Cronometro']),int(self.SemanasbyInter),int(self.DiasbyInter),int(self.HorasbyInter),int(self.MinutosbyInter),int(self.SegundosbyInter),self.IniciobyInterval,self.FinbyInterval])
			self.pk = self.parent.BD.Seleccionar('SELECT @@identity')
			self.parent.AgregarTareaProgramada(self.pk)
