import threading
from PyQt5.QtGui import QImage,QColor

class ThreadBW (threading.Thread):
    
    def __init__(self,image : QImage,callback):
        threading.Thread.__init__(self)
        self.callback = callback
        self.image = image
      
    def run(self):
        image_height = self.image.height()
        image_width = self.image.width()

        for h in range(image_height):
            for w in range(image_width):
                red = self.image.pixelColor(w,h).red()
                green = self.image.pixelColor(w,h).green()
                blue = self.image.pixelColor(w,h).blue()

                pixel = self.convertRGBToBlackAndWhite(red,green,blue)
                self.image.setPixelColor(w,h,QColor.fromRgb(pixel,pixel,pixel))
            
        self.callback(self.image)
    
    def convertRGBToBlackAndWhite(self, r : int,g : int, b : int):
        colorInt = (r + g + b)/3
        if(colorInt >=128):
            return 255
        else:
            return 0


class ThreadGray (threading.Thread):

    # Considerando o modelo YUV para iluminância 
    # Wr = 0.299
    # Wg = 0.587
    # Wb = 0.114

    def __init__(self,image : QImage,callback):
        threading.Thread.__init__(self)
        self.callback = callback
        self.image = image
      
    def run(self):
        image_height = self.image.width()
        image_width = self.image.height()

        for h in range(image_height):
            for w in range(image_width):
                red = self.image.pixelColor(w,h).red()
                green = self.image.pixelColor(w,h).green()
                blue = self.image.pixelColor(w,h).blue()

                pixel = self.convertRGBToGray(red,green,blue)
                self.image.setPixelColor(w,h,QColor.fromRgb(pixel,pixel,pixel))

            self.callback(self.image)
    
    def convertRGBToGray(self,r : int,g : int, b : int):
        colorInt = (0.299 * r + 0.587 * g + 0.114 * b)/3
        return colorInt