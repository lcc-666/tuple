from selenium import webdriver

from tupian import down
from xiourenji import qvchong


class dowlod(down):
    def __init__(self, url):
        self.bro = webdriver.Chrome()
        self.bro.set_page_load_timeout(3)
        self.root_url = url


f = open("shao.txt", 'r')
ls = f.readlines()

ls.reverse()
for i in range(len(ls)):
    ls[i] = ls[i].split("/")[-1].strip()
url = "https://www.95531d0bd91f.com/enter/index.html"
ls = qvchong.deduplication(ls)
s = dowlod(url)
s.new_url()
root=s.root_url+"/tupian/"
for i in ls:
    #print(root+i)
    s.detail(root + i)
