import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QGridLayout,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Modern Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Set app theme
        self.set_theme()

        # Initialize UI
        self.init_ui()

    def set_theme(self):
        # Set a modern dark theme
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        QApplication.setPalette(dark_palette)

    def init_ui(self):
        # Main widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Display for calculator
        self.display = QLineEdit(self)
        self.display.setFont(QFont("Arial", 20))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(
            """
            QLineEdit {
                background-color: #2D2D2D;
                color: #FFFFFF;
                border: 1px solid #555555;
                padding: 10px;
            }
            """
        )
        main_layout.addWidget(self.display)

        # Button layout
        buttons_layout = QGridLayout()

        # Button labels
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C"
        ]

        # Add buttons to the grid
        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text, self)
            button.setFont(QFont("Arial", 16))
            button.setStyleSheet(
                """
                QPushButton {
                    background-color: #42A2D5;
                    color: #FFFFFF;
                    border: none;
                    border-radius: 5px;
                    padding: 15px;
                }
                QPushButton:hover {
                    background-color: #3282B5;
                }
                """
            )
            button.clicked.connect(self.on_button_click)
            buttons_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        main_layout.addLayout(buttons_layout)

    def on_button_click(self):
        # Handle button clicks
        button = self.sender()
        text = button.text()

        if text == "=":
            # Evaluate the expression
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif text == "C":
            # Clear the display
            self.display.clear()
        else:
            # Append the button text to the display
            self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
