import base64
import os
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class down:
    def __init__(self, url):
        self.bro = webdriver.Chrome()
        self.root_url = url
        ls = self.get_list()
        for item in ls:
            print(item)
            self.detail(item)

    def get_list(self):
        root_url = self.root_url
        tagre_url = "{}/tupian/list-%E6%B8%85%E7%BA%AF%E5%94%AF%E7%BE%8E-1.html".format(root_url)
        bro = requests.session()
        text = bro.get(tagre_url).text
        tree = etree.HTML(text)
        url_list = tree.xpath("//div[@id='tpl-img-content']/li/a/@href")
        url_list=url_list
        l2=list(set(url_list))
        l2.sort(key=url_list.index)

        ls = []
        for i in range(20):
            ls.append(root_url + l2[i])

        return ls

    def detail(self,url):
        bro=self.bro
        bro.get(url)
        WebDriverWait(bro, 10, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "videopic")))
        ls = bro.find_elements(by=By.CLASS_NAME, value="videopic")

        for item in ls:
            item.click()
            time.sleep(0.5)
            txt = item.get_property("src")
            name = item.get_property("title")
            file = open("{}.txt".format(name), 'w')
            file.write(txt)
            file.close()
            self.getpic(name)

    def getpic(self,name):
        path = r"D:\learn\picture\\"
        f = open(name + ".txt", "r")
        txt = f.read().split(',')[-1]
        f.close()
        imgdata = base64.b64decode(txt)
        file = open(r"{}.jpg".format(path + name), 'wb')
        file.write(imgdata)
        file.close()
        os.remove(name + ".txt")


if __name__ == '__main__':
    url = "https://www.95531d0bd91f.com/"
    down(url)
