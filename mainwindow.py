import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from pdi import *

class MainWindow(QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        uic.loadUi("mainwindow.ui",self)
        preloadImage = QPixmap("./yoshi.png")
        

        imageBW = convertToBlackAndWhite(preloadImage.toImage())
        loadImage = QPixmap.fromImage(imageBW)

        print("Altura: " + str(preloadImage.height()))
        print("Largura: " +  str(preloadImage.width()))
        self.image.setPixmap(loadImage)
        self.show()


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    main = MainWindow()
    qt.exec()