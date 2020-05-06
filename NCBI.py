import requests
import random
from bs4 import BeautifulSoup
import time
import datetime
import re
import chardet
import urllib3

def getwebpage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    htmlpage = requests.get(url, headers=headers, verify=False,timeout=5)
    chardit = chardet.detect(htmlpage.content).get('encoding')
    if chardit == "Windows-1252":
        htmlpage.encoding = 'big5'
    if chardit == "Windows-1254":
        htmlpage.encoding = 'utf-8'
    if htmlpage.status_code != 200:
        print("invalid url", htmlpage.status_code)
        return None
    else:
        return htmlpage.text

site = "https://www.ncbi.nlm.nih.gov/gene/56606/?report=expression"

html = getwebpage(site)
if html != None:
    soup = BeautifulSoup(html, 'html.parser')
    urlitems = soup.find("div", class_="ui-ncbigrid-outer-div")   
    print(urlitems)
    if urlitems != None:
        st1 = urlitems.find("tbody")
        print(st1)
        if st1 != None:
            st2 = st1.find_all("tr",class_="aggr-row kidney")
            if st2 != None:
                print("NEXT \n")
                print(st2)
