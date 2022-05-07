from PIL import Image, UnidentifiedImageError
import os
import shutil

def file_list(path):
    ls = os.listdir(path)
    for i in ls:
        new_path = path + "\\" + i
        edit(new_path)
        shutil.move(new_path,r"D:\learn\picture\jianji\\"+i)


def edit(path):
    try:
        img = Image.open(path)
        left = 0
        upper = 0
        right = img.width
        low = img.height - 60
        box = (left, upper, right, low)
        roi = img.crop(box)
        roi.save(path)
    except:
        print(path)
        os.remove(path)


if __name__ == '__main__':
    path = r"D:\learn\picture\quan"
    file_list(path)
