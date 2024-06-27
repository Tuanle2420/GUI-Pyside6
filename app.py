from Demo_ui import Ui_DempApp
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyApp(QMainWindow, Ui_DempApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Demo App')
        
        self.stackedWidget.setCurrentIndex(0)
        
        self.dashboard_btn.clicked.connect(self.switch_to_dashboardPage)
        self.data_btn.clicked.connect(self.switch_to_dataPage)
        self.pre_data_btn.clicked.connect(self.switch_to_prePage)
        self.filter_btn.clicked.connect(self.switch_to_filterPage)
        self.defi_btn.clicked.connect(self.switch_to_defiPage)
        self.hot_data.clicked.connect(self.switch_to_hotPage)
        
    
    
    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_dataPage(self):
        self.stackedWidget.setCurrentIndex(5)
        
    def switch_to_prePage(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def switch_to_filterPage(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def switch_to_defiPage(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def switch_to_hotPage(self):
        self.stackedWidget.setCurrentIndex(4)
        
    