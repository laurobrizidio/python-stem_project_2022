import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from mainwindow import Ui_MainWindow

class GUI_cont(QMainWindow,Ui_MainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.image.setPixmap(QPixmap("./yoshi.png"))




if __name__ == "__main__":
    qt = QApplication(sys.argv)
    view = GUI_cont()
    view.show()
    qt.exec()