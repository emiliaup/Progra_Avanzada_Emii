import PyQt5.QtGui as gui 
import PyQt5.QtCore as core
from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal
from codigo_ventanar import MainWindow2
from ventana_de_errores import Ventana_error_nombre
from parametros import PATH_VENTANA_RESUMEN, PATH_RANKING

window_name, base_class = uic.loadUiType(PATH_VENTANA_RESUMEN)


class Resumen(window_name, base_class):
    senal_ventana_i = pyqtSignal()
    senal_ventanag = pyqtSignal(str,int,int,int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        self.pagina_juego_botton.clicked.connect(self.pagina_juego)
        self.pagina_inicio_botton.clicked.connect(self.pagina_inicio)
        
    
    def resumen_total(self, nombre, aprobacion, puntaje_acumulado, 
    puntaje_ronda, max_combo, pasos_fallidos, porcentaje_aprobacion, dinero,
    nivel):
        self.nombre_pinguino = nombre
        self.puntaje_acumulado = puntaje_acumulado
        self.puntaje_ronda = puntaje_ronda
        self.max_combo = max_combo
        self.pasos_fallidos = pasos_fallidos
        self.porcentaje_aprobacion = porcentaje_aprobacion
        self.bool_aprobacion = aprobacion
        self.dinero = dinero
        self.nivel = nivel
        texto1 = f"Puntaje acomulado: {self.puntaje_acumulado}, \n"
        texto2 = f" Puntaje de ronda: {self.puntaje_ronda}, \n"
        texto3 = f"Max Combo obtenido esta ronda: {self.max_combo}, \n"
        texto4 = f" Porcentaje de aprobcion: {self.porcentaje_aprobacion}, \n"
        texto = texto1 + texto2 + texto3 + texto4
        self.mayor_combo_puntos_txt.setText(texto)
        self.name_text.setText(self.nombre_pinguino)
    

        if self.bool_aprobacion == "True":
            self.aprobado_txt.setVisible(True)
            self.no_aprobado_txt.setVisible(False)
            self.pagina_juego_botton.setEnabled(True)
            self.ranking_guardar()
            self.show()
        elif self.bool_aprobacion == "False":
            self.aprobado_txt.setVisible(False)
            self.no_aprobado_txt.setVisible(True)
            self.pagina_juego_botton.setEnabled(False)
            self.ranking_guardar()
            self.show()
                
    def ranking_guardar(self):
        with open(PATH_RANKING, "a+") as puntajes:
            puntajes.write(f"{self.nombre_pinguino}  {str(self.puntaje_acumulado)} \n")
            puntajes.close()

    def pagina_inicio(self):
        self.senal_ventana_i.emit()
        self.close()

    def pagina_juego(self):
        self.senal_ventanag.emit(self.nombre_pinguino, self.puntaje_acumulado, 
        self.dinero, self.nivel)
        self.close()
