# LOL website is down

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
import time


# For testing
import requests


#link = "https://www.codingame.com/clashofcode/clash/1558452d871d4d157e24ee47c16a7492db3258b"
link = "https://www.codingame.com/ide/35478861c775e56b0e180f7aea83f25c2cc25a4b"


#login is needed only the first time
# options = webdriver.ChromeOptions()

# # Here i am using brave's login credentials so that i don't have to login 
# options.add_argument('--user-data-dir=/home/none/.config/BraveSoftware/Brave-Browser/')
driver = webdriver.Chrome(executable_path='chromedriver')

driver.get(link)

# List of test cases in case of reverse mode:  cg-ide-testcases-details-reverse
# Case open : testcase open
# test Case content : testcase-content

time.sleep(10)


#closing the welcome window
driver.find_element_by_class_name("got-it-button").click()


#title xpath
# 

test_cases = driver.find_elements_by_class_name("cg-ide-testcases-details-reverse")

print(len(test_cases))
for case in test_cases:
    co = case.find_element_by_class_name("testcase open")
    for content in co:
        print(content.find_element_by_class_name("testcase-content"))

# /html/body/div[8]/div[2]/div[1]/div/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]
# /html/body/div[8]/div[2]/div[1]/div/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]

# //*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]
# //*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]

# testcase-text testcase-in
# testcase-text testcase-out


# shortest mode question statement
#//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/cg-ide-statement/div/cg-statement/div/div/div[1]/span

# stat blocks
#statement-section statement-protocol
#//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/cg-ide-statement/div/cg-statement/div/div/div[2]

#to show test cases
# header-button showtestcases-button

# testcases-details-container
# cg-ide-testcases-details