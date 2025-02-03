from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys

class MeuNome(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nome")
        self.setGeometry(100, 100, 200, 100)  # x, y, largura, altura

        layout = QVBoxLayout()

        label = QLabel("Raquel Santos", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(label)

        # Adicionando a imagem
        image_label = QLabel(self)
        pixmap = QPixmap(r"C:\Users\raque\Downloads\img_eu.jpeg")
        if not pixmap.isNull():
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = MeuNome()
    Window.show()

    sys.exit(App.exec())                        