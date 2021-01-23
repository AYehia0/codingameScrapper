from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
import time

#for waiting elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://www.codingame.com/ide/35480382a7fdc82f7d3fc2f2ed3d10bc072db941"

#login is needed only the first time
options = webdriver.ChromeOptions()

# # Here i am using brave's login credentials so that i don't have to login 
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(executable_path='chromedriver', options=options)
wait = WebDriverWait(driver, 5)

# Opening the clash
driver.get(link)

# Closing the welcome window
welcome_window = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'got-it-button'))).click()

# Waiting some secs, could be replaced later
time.sleep(3)

#title xpath
title = driver.find_element_by_xpath('//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[1]/div[1]/h1/span[2]').text

reverse_cc = driver.find_element_by_class_name('cg-ide-testcases-details-reverse')
test_cases = len(reverse_cc.find_elements_by_xpath('./div'))

for i in range(1, test_cases):
    input_test = driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div/div[2]/div[{i}]/div[2]/div[2]/pre[1]').text
    output_test = driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div/div[2]/div[{i}]/div[2]/div[2]/pre[2]').text
    print(input_test)
    print(output_test)
