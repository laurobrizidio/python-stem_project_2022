from PyQt5.QtGui import QImage,QColor
from threadpdi import ThreadBW, ThreadGray

def convertToBlackAndWhite(image : QImage,callback):
    ThreadBW(image,callback).start()


def convertToGrayScale(image : QImage,callback):
    ThreadGray(image,callback).start()