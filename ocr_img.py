import pytesseract
from PIL import Image


def ocr_my_img(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image, lang='eng')
    return text


def split_image(file_name):
    img = Image.open(file_name)
    width, height = img.size

    # Разделите изображение на две половины
    left_img = img.crop((0, 0, width//2, height))
    right_img = img.crop((width//2, 0, width, height))

    # Сохраните обе половины изображения
    left_img.save(f'left_{file_name}')
    right_img.save(f'right_{file_name}')
    return f'left_{file_name}', f'right_{file_name}'
# # Пример использования
# split_image('your_image.png')
