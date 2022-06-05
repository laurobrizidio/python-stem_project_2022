from PyQt5.QtGui import QImage,QColor

def convertToBlackAndWhite(image : QImage):
    image_height = image.height()
    image_width = image.width()

    POSITION_X = 500
    POSITION_Y = 500

    print("Color RED: {} - GREEN: {} - BLUE: {}",
    image.pixelColor(POSITION_X,POSITION_Y).red(),
    image.pixelColor(POSITION_X,POSITION_Y).green(),
    image.pixelColor(POSITION_X,POSITION_Y).blue())

    for h in range(image_height):
        for w in range(image_width):
            red = image.pixelColor(w,h).red()
            green = image.pixelColor(w,h).green()
            blue = image.pixelColor(w,h).blue()


            pixel = convertRGBToBlackAndWhite(red,green,blue)
            image.setPixelColor(w,h,QColor.fromRgb(pixel,pixel,pixel))

    return image


def convertRGBToBlackAndWhite(r : int,g : int, b : int):
    colorInt = (r + g + b)/3
    if(colorInt >=128):
        return 255
    else:
        return 0