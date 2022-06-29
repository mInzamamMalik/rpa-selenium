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

driver.get('https://www.youtube.com/watch?v=sFS0vmV54vY')

time.sleep(6)

id_input = driver.find_element(
    By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[26]/div[2]/div[1]/button')
id_input.click()

time.sleep(30)

driver.quit()
