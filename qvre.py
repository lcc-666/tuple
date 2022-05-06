import os
import shutil
path=r"D:\learn\picture"
ls = os.listdir(r"D:\learn\picture")
ls.remove('quan')
ls.sort()

windows = []
dict = {}

for i in ls:
    i = i[:-4]
    while i[-1].isnumeric() is True:
        i = i[:-1]
    windows.append(i)

for i in windows:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
# clearn=[]
# for i in dict.items():
#     if i[-1] == 20:
#         clearn.append(i[0])
#     if i[-1] == 40:
#         clearn.append(i[0])
# for i in clearn:
#     del dict[i]
#
# for a in ls:
#     i=a
#     i = i[:-4]
#     while i[-1].isnumeric() is True:
#         i = i[:-1]
#     if i in clearn:
#         old=r"D:\learn\picture"+"\\"+a
#         new=r"D:\learn\picture"+r"\quan\\"+a
#         shutil.move(old,new)




