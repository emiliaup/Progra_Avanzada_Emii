from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QUrl, QMimeData, Qt, QPointF
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGraphicsView,
 QGraphicsScene, QGraphicsEllipseItem, QPushButton,
QApplication, QHBoxLayout, QVBoxLayout,QGridLayout,QDialog,QProgressBar, QApplication)
import sys
from PyQt5.QtGui import QPixmap, QDrag, QPainter, QCursor
from random import shuffle, sample, randint, choice
from os import path
from time import sleep, time
from ventana_de_errores import Ventana_error_box
from flechas_confirmar import Info_Flechas
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent 
from flechas_pinguinps_threads import Flecha_juego
from parametros import (VELOCIDAD_FLECHA, PUNTOS_FLECHA, DINERO_TRAMPA,
PATH_CANCION1, PATH_CANCION2, PATH_VENTANA_JUEGO, PATH_RANKING)
from continuacion_juegp import MainWindow3

window_name, base_class = uic.loadUiType(PATH_VENTANA_JUEGO)

class MainWindow1(window_name, base_class):
    senal_thread = pyqtSignal(list)
    senal_resumen = pyqtSignal(str,str,int,int,int,int,int,int,int)
    senal_mouse = pyqtSignal(str)
    senal_confirmar_a = pyqtSignal(list)
    senal_confirmar_s = pyqtSignal(list)
    senal_confirmar_w = pyqtSignal(list)
    senal_confirmar_d = pyqtSignal(list)
    senal_ventanai = pyqtSignal()
    senal_cheatcode = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dificultad_box.currentTextChanged.connect(self.dificultad)
        self.botton_comenzar_juego.clicked.connect(self.botton_partir_j)
        self.botton_pausa.clicked.connect(self.pausa)    
        self.cancion_box.currentTextChanged.connect(self.cancion)
        self.boton_salir_juego.clicked.connect(self.boton_salida)
        self.botton_pausa.setEnabled(False)
        self.texto_dificultad = "None"
        self.texto_cancion = "None" 
        self.boom_left.setVisible(False)
        self.boom_right.setVisible(False)
        self.boom_up.setVisible(False)
        self.boom_down.setVisible(False)
        self.press_right.setVisible(False)
        self.press_up.setVisible(False)
        self.press_left.setVisible(False)
        self.press_down.setVisible(False)
        self.velocidad = VELOCIDAD_FLECHA
        self.puntaje_acumulados = 0
        self.dinero = 0
        self.puntos_f = PUNTOS_FLECHA
        self.dinero_trampa = DINERO_TRAMPA
        self.trampa1 = []
        self.flechas_puntos_l = []
        self.lista_y = []
        self.setAcceptDrops(True)
        self.thread = None
        self.nombre_jugador = " "
        self.pasos_terminados = 0
        self.pausa_bool = False
        self.nivel_ronda = 0 
        self.extra = MainWindow3(self)
        

    def nueva_ronda(self, nombre, puntaje_a, dinero_i):
        self.nombre_jugador = nombre
        self.puntaje_acumulados = puntaje_a
        self.dinero = dinero_i
        self.botton_pausa.setEnabled(False)
        self.flecha = []
        self.botton_comenzar_juego.setEnabled(True)
        self.cancion_box.setEnabled(True)
        self.dificultad_box.setEnabled(True)
        self.puntos_combo_total = 0
        self.puntos_combo = 0
        self.puntos_flechas = 0
        self.pasos_correctos = 0
        self.pasos_incorrecto = 0
        self.puntaje_ronda = 0
        self.pasos_totales = 1
        self.trampa1 = []
        self.flechas_puntos_l = []
        self.lista_y = []
        if self.nivel_ronda == 1:
            self.dificultad_box.addItem("Aficionados")

        if self.nivel_ronda == 2:
            self.dificultad_box.addItem("Maestro Cumbia")
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_P:
            self.pausa_bool = True
            self.trampa1 = []
        elif event.key() == Qt.Key_A:
            self.trampa1 = []
            self.aprobar_a(self.lista_y)
            self.press_left.show()
        elif event.key() == Qt.Key_W:
            self.aprobar_w(self.lista_y)
            self.press_up.show()
            self.trampa1 = []
        elif event.key() == Qt.Key_S:
            self.aprobar_s(self.lista_y)
            self.press_down.show()
            self.trampa1 = []
        elif event.key() == Qt.Key_D:
            self.aprobar_d(self.lista_y)
            self.press_right.show()
            self.trampa1 = []
        elif event.key() == Qt.Key_M:
            self.trampa1.append("M")
        elif event.key() == Qt.Key_O:
            self.trampa1.append("O")
        elif event.key() == Qt.Key_N:
            self.trampa1.append("N")
            if self.trampa1[0] == "M" and self.trampa1[1] == "O":
                self.trampa()
            else:
                self.trampa1 = []
                self.trampa1.append("N")
        elif event.key() == Qt.Key_I:
            self.trampa1.append("I")
        elif event.key() == Qt.Key_V:
            self.trampa1.append("V")
            self.trampa()
        else:
            self.trampa1 = []
    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_A:
            self.press_left.hide()
            self.boom_left.hide()
        if event.key() == Qt.Key_W:
            self.press_up.hide()
            self.boom_up.hide()
        if event.key() == Qt.Key_S:
            self.press_down.hide()
            self.boom_down.hide()
        if event.key() == Qt.Key_D:
            self.press_right.hide()
            self.boom_right.hide()

    def botton_partir_j(self):
    
        if self.texto_cancion == "None" or self.texto_dificultad == "None":
            self.ventana_error1 = Ventana_error_box()
            self.botton_comenzar_juego.setEnabled(True)
        else:
            self.timer1 = time()
            self.timer_crea_flecha = QTimer(self)
            self.timer_crea_flecha.setInterval(self.nuevo_paso)
            self.timer_crea_flecha.timeout.connect(self.creador_de_flecha)
            self.botton_pausa.setEnabled(True)
            self.flecha = []
            self.botton_comenzar_juego.setEnabled(False)
            self.cancion_box.setEnabled(False)
            self.dificultad_box.setEnabled(False)
            self.timer_crea_flecha.start()
        
    def creador_de_flecha(self):
        N = randint(1,self.combinacion)
        img_f = []
        for i in range(0,N):
            ff = Info_Flechas()
            while ff in img_f:
                ff = Info_Flechas()
            self.pasos_totales += 1
            self.pasos_terminados += 1
            self.lista_finfo = ff.flecha_info()
            nueva_flecha = Flecha_juego(self, self.width(), self.height(), self.lista_finfo[3], 
            self.lista_finfo[2], self.pausa_bool, self.lista_finfo[1], self.velocidad)
            nueva_flecha.actualizar.connect(self.actualizar_label)
            nueva_flecha.senal_flechas_en_y.connect(self.flecha_y)
            nueva_flecha.senal_flechas_no_y.connect(self.flecha_y_no)
            self.flecha.append(nueva_flecha)
            img_f.append(ff)
        img_f = []
        self.timer2 = time()
        self.player.play()
        #Combo 
        self.dinero_player.setText(f"Tienes {self.dinero} $")
        self.mayor_combo_obtenido.setText("Mayor Combo Obtenido: " + str(self.puntos_combo_total))
        self.combo_actual.setText("Combo Actual: " + str(self.puntos_combo))
        # progress bar
        self.bar_time = ((self.timer2 - self.timer1)/self.duracion_partida) * 100
        if self.bar_time >= 98.5:
            self.bar_time = 100
        self.progreso_de_cancion.setValue(self.bar_time)
        aprob = (self.pasos_correctos - self.pasos_incorrecto)
        self.porcentaje_aprobacion = (aprob/self.pasos_totales) * 100
        self.progreso_de_aprobacion.setValue(self.porcentaje_aprobacion)
        #Tiempo
        if self.timer2 - self.timer1 >= self.duracion_partida:
            self.timer_crea_flecha.stop()
            self.puntaje_acumulados += self.puntos_flechas
            QTimer.singleShot(6000,self.puntaje)
                                         
    def actualizar_label(self, label, x, y):
        label.move(x, y)
    def flecha_y(self, label, tipo_f, x):
        self.pasos_terminados -= 1
        self.listaf = [tipo_f, x, label]
        self.lista_y.append(self.listaf)
    def flecha_y_no(self, label, tipo_f, x):
        self.lista_y.pop(0)
    def aprobar_a(self, lista):
        self.una_flecha = 0
        for i in self.lista_y:
            if i[1] == 30:
                i[2].hide()
                self.boom_left.show()
                self.una_flecha += 1 
                self.pasos_correctos += 1
                self.puntos_combo += 1
                if i[0] == "_6" or i[0] == "_8":
                    self.puntos_flechas += 1
                elif i[0] == "_1":
                    self.puntos_flechas += 2
                elif i[0] == "_2":
                    self.puntos_flechas += 10
        if self.una_flecha == 0:
            self.puntos_combo = 0 
            self.pasos_incorrecto += 1   
        if self.puntos_combo > self.puntos_combo_total:
                self.puntos_combo_total = self.puntos_combo      
    def aprobar_w(self, lista):
        self.una_flecha = 0
        for i in self.lista_y:
            if i[1] == 110:
                i[2].hide()
                self.boom_up.show()
                self.una_flecha += 1 
                self.pasos_correctos += 1
                self.puntos_combo += 1
                if i[0] == "_6" or i[0] == "_8":
                    self.puntos_flechas += 1
                elif i[0] == "_1":
                    self.puntos_flechas += 2
                elif i[0] == "_2":
                    self.puntos_flechas += 10
        if self.una_flecha == 0:
            self.puntos_combo = 0 
            self.pasos_incorrecto += 1
        if self.puntos_combo > self.puntos_combo_total:
                self.puntos_combo_total = self.puntos_combo
    def aprobar_d(self, lista):
        self.una_flecha = 0
        for i in self.lista_y:
            if i[1] == 190:
                i[2].hide()
                self.boom_right.show()
                self.una_flecha += 1 
                self.pasos_correctos += 1
                self.puntos_combo += 1
                if i[0] == "_6" or i[0] == "_8":
                    self.puntos_flechas += 1
                elif i[0] == "_1":
                    self.puntos_flechas += 2
                elif i[0] == "_2":
                    self.puntos_flechas += 10
        if self.una_flecha == 0:
            self.puntos_combo = 0 
            self.pasos_incorrecto += 1
        if self.puntos_combo > self.puntos_combo_total:
                self.puntos_combo_total = self.puntos_combo
    def aprobar_s(self, lista):
        self.una_flecha = 0
        for i in self.lista_y:
            if i[1] == 270:
                i[2].hide()
                self.boom_down.show()
                self.una_flecha += 1 
                self.pasos_correctos += 1
                self.puntos_combo += 1
                if i[0] == "_6" or i[0] == "_8":
                    self.puntos_flechas += 1
                elif i[0] == "_1":
                    self.puntos_flechas += 2
                elif i[0] == "_2":
                    self.puntos_flechas += 10
        if self.una_flecha == 0:
            self.puntos_combo = 0 
            self.pasos_incorrecto += 1
        if self.puntos_combo > self.puntos_combo_total:
                self.puntos_combo_total = self.puntos_combo
    def dificultad(self):
        self.texto_dificultad = self.dificultad_box.currentText()
        if self.texto_dificultad == "Principiante":
            self.duracion_partida = 30
            self.nuevo_paso = 1000
            self.combinacion = 1
            self.aprobacion = 30
        elif self.texto_dificultad == "Aficionados":
            self.duracion_partida = 45
            self.nuevo_paso = 750
            self.combinacion = 2
            self.aprobacion = 50
        elif self.texto_dificultad == "Maestro Cumbia":
            self.duracion_partida = 60
            self.nuevo_paso = 500
            self.combinacion = 3
            self.aprobacion = 70
    def pausa(self):
        if self.pausa_bool == False:
            self.pausa_bool = True
            self.timer_crea_flecha.stop()
            self.player.pause()
        elif self.pausa_bool == True:
            self.timer_crea_flecha.start()
            self.pausa_bool = False
            self.player.play()   
    def cancion(self):
        self.texto_cancion = self.cancion_box.currentText()
        if self.texto_cancion == "Cancion 2":
            self.player = QMediaPlayer()
            sound = QMediaContent(QUrl.fromLocalFile(PATH_CANCION2))
            self.player.setMedia(sound)
            self.player.setVolume(1000)
        elif self.texto_cancion == "Cancion 1":
            self.player = QMediaPlayer()
            sound = QMediaContent(QUrl.fromLocalFile(PATH_CANCION1))
            self.player.setMedia(sound)
            self.player.setVolume(1000)
    def resumen(self):
        prob = (self.pasos_correctos - self.pasos_incorrecto)
        self.porcentaje_aprobacion = (prob/self.pasos_totales) * 100
        if self.aprobacion > self.aprobacion_final:
            self.senal_resumen.emit(self.nombre_jugador, "False", self.puntaje_acumulados,
            self.puntaje_ronda, self.puntos_combo_total, self.puntos_flechas, 
            self.porcentaje_aprobacion, self.dinero, self.nivel_ronda)
            self.close()
        else: 
            self.nivel_ronda += 1
            self.senal_resumen.emit(self.nombre_jugador, "True", self.puntaje_acumulados,
            self.puntaje_ronda, self.puntos_combo_total, self.puntos_flechas, 
            self.porcentaje_aprobacion, self.dinero, self.nivel_ronda)
            self.close()
    def puntaje(self):
        prob = (self.pasos_correctos - self.pasos_incorrecto)
        self.aprobacion_final = ( prob/self.pasos_totales)*100
        self.puntaje_ronda = (self.puntos_combo_total) * self.puntos_flechas * self.puntos_f
        self.dinero += self.puntaje_ronda
        self.puntaje_acumulados += self.puntaje_ronda
        self.resumen()
        self.player.stop()
