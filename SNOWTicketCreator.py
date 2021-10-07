from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def menu_options():
    print("1) create Patient login ticket\n")
    print("2) create admin health check ticket\n")
    print("q) quit")
    choice = input("what would you like to do: ")
    return choice

if (__name__ == "__main__"):
    options = Options()
    options.headless = True
    CHROMEDRIVER_PATH = """C:\\users\\renat\\chromedriver.exe"""
    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
    driver.maximize_window()
    executor_url = driver.command_executor._url
    session_id = driver.session_id
    driver.get("https://ironbow.servicenowservices.com/")
    driver.find_element_by_name("username").send_keys("") #fill ironbow username between the quotes
    driver.find_element_by_name("password1").send_keys("") #fill ironbow password between the quotes
    driver.find_element_by_xpath("""//*[@id="submit_row"]/td/input""").click()
    time.sleep(3)
    driver.switch_to_frame('tp_frame')
    # driver.switch_to.frame('tp_frame')
    time.sleep(6)
    driver.find_element_by_xpath("""//*[@id="auth_methods"]/fieldset/div[1]/button""").click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'mainBannerImage16')))
    driver.switch_to.parent_frame()
    print(driver.title)
    print(driver.current_url)
    print(executor_url)
    print(session_id)

    choice = menu_options()
    while (choice != 'q'):
        if choice == 1:
            print("creating USCG patient ticket")
            choice = menu_options()
        elif choice == 2:
            print("creating admin health check ticket")
            choice = menu_options()
        else:
            driver.quit()
