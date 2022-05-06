import base64
import os
import time
import tqdm
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
        for i in range(3, 11):
            ls = self.get_list(i)
            for item in ls:
                print("第{}页第{}个".format(i, ls.index(item) + 1), item)
                self.detail(item)
            time.sleep(5)

    def get_list(self, page):
        root_url = self.root_url
        tagre_url = "{}/tupian/list-%E6%B8%85%E7%BA%AF%E5%94%AF%E7%BE%8E-{}.html".format(root_url, page)
        bro = requests.session()
        text = bro.get(tagre_url).text
        tree = etree.HTML(text)
        url_list = tree.xpath("//div[@id='tpl-img-content']/li/a/@href")
        name_list = tree.xpath("//div[@id='tpl-img-content']/li/a/@title")
        name_list1 = list(set(name_list))
        name_list1.sort(key=name_list.index)
        url_list2 = list(set(url_list))
        url_list2.sort(key=url_list.index)
        get_dict = {}
        for i in range(20):
            get_dict[name_list1[i]] = root_url + url_list2[i]

        dict = {'SF-No.178 Eri Kitagawa': 15, 'SF-No.189 Azusa Takagi(高木梓)': 15, 'Tifa succubus': 19, '人美身材靓呢': 19,
                '写真集': 19, '可爱女仆MargaritaE.part2 ': 17, '嫩滑的奶子哦': 19, '彩虹内衣喜欢吗': 19, '性感又清新的大学生唐佳怡可爱女仆装和性感兔女郎写真': 19,
                '气质女神': 19, '能顶到你屏幕的大奶呢': 16, '都市丽人王馨瑶黑色短裙加黑丝美腿性感写真 ': 29, '韩国人气模特_ 孙允珠_ 高清套图 ': 30}
        ls = []
        for i in get_dict:
            if i in dict:
                ls.append(get_dict[i])
        return ls

    def detail(self, url):
        bro = self.bro
        bro.get(url)
        try:
            WebDriverWait(bro, 10, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "videopic")))
        except:
            print("iojioiojjio")
            bro.get(url)
            WebDriverWait(bro, 10, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "videopic")))

        ls = bro.find_elements(by=By.CLASS_NAME, value="videopic")

        for item in tqdm.tqdm(ls):
            item.click()
            time.sleep(0.5)
            txt = item.get_property("src")
            name = item.get_property("title")
            file = open("{}.txt".format(name), 'w')
            file.write(txt)
            file.close()
            try:
                self.getpic(name)
            except:
                time.sleep(3)
                txt = item.get_property("src")
                name = item.get_property("title")
                file = open("{}.txt".format(name), 'w')
                file.write(txt)
                file.close()

    def getpic(self, name):
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
