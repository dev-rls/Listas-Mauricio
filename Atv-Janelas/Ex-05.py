import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

def on_button_click():
    button.hide()
    
    new_button = QPushButton('Outro botão')
    new_button.clicked.connect(on_new_button_click)  

    new_image_label = QLabel()
    new_pixmap = QPixmap(r'C:\Users\RaquelSantos\Documents\teste\img2.jfif')  
    if not new_pixmap.isNull():
        new_image_label.setPixmap(new_pixmap)
    else:
        new_image_label.setText('Nova imagem não encontrada')

    new_image_label.setAlignment(Qt.AlignCenter)

    layout.addWidget(new_image_label)
    layout.addWidget(new_button)

    window.adjustSize()

def on_new_button_click():
    print("Novo botão clicado!")

def main():
    global window, button, layout

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Hello World')

    layout = QVBoxLayout()

    name_label = QLabel('Raquel')
    name_label.setAlignment(Qt.AlignCenter)

    image_label = QLabel()
    pixmap = QPixmap(r'C:\Users\RaquelSantos\Documents\teste\img1.jfif')
    if not pixmap.isNull():
        image_label.setPixmap(pixmap)
    else:
        image_label.setText('Imagem não encontrada')

    image_label.setAlignment(Qt.AlignCenter)

    button = QPushButton('Clique aqui')
    button.clicked.connect(on_button_click)

    layout.addWidget(name_label)
    layout.addWidget(image_label)
    layout.addWidget(button)

    window.setLayout(layout)

    window.resize(400, 500)

    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
 