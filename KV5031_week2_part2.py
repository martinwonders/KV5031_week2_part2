import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QDialog


class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()

        #Create Label and Button
        self.label = QLabel("<b><font color='red'>Martin A Wonders!</font></b>")
        self.button = QPushButton("Change the label!")

        #Connect button click to the slot (method)
        self.button.clicked.connect(self.on_button_clicked)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.setWindowTitle("Hello World App!")
        self.resize(300, 100)

    # Slot (method) for handling button click
    def on_button_clicked(self):
        print("Clicked")
        self.label.setText("<b><font color='blue'>You clicked the button</font></b>")
        self.show_dialog()

    def show_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog Box")

        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(QLabel("This is a custom dialog box!"))

        dialog.setLayout(dialog_layout)
        dialog.exec()

app = QApplication(sys.argv)
window = HelloWorldWindow()
window.show()
sys.exit(app.exec())
