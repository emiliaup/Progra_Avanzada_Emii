from  PyQt5.QtWidgets import QApplication
import sys
from cliente import Cliente
from sala_espera import Sala_espera

app = QApplication([])

PORT = 3245
HOST = 'localhost'


cliente = Cliente(PORT, HOST)
window = Sala_espera()

sys.exit(app.exec_())