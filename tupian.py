import time
import tqdm
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from xiourenji.base64tojpg import getpic


class down:
    def __init__(self, url):
        self.bro = webdriver.Chrome()
        self.root_url = url
        for i in range(13, 150):
            ls = self.get_list(i)
            for item in ls:
                print("第{}页第{}个".format(i, ls.index(item) + 1), item)
                self.detail(item)

    def get_list(self, page):
        root_url = self.root_url
        tagre_url = "{}/tupian/list-%E6%B8%85%E7%BA%AF%E5%94%AF%E7%BE%8E-{}.html".format(root_url, page)
        bro = requests.session()
        text = bro.get(tagre_url).text
        tree = etree.HTML(text)
        url_list = tree.xpath("//div[@id='tpl-img-content']/li/a/@href")
        url_list = url_list
        l2 = list(set(url_list))
        l2.sort(key=url_list.index)

        ls = []
        for i in range(20):
            ls.append(root_url + l2[i])
        return ls

    def detail(self, url):
        bro = self.bro
        bro.get(url)
        try:
            wait = WebDriverWait(bro, 3)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'content')))
        except TimeoutError:
            bro.get(url)
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
                getpic(name)
            except:
                item.click()
                time.sleep(3)
                txt = item.get_property("src")
                name = item.get_property("title")
                file = open("{}.txt".format(name), 'w')
                file.write(txt)
                file.close()
                getpic(name)


if __name__ == '__main__':
    url = "https://www.95531d0bd91f.com/"
    down(url)
