import requests
from lxml import etree
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

def get_list(url):
    root_url = url

    tagre_url = "{}/tupian/list-%E6%B8%85%E7%BA%AF%E5%94%AF%E7%BE%8E-1.html".format(root_url)

    bro = requests.session()
    text = bro.get(tagre_url).text
    tree = etree.HTML(text)
    url_list = tree.xpath("//div[@id='tpl-img-content']/li/a/@href")
    ls = []
    for i in range(20):
        ls.append(root_url + url_list[i])
    return ls

def detail(url):
    bro =webdriver.Chrome()
    bro.get(url)
    WebDriverWait(bro,10,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,"videopic")))
    ls=bro.find_elements(by=By.CLASS_NAME,value="videopic")

    for item in ls:
        item.click()
        time.sleep(0.5)
        txt=item.get_property("src")
        name=item.get_property("title")
        file=open("{}.txt".format(name),'w')
        file.write(txt)
        file.close()
        getpic(name)


def getpic(name):
    path=r"D:\learn\picture\\"
    f=open(name+".txt","r")
    txt = f.read().split(',')[-1]
    f.close()
    imgdata = base64.b64decode(txt)
    file = open(r"{}.jpg".format(path+name), 'wb')
    file.write(imgdata)
    file.close()
    os.remove(name+".txt")


if __name__ == '__main__':
    #ls = get_list("https://www.69fcy.com")
    url="https://www.95531d0bd91f.com/tupian/194358.html"
    detail(url)
