from msilib.schema import ComboBox
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from pdi import *

class MainWindow(QMainWindow):

    

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        uic.loadUi("mainwindow.ui",self)

        self.R_value = None
        self.G_value = None
        self.B_value = None

        self.lbl_slider_value_R.setText(str(self.slider_red.value()))
        self.lbl_slider_value_G.setText(str(self.slider_green.value()))
        self.lbl_slider_value_B.setText(str(self.slider_blue.value()))

        # Observer
        self.slider_red.valueChanged.connect(self.value_change_R)

        self.slider_green.valueChanged.connect(self.value_change_G)

        self.slider_blue.valueChanged.connect(self.value_change_B)

        #  Set Image

        self.preloadImage = QPixmap("./yoshi.png")
        self.image.setPixmap(self.preloadImage)


        self.button_click.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        print("Clicked")
        options = self.comboBox.currentIndex()

        print("Option: " + str(options)) 
        
        if(options == 0):
            self.image.setPixmap(self.preloadImage)

        elif(options == 1): 
            imageBW = convertToBlackAndWhite(self.preloadImage.toImage())
            loadImage = QPixmap.fromImage(imageBW)
            self.image.setPixmap(loadImage)
        
        elif(options == 2): 
            imageGray = convertToGrayScale(self.preloadImage.toImage())
            loadImage = QPixmap.fromImage(imageGray)
            self.image.setPixmap(loadImage)

        #elif(options == 3): 
            # A implementar

    def value_change_R(self):
        self.lbl_slider_value_R.setText(str(self.slider_red.value()))
        self.R_value = self.slider_red.value()
        
    def value_change_G(self):
        self.lbl_slider_value_G.setText(str(self.slider_green.value()))
        self.G_value = self.slider_green.value()
        
    def value_change_B(self):
        self.lbl_slider_value_B.setText(str(self.slider_blue.value()))
        self.B_value = self.slider_blue.value()

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    main = MainWindow()
    qt.exec()