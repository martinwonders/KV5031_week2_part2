import sys
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QApplication


class LayoutWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.label = QLabel("Yout name:")
        self.name_edit = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit)
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear)

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.clear_button)

        # Vertical layout for label, input and buttons
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.name_edit)
        main_layout.addLayout(button_layout)

        # Set the Layout
        self.setLayout(main_layout)

    def submit(self):
        name = self.name_edit.text()
        self.label.setText(f"Hello {name}")

    def clear(self):
        self.name_edit.clear()
        self.label.setText("")


app = QApplication(sys.argv)
window = LayoutWindow()
window.show()
sys.exit(app.exec())

