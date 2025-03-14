import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QColor, QPalette


class DigitalClockApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("HPDS Digital Clock")
        self.setGeometry(100, 100, 400, 200)

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
        layout = QVBoxLayout(central_widget)

        # Clock label
        self.clock_label = QLabel(self)
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.clock_label.setFont(QFont("Arial", 48))
        self.clock_label.setStyleSheet("color: #42A2D5;")
        layout.addWidget(self.clock_label)

        # HPDS label
        self.hpds_label = QLabel("HPDS", self)
        self.hpds_label.setAlignment(Qt.AlignCenter)
        self.hpds_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.hpds_label.setStyleSheet("color: #FFFFFF;")
        layout.addWidget(self.hpds_label)

        # Update the clock every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Initialize time
        self.update_time()

    def update_time(self):
        # Get the current time
        current_time = QTime.currentTime()
        display_text = current_time.toString("hh:mm:ss")

        # Update the clock label
        self.clock_label.setText(display_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DigitalClockApp()
    window.show()
    sys.exit(app.exec_())