### solo pre ronda
    def trampa(self):
        if len(self.trampa1) == 3 and self.trampa1[0] == "M" and self.trampa1[1] == "O":
            if self.trampa1[2] == "N":
                self.dinero += self.dinero_trampa
        elif len(self.trampa1) == 3 and self.trampa1[0] == "N":
            if self.trampa1[1] == "I" and self.trampa1[2] == "V":
                self.timer_crea_flecha.stop()
                QTimer.singleShot(4000,self.puntaje)
        else: 
            self.trampa1 = []

    def nombre_usurario (self, nombre):
        self.puntaje_acumulados = 0
        self.botton_pausa.setEnabled(False)
        self.flecha = []
        self.botton_comenzar_juego.setEnabled(True)
        self.cancion_box.setEnabled(True)
        self.dificultad_box.setEnabled(True)
        self.puntos_combo_total = 0
        self.puntos_combo = 0
        self.puntos_flechas = 0
        self.pasos_correctos = 0
        self.pasos_incorrecto = 0
        self.pasos_totales = 1
        self.nivel_ronda = 0 
        self.show()
        self.nombre_jugador = nombre
    def boton_salida(self):
        self.puntaje()
        self.timer_crea_flecha.stop()
        self.senal_ventanai.emit()      
        final =(self.puntaje_ronda + self.puntaje_acumulados)  
        with open(PATH_RANKING, "a+") as puntajes:
            puntajes.write(f"{self.nombre_jugador}  {str(final)} \n")
            puntajes.close()
        self.player.stop()
        QTimer.singleShot(4000,self.close_game)
    def close_game(self):
        self.close()

