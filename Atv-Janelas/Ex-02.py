'''02. Faça um programa que abra uma janela com um texto com seu centralizado.'''

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt
import sys

class MeuNome(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nome")
        self.setGeometry(200, 100, 400, 200)  # x, y, largura, altura

        label = QLabel("Raquel Santos", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.setCentralWidget(label)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = MeuNome()
    Window.show()

    sys.exit(App.exec())
