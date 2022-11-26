from PIL import Image, ImageFilter
import sys


def pict_rotate():
    try:
        user_photo = Image.open('assets/menu.png')
    except IOError:
        pass

    user_rotatephoto = user_photo.rotate(180)
    user_rotatephoto.show()
    #return user_rotatephoto


def pict_mohohrom():
    try:
        user_photo = Image.open('assets/menu.png')
    except IOError:
        pass

    user_rotatephoto = user_photo.convert("L")
    user_rotatephoto.show()


def pict_contour():
    try:
        user_photo = Image.open('assets/menu.png')
    except IOError:
        pass

    user_rotatephoto = user_photo.filter(ImageFilter.CONTOUR)
    user_rotatephoto.show()


def pict_watermark():
    try:
        user_photo = Image.open('assets/menu.png')
        foreground = Image.open("test2.jpg")
    except IOError:
        pass

    user_rotatephoto = user_photo.paste(foreground, (0, 0), foreground)
    user_rotatephoto.show()



if __name__ == "__main__":
    pict_rotate()