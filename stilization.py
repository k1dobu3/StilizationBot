from PIL import Image, ImageFilter
import sys


def pict_rotate(photo_pathname):
    try:
        user_photo = Image.open(f'{photo_pathname}')
    except IOError:
        pass

    user_rotatephoto = user_photo.rotate(180)
    user_rotatephoto.save(f"{photo_pathname}")
    return True


def pict_mohohrom(photo_pathname):
    try:
        user_photo = Image.open(f'{photo_pathname}')
    except IOError:
        pass

    user_rotatephoto = user_photo.convert("L")
    user_rotatephoto.save(f"{photo_pathname}")
    return True


def pict_contour(photo_pathname):
    try:
        user_photo = Image.open(f'{photo_pathname}')
    except IOError:
        pass

    user_rotatephoto = user_photo.filter(ImageFilter.CONTOUR)
    user_rotatephoto.save(f"{photo_pathname}")
    return True


def pict_watermark():
    try:
        user_photo = Image.open('assets/menu.png')
        foreground = Image.open("test2.jpg")
    except IOError:
        pass

    #user_rotatephoto = user_photo.paste(foreground, (0, 0), foreground)
    #user_rotatephoto.show()

    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)


if __name__ == "__main__":
    pict_rotate()