from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import requests
import shutil
import json
import urllib.request

#obtain link from an online file

'''
url = "http://drive.google.com/uc?id=1UJWVVeFotSN3m-eBxVPSQqRW5kJ50yQe"
response = urllib.request.urlopen(url)
file = open("zoom.json", "r")
data = json.loads(response.read())

link = data['1']
'''

#obtain link from a local storage
file = open('zoom.json',)

data = json.load(file)

link = data['1']
 
#optional - choose the chrome profile to use.
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\webdriver")
options.add_argument('--profile-directory=Profile 1')

#However, use of a new chrome instance would always require alert handling.
driver = webdriver.Chrome("C:/Program Files/webdriver/chromedriver.exe", options=options)
driver.maximize_window()
driver.get(link)


