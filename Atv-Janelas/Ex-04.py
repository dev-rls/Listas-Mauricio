from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys

class MeuNome(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nome")
        self.setGeometry(200, 100, 400, 300)  # x, y, largura, altura

        # Criando um layout vertical
        layout = QVBoxLayout()

        # Adicionando o texto
        label = QLabel("Raquel Santos", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(label)

        # Adicionando a imagem
        image_label = QLabel(self)
        pixmap = QPixmap(r"C:\Users\raque\Downloads\img_eu.jpeg")  # Usando string bruta
        if not pixmap.isNull():
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(image_label)

        # Adicionando o botão Sair
        sair_button = QPushButton("Sair", self)
        sair_button.clicked.connect(self.close)
        layout.addWidget(sair_button)

        # Criando um widget de contêiner e definindo o layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = MeuNome()
    Window.show()

    sys.exit(App.exec())
