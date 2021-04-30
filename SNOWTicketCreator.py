from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = True
CHROMEDRIVER_PATH = """C:\\users\\renat\\AppData\\Local\\Temp\\Rar$EXa26408.26884\\chromedriver.exe"""
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
driver.get("https://ironbow.servicenowservices.com/")
driver.find_element_by_name("username").send_keys("rregalado")
driver.find_element_by_name("password1").send_keys("IBIwuoma0amIwuoma0am")
driver.find_element_by_xpath("""//*[@id="submit_row"]/td/input""").click()
time.sleep(3)
driver.switch_to_frame('tp_frame') 
time.sleep(6)
driver.find_element_by_xpath("""//*[@id="auth_methods"]/fieldset/div[1]/button""").click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'mainBannerImage16')))
print(driver.title)