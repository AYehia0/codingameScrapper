# LOL website is down

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options

# For testing
import requests


link = "https://www.codingame.com/ide/354506029a26c09f843bad81165aa0c423daa338"


#login is needed only the first time
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(executable_path='chromedriver', options=options)

driver.get(link)

wait = WebDriverWait(driver, 50)

