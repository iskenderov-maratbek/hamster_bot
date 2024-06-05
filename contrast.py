from PIL import Image

    # image = cv2.imread(fi lename)
    # os.remove(filename) 

    # # Увеличение контрастности
    # alpha = 1.5  # Коэффициент контрастности (можно настроить по вашему усмотрению)
    # beta = -150     # Смещение яркости

    # adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # # Сохранение измененного изображения
    # cv2.imwrite(f'++{filename}', adjusted)


def imgCorrect(filename):
    img = Image.open(filename)
    img = img.convert("RGB")
    datas = img.getdata()
    new_image_data = []
    start = 220
    end = 255 
    for item in datas:
        if not(start <= item[0] <= end and start <= item[1] <= end and start <= item[2] <= end):
            new_image_data.append((end,end,end)) 
        else:
            new_image_data.append((0, 0, 0))

    img.putdata(new_image_data)
    img.save(filename)