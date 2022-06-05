from PyQt5.QtGui import QImage,QColor

def convertToBlackAndWhite(image : QImage):
    image_height = image.height()
    image_width = image.width()

    for h in range(image_height):
        for w in range(image_width):
            red = image.pixelColor(w,h).red()
            green = image.pixelColor(w,h).green()
            blue = image.pixelColor(w,h).blue()

            pixel = convertRGBToBlackAndWhite(red,green,blue)
            image.setPixelColor(w,h,QColor.fromRgb(pixel,pixel,pixel))

    return image


def convertToGrayScale(image : QImage):
    image_height = image.height()
    image_width = image.width()

    for h in range(image_height):
        for w in range(image_width):
            red = image.pixelColor(w,h).red()
            green = image.pixelColor(w,h).green()
            blue = image.pixelColor(w,h).blue()

            pixel = convertRGBToGray(red,green,blue)
            image.setPixelColor(w,h,QColor.fromRgb(pixel,pixel,pixel))

    return image

# Considerando o modelo YUV para iluminância 
    # Wr = 0.299
    # Wg = 0.587
    # Wb = 0.114

def convertRGBToGray(r : int,g : int, b : int):
    colorInt = (0.299 * r + 0.587 * g + 0.114 * b)/3
    return colorInt


def convertRGBToBlackAndWhite(r : int,g : int, b : int):
    colorInt = (r + g + b)/3
    if(colorInt >=128):
        return 255
    else:
        return 0