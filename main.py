#!/usr/bin/env python
# -*- coding: latin-1 -*-
from PyQt4 import QtGui, QtCore
from QTMain import Ui_MainWindow
from bd import BasedeDatos
import time, sys
import globalvars
from date import LaFecha
from apscheduler.schedulers.qt import QtScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger
#Arranque de las variables globales.
from agregartarea import DialogAgregarTarea
from programartarea import DialogProgramarTarea
from editartarea import DialogEditarTarea
import logging
logging.basicConfig()
globalvars.initvars()
from functools import partial

class MainClass(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.MainWindow = Ui_MainWindow()
		self.MainWindow.setupUi(self)

		self.iconoeditar = QtGui.QIcon()
		self.iconoeditar.addPixmap(QtGui.QPixmap(":/ico/edit-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.iconoborrar = QtGui.QIcon()
		self.iconoborrar.addPixmap(QtGui.QPixmap(":/ico/Delete_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.iconocam =QtGui.QIcon()

		self.setWindowIcon(QtGui.QIcon("icon.png"))

		self.MainWindow.tableWidget_TareasConfig.verticalHeader().setVisible(False)
		self.MainWindow.tableWidget_TareasConfig.setShowGrid(False)
		self.MainWindow.tableWidget_TareasConfig.setAlternatingRowColors(True)
		self.MainWindow.tableWidget_TareasConfig.verticalHeader().setDefaultSectionSize(20)
		self.MainWindow.tableWidget_TareasConfig.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.MainWindow.tableWidget_TareasConfig.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

		self.MainWindow.tableWidget_Tareas.verticalHeader().setVisible(False)
		self.MainWindow.tableWidget_Tareas.setShowGrid(False)
		self.MainWindow.tableWidget_Tareas.setAlternatingRowColors(True)
		self.MainWindow.tableWidget_Tareas.verticalHeader().setDefaultSectionSize(20)
		self.MainWindow.tableWidget_Tareas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.MainWindow.tableWidget_Tareas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

		self.connect(self.MainWindow.actionAgregar_Tarea, QtCore.SIGNAL("triggered()"),self.AbrirAgregarTarea)
		self.connect(self.MainWindow.actionProgramar_Tarea, QtCore.SIGNAL("triggered()"),self.AbrirProgramarTarea)
		
		self.scheduler = QtScheduler()

		self.BD = BasedeDatos()
		self.BD.Conectar()

		self.CargarTareasProgramadas()
		self.CargarTareas()
		self.ProgramarTareas()

		self.ListarTareas()
		self.ListarTareasProgramadas()
		##################   FUNCIONES PARA EL SYSTEM TRAY ICON   #######################


		self.exitOnClose = False
		exit = QtGui.QAction(QtGui.QIcon("icon.png"), "Cerrar 365Jobs", self)
		self.connect(exit, QtCore.SIGNAL("triggered()"), self.exitEvent)
		self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon("icon.png"), self)
		menu = QtGui.QMenu(self)
		menu.addAction(exit)
		self.trayIcon.setContextMenu(menu)
		self.connect(self.trayIcon, \
			QtCore.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), \
			self.trayIconActivated)
		self.trayIcon.show()
		self.trayIcon.showMessage("365Jobs Abierto!", "Click para abrir la Ventana\nBoton derecho para Menu" )
		self.trayIcon.setToolTip("365Jobs")

		print self.DictTareasProgramadasByID

	def trayIconActivated(self, reason):
		if reason == QtGui.QSystemTrayIcon.Context:
			self.trayIcon.contextMenu().show()
		elif reason == QtGui.QSystemTrayIcon.Trigger:
			self.show()
			self.raise_()

	def closeEvent(self, event):
		if self.exitOnClose:
			self.trayIcon.hide()
			del self.trayIcon
			#event.accept()
		else:
			self.hide()
			event.setAccepted(True)
			event.ignore()

	def exitEvent(self):
		self.exitOnClose = True
		self.close()

	def AbrirAgregarTarea(self):
		self.DialogAgregarTarea = DialogAgregarTarea(self)
		self.DialogAgregarTarea.show()

	def AbrirProgramarTarea(self):
		self.DialogProgramarTarea = DialogProgramarTarea(self)
		self.DialogProgramarTarea.show()

	def AbrirEditarTarea(self,idtarea):
		self.DialogEditarTarea = DialogEditarTarea(self,idtarea)
		self.DialogEditarTarea.show()

	def CargarTareas(self):
		self.Tareas = self.BD.Seleccionar("""SELECT * FROM t365_Jobs """)

	def CargarTareasProgramadas(self):
		self.TareasProg = self.BD.Seleccionar("""SELECT t365_JobsTipos.Nombre AS nombretipo, t365_Jobs.nombre AS nombretarea, t365_JobsConfig.id_tareaconfig,t365_JobsConfig.id_tarea, t365_JobsConfig.id_tipo, t365_JobsConfig.day_run_date, t365_JobsConfig.interval_weeks, 
                         t365_JobsConfig.interval_days, t365_JobsConfig.interval_hours, t365_JobsConfig.interval_seconds, t365_JobsConfig.interval_minutes, t365_JobsConfig.start_date, t365_JobsConfig.end_date, 
                         t365_JobsConfig.cron_year, t365_JobsConfig.cron_month, t365_JobsConfig.cron_day, t365_JobsConfig.cron_week, t365_JobsConfig.cron_day_of_week, t365_JobsConfig.cron_hour, t365_JobsConfig.cron_minute,
                          t365_JobsConfig.cron_second, t365_Jobs.query, t365_Jobs.params FROM t365_Jobs INNER JOIN
                         t365_JobsConfig ON t365_Jobs.id_tarea = t365_JobsConfig.id_tarea INNER JOIN
                         t365_JobsTipos ON t365_JobsConfig.id_tipo = t365_JobsTipos.id_tipo""")

	def ListarTareas(self):
		
		while self.MainWindow.tableWidget_Tareas.rowCount() > 0:
			self.MainWindow.tableWidget_Tareas.removeRow(0)

		for datostarea in self.Tareas:
			Siguiente = self.MainWindow.tableWidget_Tareas.rowCount()
			self.MainWindow.tableWidget_Tareas.insertRow(Siguiente)
			columna = 0
			texto = QtGui.QTableWidgetItem(datostarea.nombre)
			self.MainWindow.tableWidget_Tareas.setItem(Siguiente,columna,texto)
			columna = 1
			texto = QtGui.QTableWidgetItem(datostarea.query)
			self.MainWindow.tableWidget_Tareas.setItem(Siguiente,columna,texto)
			columna = 2
			texto = QtGui.QTableWidgetItem(datostarea.params)
			self.MainWindow.tableWidget_Tareas.setItem(Siguiente,columna,texto)
			columna = 3
			ly = QtGui.QHBoxLayout()
			ly.setContentsMargins(0, 0, 0, 0)
			wdg = QtGui.QWidget()
			btneditar = QtGui.QPushButton(self.MainWindow.tableWidget_Tareas)
			btneditar.setFlat(True)
			btneditar.setIcon(self.iconoeditar)
			ly.addWidget(btneditar)
			#####################################################################################
			btnborrar = QtGui.QPushButton(self.MainWindow.tableWidget_Tareas)
			btnborrar.setFlat(True)
			btnborrar.setIcon(self.iconoborrar)
			ly.addWidget(btnborrar)
			wdg.setLayout(ly)
			self.MainWindow.tableWidget_Tareas.setCellWidget(Siguiente, columna, wdg)
			btneditar.clicked.connect(partial(self.AbrirEditarTarea,datostarea.id_tarea))
			btnborrar.clicked.connect(partial(self.BorrarTareayConfigPorIDTarea,str(datostarea.id_tarea)))
		
	def ListarTareasProgramadas(self):
		
		while self.MainWindow.tableWidget_TareasConfig.rowCount() > 0:
			self.MainWindow.tableWidget_TareasConfig.removeRow(0)

		for datostarea in self.TareasProg:
			Siguiente = self.MainWindow.tableWidget_TareasConfig.rowCount()
			self.MainWindow.tableWidget_TareasConfig.insertRow(Siguiente)
			columna = 0
			texto = QtGui.QTableWidgetItem(datostarea.nombretarea)
			self.MainWindow.tableWidget_TareasConfig.setItem(Siguiente,columna,texto)
			columna = 1
			texto = QtGui.QTableWidgetItem(datostarea.nombretipo)
			self.MainWindow.tableWidget_TareasConfig.setItem(Siguiente,columna,texto)
			columna = 3
			ly = QtGui.QHBoxLayout()
			ly.setContentsMargins(0, 0, 0, 0)
			wdg = QtGui.QWidget()
			#####################################################################################
			btnborrar = QtGui.QPushButton(self.MainWindow.tableWidget_TareasConfig)
			btnborrar.setFlat(True)
			btnborrar.setIcon(self.iconoborrar)
			ly.addWidget(btnborrar)
			wdg.setLayout(ly)
			self.MainWindow.tableWidget_TareasConfig.setCellWidget(Siguiente, columna, wdg)
			btnborrar.clicked.connect(partial(self.BorrarTareaConfig,str(datostarea.id_tareaconfig)))
	
	def ProgramarTareas(self):
		Siguiente = -1
		columna = 2 #Siempre 2 porque es donde van los botones
		self.DictTareasProgramadasFilasColumnas = {}
		self.DictTareasProgramadasByID = {}
		self.ListaOrdenJobs = []
		for datostarea in self.TareasProg:
			Siguiente = Siguiente + 1
			if datostarea.nombretipo == 'Fecha':
				self.trigger = DateTrigger(run_date=datostarea.day_run_date)
				self.job = self.scheduler.add_job(id=str(datostarea.id_tareaconfig), name=datostarea.nombretarea, func=self.EjecutarQuery, trigger=self.trigger, args =[datostarea.query,datostarea.params])

			elif datostarea.nombretipo == 'Cronometro':
				self.trigger = CronTrigger(year=datostarea.cron_year, month=datostarea.cron_month, day=datostarea.cron_day, week=datostarea.cron_week, day_of_week=datostarea.cron_day_of_week, hour=datostarea.cron_hour, minute=datostarea.cron_minute, second=datostarea.cron_second, start_date=datostarea.start_date, end_date=datostarea.end_date)
				self.job = self.scheduler.add_job(id=str(datostarea.id_tareaconfig), name=datostarea.nombretarea, func=self.EjecutarQuery, trigger=self.trigger, args =[datostarea.query,datostarea.params])

			elif datostarea.nombretipo == 'Interval':
				self.trigger = IntervalTrigger(weeks=datostarea.interval_weeks, days=datostarea.interval_days, hours=datostarea.interval_hours, minutes=datostarea.interval_minutes, seconds=datostarea.interval_seconds, start_date=datostarea.start_date, end_date=datostarea.end_date)
				self.job = self.scheduler.add_job(id=str(datostarea.id_tareaconfig), name=datostarea.nombretarea, func=self.EjecutarQuery, trigger=self.trigger, args =[datostarea.query,datostarea.params])
			self.ListaOrdenJobs.append(self.job)
			self.DictTareasProgramadasFilasColumnas[self.job] = [Siguiente,columna]
			self.DictTareasProgramadasByID[str(datostarea.id_tareaconfig)] = self.job
		
		self.scheduler.start()
		self.scheduler.print_jobs()
		self.PintarFechasProxEjec()
	
	def PintarFechasProxEjec(self):
		for idtp in self.ListaOrdenJobs:
			proximaejecucion = idtp.next_run_time.strftime("%d %b %Y %H:%M:%S")
			texto = QtGui.QTableWidgetItem(proximaejecucion)
			self.MainWindow.tableWidget_TareasConfig.setItem(self.DictTareasProgramadasFilasColumnas[idtp][0],self.DictTareasProgramadasFilasColumnas[idtp][1],texto)			
		print self.DictTareasProgramadasFilasColumnas		
	
	def EjecutarQuery(self,query,params):
		if not params:
			self.BD.Insertar('exec  '+str(query))
		else:
			listapar = []
			for par in params:
				listapar.append(par)

			cantidadparametros = len(params)
			query  = 'exec  '+str(query)+' ?'
			for arg in range(cantidadparametros-1):
				query = query + ' ,?'
			print query
			self.BD.Insertar(query,listapar)
		self.PintarFechasProxEjec()
	
	def BorrarTareaConfig(self,idtareaconfig):

		self.BD.Borrar('DELETE FROM t365_JobsConfig WHERE id_tareaconfig = ? ',str(idtareaconfig))
		jobeliminado = self.DictTareasProgramadasByID[str(idtareaconfig)]
		jobeliminado.remove()
		del self.DictTareasProgramadasByID[str(idtareaconfig)]
		del self.DictTareasProgramadasFilasColumnas[jobeliminado]
		self.ListaOrdenJobs.remove(jobeliminado)
		self.CargarTareasProgramadas()
		self.ListarTareasProgramadas()

	def BorrarTareayConfigPorIDTarea(self,idtarea):
		tareasborrar = self.BD.Seleccionar('SELECT id_tareaconfig FROM t365_JobsConfig WHERE id_tarea = ?',str(idtarea))
		for tar in tareasborrar:
			self.BD.Borrar('DELETE FROM t365_JobsConfig WHERE id_tareaconfig = ? ',str(tar.id_tareaconfig))
			jobeliminado = self.DictTareasProgramadasByID[str(tar.id_tareaconfig)]
			jobeliminado.remove()
			del self.DictTareasProgramadasByID[str(tar.id_tareaconfig)]
			del self.DictTareasProgramadasFilasColumnas[jobeliminado]
			self.ListaOrdenJobs.remove(jobeliminado)
			self.CargarTareasProgramadas()
			self.ListarTareasProgramadas()
		self.BD.Borrar('DELETE FROM t365_Jobs WHERE id_tarea = ? ',str(idtarea))


	def AgregarTareaProgramada(self,idtareaconfig):
		self.CargarTareasProgramadas()
		self.ListarTareasProgramadas()
		self.NuevaTareaProg = self.BD.Seleccionar("""SELECT t365_JobsTipos.Nombre AS nombretipo, t365_Jobs.nombre AS nombretarea, t365_JobsConfig.id_tareaconfig,t365_JobsConfig.id_tarea, t365_JobsConfig.id_tipo, t365_JobsConfig.day_run_date, t365_JobsConfig.interval_weeks, 
                         t365_JobsConfig.interval_days, t365_JobsConfig.interval_hours, t365_JobsConfig.interval_seconds, t365_JobsConfig.interval_minutes, t365_JobsConfig.start_date, t365_JobsConfig.end_date, 
                         t365_JobsConfig.cron_year, t365_JobsConfig.cron_month, t365_JobsConfig.cron_day, t365_JobsConfig.cron_week, t365_JobsConfig.cron_day_of_week, t365_JobsConfig.cron_hour, t365_JobsConfig.cron_minute,
                          t365_JobsConfig.cron_second, t365_Jobs.query, t365_Jobs.params FROM t365_Jobs INNER JOIN
                         t365_JobsConfig ON t365_Jobs.id_tarea = t365_JobsConfig.id_tarea INNER JOIN
                         t365_JobsTipos ON t365_JobsConfig.id_tipo = t365_JobsTipos.id_tipo Where id_tareaconfig = ?""", str(idtareaconfig[0][0]))
		if self.NuevaTareaProg[0].nombretipo == 'Fecha':
			self.trigger = DateTrigger(run_date=self.NuevaTareaProg[0].day_run_date)
			self.job = self.scheduler.add_job(id=str(self.NuevaTareaProg[0].id_tareaconfig), name=self.NuevaTareaProg[0].nombretarea, func=self.EjecutarQuery, trigger=self.trigger, args =[self.NuevaTareaProg[0].query,self.NuevaTareaProg[0].params])

		elif self.NuevaTareaProg[0].nombretipo == 'Cronometro':
			self.trigger = CronTrigger(year=self.NuevaTareaProg[0].cron_year, month=self.NuevaTareaProg[0].cron_month, day=self.NuevaTareaProg[0].cron_day, week=self.NuevaTareaProg[0].cron_week, day_of_week=self.NuevaTareaProg[0].cron_day_of_week, hour=self.NuevaTareaProg[0].cron_hour, minute=self.NuevaTareaProg[0].cron_minute, second=self.NuevaTareaProg[0].cron_second, start_date=self.NuevaTareaProg[0].start_date, end_date=self.NuevaTareaProg[0].end_date)
			self.job = self.scheduler.add_job(id=str(self.NuevaTareaProg[0].id_tareaconfig), name=self.NuevaTareaProg[0].nombretarea, func=self.EjecutarQuery, trigger=self.trigger, args =[self.NuevaTareaProg[0].query,self.NuevaTareaProg[0].params])

		elif self.NuevaTareaProg[0].nombretipo == 'Interval':
			self.trigger = IntervalTrigger(weeks=self.NuevaTareaProg[0].interval_weeks, days=self.NuevaTareaProg[0].interval_days, hours=self.NuevaTareaProg[0].interval_hours, minutes=self.NuevaTareaProg[0].interval_minutes, seconds=self.NuevaTareaProg[0].interval_seconds, start_date=self.NuevaTareaProg[0].start_date, end_date=self.NuevaTareaProg[0].end_date)
			self.job = self.scheduler.add_job(id=str(self.NuevaTareaProg[0].id_tareaconfig), name=self.NuevaTareaProg[0].nombretarea, func=self.EjecutarQuery, trigger=self.trigger, args =[self.NuevaTareaProg[0].query,self.NuevaTareaProg[0].params])
		self.ListaOrdenJobs.append(self.job)
		posicion = self.ListaOrdenJobs.index(self.job)
		self.DictTareasProgramadasFilasColumnas[self.job] = [posicion,2]
		self.DictTareasProgramadasByID[str(self.NuevaTareaProg[0].id_tareaconfig)] = self.job 
		self.PintarFechasProxEjec()		



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	#app.setStyle(QtGui.QStyleFactory.create("plastique"))
	window = MainClass()
	window.show()
	app.exec_()

