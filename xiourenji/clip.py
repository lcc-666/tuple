from PIL import Image
from concurrent.futures import ThreadPoolExecutor,as_completed
import os
import shutil
import time
import tqdm

def file_list(path):
    ls = os.listdir(path)
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_list = []
        results = []
        for i in ls:
            future = executor.submit(thread, i)
            future_list.append(future)
        for task in tqdm.tqdm(as_completed(future_list), total=len(future_list)):
            results.append(task.result())

def thread(i):
    path = r"D:\learn\picture\quan"
    new_path = path + "\\" + i
    edit(new_path)
    try:
        shutil.move(new_path, r"D:\learn\picture\jianji\\" + i)
    except FileNotFoundError:
        pass




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
