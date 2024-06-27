from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from app import MyApp

program = QApplication(sys.argv)
window = MyApp()
window.show()
program.exec()