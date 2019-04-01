import numpy as np
import cv2
import glob
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from PIL import Image
import requests
from io import BytesIO
import schedule
import os

print('processing...')

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'



browser = webdriver.Chrome() 
url = "http://egat.siamcyber.info/#/index/main"
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
a = browser.find_element_by_xpath('//*[@id="status"]')
a.find_element_by_xpath('//*[@id="login"]/div[1]/input').send_keys('maod')
a.find_element_by_xpath('//*[@id="login"]/div[2]/input').send_keys('1234')
a.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(5)

b = browser.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[1]/div[2]/div/div/div')

for i in range(1, 4):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)
	

html_source = browser.page_source
gun = str.encode(html_source)

soup = BeautifulSoup(gun, 'html.parser')
links = soup.findAll('img')
	

link_arr = list()
for a in links:
        url =a.get('ng-src')
        link_arr.append(url)
        print(url)

for c in link_arr[1:]:
        a = "1"
        res = requests.get(c)
        dir_ = "E:\\wasin\\wasin\\python\\wasin\\venv\\image\\"
        sp_s = c.split('/')
        if sp_s[-1] == 'R000':
                pass
        else:
            img=Image.open(BytesIO(res.content))
            img.save(dir_+sp_s[-1],'JPEG')
        browser.service.stop()
        #os.renames(img, a)
time.sleep(30)
        
#for root, dirs, files in os.walk(dir_):
        #for file in files:
                #os.remove(os.path.join(root, file))
       
print('...finised...')


