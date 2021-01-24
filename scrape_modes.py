from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
import time

#for waiting elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Mode:

    def __init__(self, link):

        # gettin the link
        self.link = link

        # login is needed only the first time
        self.options = webdriver.ChromeOptions()

        # For running in the backgroung
        self.options.add_argument('--headless')
        self.options.add_argument("--disable-gpu")

        # Here i am using brave's login credentials so that i don't have to login 
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(executable_path='chromedriver', options=self.options)
        self.timeout = 12
        self.wait = WebDriverWait(self.driver, self.timeout)
        

        # Opening the clash
        self.driver.get(link)
    

    # Closing the welcome window
    def bypass_welcome(self):
        
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'got-it-button'))).click()

        # Waiting some secs, could be replaced later
        time.sleep(3)


    def get_test_cases(self):
        #clicking the expert mode 
        self.driver.find_element_by_xpath('//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[5]/div[1]/div[1]/div[3]/button').click()
        
        time.sleep(2)
        
        test_cs_contatiner = self.driver.find_element_by_xpath('//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[1]/div/div/div/div')
        test_counts = len(test_cs_contatiner.find_elements_by_xpath('./div'))
        
        print("###TEST CASES###")
        for i in range(1, test_counts+1):

            self.driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[1]/div/div/div/div/div[{i}]').click()
            time.sleep(1)
            case_info = self.driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[1]/div/div/div/div/div[{i}]/div[2]/div').text
            
            print(case_info)
            print("------------")


    def which_mode(self):
        #title xpath
        title = self.driver.find_element_by_xpath('//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[1]/div[1]/h1/span[2]').text
        return title.split('-')[-1].strip(' ').split(' ')[0].lower()


    def get_code(self):

        mode = self.which_mode()
        # Fastest and Shortest modes only have problem description
        if mode == 'fastest' or mode == 'shortest':
            problem_descreption = self.driver.find_element_by_class_name("question-statement").text
            qs_in = self.driver.find_element_by_class_name('question-statement-input').text
            qs_out = self.driver.find_element_by_class_name('question-statement-output').text
            qs_constrains = self.driver.find_element_by_class_name('question-statement-constraints').text

            qs_example_in = self.driver.find_element_by_class_name('question-statement-example-in').text
            qs_example_out = self.driver.find_element_by_class_name('question-statement-example-out').text

            print(f"PROBLEM: {problem_descreption}")
            print(qs_in)
            print(qs_out)
            print(f"CONSTRAINS: {qs_constrains}")
            print(f"EXAMPLE input: {qs_example_in}")
            print(f"EXAMPLE output: {qs_example_out}")
            self.get_test_cases()
        
        # else just else
        if mode == 'reverse':

            reverse_cc = self.driver.find_element_by_class_name('cg-ide-testcases-details-reverse')
            test_cases = len(reverse_cc.find_elements_by_xpath('./div'))

            for i in range(1, test_cases + 1):
                input_test = self.driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div/div[2]/div[{i}]/div[2]/div[2]/pre[1]').text
                output_test = self.driver.find_element_by_xpath(f'//*[@id="scrollable-pane"]/div/ide-page/div/div[2]/div[4]/div[4]/div[2]/div/div[2]/div/div[2]/div[{i}]/div[2]/div[2]/pre[2]').text
                print(f"INPUT: {input_test}")
                print("------------")
                print(f"OUTPUT: {output_test}")
                print("------------")




    

