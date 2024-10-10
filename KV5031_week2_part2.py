import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QLabel, QPushButton, QVBoxLayout


class FormWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Enter your name:")
        self.lineEdit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_name)

        # layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def submit_name(self):
        name = self.lineEdit.text()
        self.label.setText(f"Hello {name}")


app = QApplication(sys.argv)
window = FormWindow()
window.show()
sys.exit(app.exec())
