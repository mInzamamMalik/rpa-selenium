from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import geckodriver_autoinstaller 
from selenium.webdriver.common.keys import Keys

import time



geckodriver_autoinstaller.install() 
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

print("installed");

driver.get('https://www.youtube.com/watch?v=sFS0vmV54vY')

id_input = driver.find_element(By.XPATH, '//*[@id="classId"]')
id_input.send_keys("secret")
id_input.send_keys(Keys.ENTER)

time.sleep(2)

data_input = driver.find_element(By.XPATH, '//*[@id="todo-item"]')
data_input.send_keys("some text")
data_input.send_keys(Keys.ENTER)

time.sleep(2)

data_input = driver.find_element(By.XPATH, '//*[@id="todo-item"]')
data_input.send_keys("some text")
data_input.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)
# driver.quit()


