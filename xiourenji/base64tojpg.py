import base64
import os

"""
base64转jpg
需要提供图片名称
可选择提供路径
"""


def getpic(name, path=r"D:\learn\picture\quan\\"):
    f = open(name + ".txt", "r")
    txt = f.read().split(',')[-1]
    f.close()
    imgdata = base64.b64decode(txt)
    file = open(r"{}.jpg".format(path + name), 'wb')
    file.write(imgdata)
    file.close()
    os.remove(name + ".txt")

