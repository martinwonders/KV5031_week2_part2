import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QLabel, QPushButton, QVBoxLayout


class FormWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Enter your name and age:")
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_name)

        # layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.nameEdit)
        layout.addWidget(self.ageEdit)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def submit_name(self):
        name = self.nameEdit.text()
        self.label.setText(f"Hello {name}, your age is {self.ageEdit.text()}")


app = QApplication(sys.argv)
window = FormWindow()
window.show()
sys.exit(app.exec())
