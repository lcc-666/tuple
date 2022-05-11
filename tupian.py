import time
import tqdm
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from xiourenji.base64tojpg import getpic
from xiourenji.qvchong import deduplication


class down:
    def __init__(self, url):
        self.bro = webdriver.Chrome()
        self.bro.set_page_load_timeout(3)
        self.root_url = url
        self.new_url()
        for i in range(140, 150):
            ls = self.get_list(i)
            for item in ls:
                print("第{}页第{}个".format(i, ls.index(item) + 1), item)
                result = 0
                while result != 1:
                    try:
                        self.detail(item)
                        result = 1
                    except:
                        pass

    def new_url(self):
        options = Options()
        prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        bro = webdriver.Chrome(options=options)
        status = 0
        while status != 200:
            try:
                bro.get(self.root_url)
                status = 200
            except WebDriverException:
                bro.refresh()
                time.sleep(3)
        url = bro.find_element(by=By.CLASS_NAME, value="header_title")
        self.root_url = "https://" + url.text
        print("url更新")
        bro.close()

    def get_list(self, page):

        root_url = self.root_url
        tagre_url = "{}/tupian/list-%E6%B8%85%E7%BA%AF%E5%94%AF%E7%BE%8E-{}.html".format(root_url, page)
        options = Options()
        prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
        options.add_experimental_option("prefs", prefs)
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        bro = webdriver.Chrome(options=options)
        status = 0
        while status != 200:
            try:
                bro.get(tagre_url)
                status = 200
            except WebDriverException:
                bro.refresh()

        text = bro.page_source
        tree = etree.HTML(text)
        url_list = tree.xpath("//div[@id='tpl-img-content']/li/a/@href")
        l2 = deduplication(url_list)
        bro.close()
        ls = []
        print("列表获取")
        for i in range(20):
            ls.append(root_url + l2[i])
        return ls

    def detail(self, url):
        bro = self.bro
        stadus_code = 0
        while stadus_code != 200:
            try:
                bro.get(url)
            except TimeoutException:
                stadus_code = 200
                pass
            except WebDriverException:
                bro.refresh()

        status = False
        while status is not True:
            try:
                wait = WebDriverWait(bro, 3)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'content')))
                status = True
            except TimeoutException:
                bro.get(url)
        ls = bro.find_elements(by=By.CLASS_NAME, value="videopic")

        for item in tqdm.tqdm(ls):
            item.click()
            time.sleep(1)
            txt = item.get_property("src")
            name = item.get_property("title")
            file = open("{}.txt".format(name), 'w')
            file.write(txt)
            file.close()
            try:
                getpic(name)
            except:
                item.click()
                time.sleep(6)
                txt = item.get_property("src")
                name = item.get_property("title")
                file = open("{}.txt".format(name), 'w')
                file.write(txt)
                file.close()
                try:
                    getpic(name)
                except:
                    file = open("shao.txt", "a")
                    file.write(name + ":" + url + "\n")


if __name__ == '__main__':
    url = "https://www.95531d0bd91f.com/"
    down(url)
    # path = r"D:\learn\picture\quan"
    # file_list(path)
