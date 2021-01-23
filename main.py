from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
import time

#for waiting elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://www.codingame.com/clashofcode/clash/1558603a439b6c45dccd69c6d059b06043606e0"

MODE = 'fastest'


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


if MODE == 'reverse':
    #title xpath
    title = driver.find_element_by_xpath('//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[1]/div[1]/h1/span[2]').text

    reverse_cc = driver.find_element_by_class_name('cg-ide-testcases-details-reverse')
    test_cases = len(reverse_cc.find_elements_by_xpath('./div'))

    for i in range(1, test_cases):
        input_test = driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div/div[2]/div[{i}]/div[2]/div[2]/pre[1]').text
        output_test = driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div/div[2]/div[{i}]/div[2]/div[2]/pre[2]').text
        print(input_test)
        print(output_test)

if MODE == 'fastest':
    problem_descreption = driver.find_element_by_class_name("question-statement").text
    qs_in = driver.find_element_by_class_name('question-statement-input').text
    qs_out = driver.find_element_by_class_name('question-statement-output').text
    qs_constrains = driver.find_element_by_class_name('question-statement-constraints').text

    qs_example_in = driver.find_element_by_class_name('question-statement-example-in').text
    qs_example_out = driver.find_element_by_class_name('question-statement-example-out').text


    #clicking the expert mode 
    driver.find_element_by_xpath('//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[5]/div[1]/div[1]/div[3]/button').click()
    time.sleep(2)
    test_cs_contatiner = driver.find_element_by_xpath('//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[1]/div/div/div/div')
    test_counts = len(test_cs_contatiner.find_elements_by_xpath('./div'))

    #clicking them all
    # //*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[1]/div/div/div/div/div[1]
    # //*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[1]/div/div/div/div/div[2]
    for i in range(1, test_counts+1):

        driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[1]/div/div/div/div/div[{i}]').click()
        time.sleep(1)
        print(driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[1]/div/div/div/div/div[{i}]/div[2]/div').text)
        print("------")

