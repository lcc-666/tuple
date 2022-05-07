from PIL import Image, UnidentifiedImageError
import os


def file_list(path):
    ls=os.listdir(path)
    for i in ls:
        a=i.split(".")[-1]
        if a=="jpg":
            new_path=path+r"\\"+i
            edit(new_path)


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
    # path = r"D:\learn\picture\泳衣遮挡不住的好身材2.jpg"
    # edit(path)
    path = r"D:\learn\picture\quan"
    file_list(path)
