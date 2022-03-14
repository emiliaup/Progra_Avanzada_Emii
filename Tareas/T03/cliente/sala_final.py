import sys
import random
import PyQt5.QtWidgets as widgets
import PyQt5.QtCore as core
from PyQt5 import uic
import json

with open('parametros.json') as file:
    data = json.load(file)
path_sala_final = data["PATH_SALA_FINAL"]

window_name, base_class = uic.loadUiType(path_sala_final)

class Sala_final(window_name, base_class):

    send_msg_signal = core.pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.perdio_jugador.hide()
        self.gano_jugador.hide()
    
    def salir(self, event):
        sys.exit()
 
    def send_msg_to_client(self):
        print(self.userInputWidget.toPlainText())
        data = {    
            "type"  :   "chat", \
            "username"  :   self.username, \
            "data"  :   self.userInputWidget.toPlainText() \
                }
        self.send_msg_signal.emit(data)
        self.userInputWidget.setPlainText('')

   
if __name__ == '__main__':
    app = widgets.QApplication([])
    window = Sala_final()
    sys.exit(app.exec_())
