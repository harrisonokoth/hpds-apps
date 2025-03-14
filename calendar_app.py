import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QCalendarWidget,
    QTextEdit,
)
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QFont, QColor, QPalette


class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Modern Calendar App")
        self.setGeometry(100, 100, 800, 600)

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

        # Calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setStyleSheet(
            """
            QCalendarWidget QWidget {
                background-color: #2D2D2D;
                color: #FFFFFF;
            }
            QCalendarWidget QToolButton {
                font-size: 16px;
                color: #FFFFFF;
            }
            QCalendarWidget QMenu {
                background-color: #2D2D2D;
                color: #FFFFFF;
            }
            """
        )
        main_layout.addWidget(self.calendar)

        # Selected date label
        self.date_label = QLabel("Selected Date: ", self)
        self.date_label.setFont(QFont("Arial", 14))
        self.date_label.setStyleSheet("color: #FFFFFF;")
        main_layout.addWidget(self.date_label)

        # Text edit for notes
        self.notes_edit = QTextEdit(self)
        self.notes_edit.setPlaceholderText("Add notes for the selected date...")
        self.notes_edit.setStyleSheet(
            """
            QTextEdit {
                background-color: #2D2D2D;
                color: #FFFFFF;
                font-size: 14px;
                border: 1px solid #555555;
                padding: 10px;
            }
            """
        )
        main_layout.addWidget(self.notes_edit)

        # Button to save notes
        save_button = QPushButton("Save Notes", self)
        save_button.setStyleSheet(
            """
            QPushButton {
                background-color: #42A2D5;
                color: #FFFFFF;
                font-size: 14px;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3282B5;
            }
            """
        )
        save_button.clicked.connect(self.save_notes)
        main_layout.addWidget(save_button)

        # Connect calendar selection to update label
        self.calendar.selectionChanged.connect(self.update_date_label)

        # Initialize selected date
        self.update_date_label()

    def update_date_label(self):
        # Update the label with the selected date
        selected_date = self.calendar.selectedDate().toString(Qt.ISODate)
        self.date_label.setText(f"Selected Date: {selected_date}")

    def save_notes(self):
        # Save notes for the selected date
        selected_date = self.calendar.selectedDate().toString(Qt.ISODate)
        notes = self.notes_edit.toPlainText()
        with open("calendar_notes.txt", "a") as file:
            file.write(f"{selected_date}: {notes}\n")
        self.notes_edit.clear()
        self.date_label.setText(f"Notes saved for {selected_date}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec_())