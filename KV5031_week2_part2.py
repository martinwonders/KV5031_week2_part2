import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Martin A Wonders!")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle("Hello World App!")
        self.resize(300, 100)

app = QApplication(sys.argv)
window = HelloWorldWindow()
window.show()
sys.exit(app.exec())
