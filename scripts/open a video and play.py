from random import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import geckodriver_autoinstaller
import time

geckodriver_autoinstaller.install()
# driver = webdriver.Firefox()
c
firefox_profile = webdriver.FirefoxProfile()

# allow video autoplay
firefox_profile.set_preference('media.autoplay.default', 1)
firefox_profile.set_preference('media.autoplay.allow-muted', False)
driver = webdriver.Firefox(firefox_profile=firefox_profile)

wait = WebDriverWait(driver, 10)

playButtonXpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[26]/div[2]/div[1]/button/svg'
videoUrl = 'https://www.youtube.com/watch?v=sFS0vmV54vY'
videoLengthInSeconds = 30

driver.get(videoUrl)
time.sleep(10 + (random() * 10))
# wait.until(EC.presence_of_element_located((By.XPATH, playButtonXpath)))

count = 1

while True:

    count = count + 1
    print("count", count)

    playButton = driver.find_element(By.XPATH, playButtonXpath)
    # try:
    #     playButton = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, playButtonXpath))
    #     )
    # finally:
    #     driver.quit()

    playButton.click()

    time.sleep(random() * videoLengthInSeconds)

    driver.refresh()
    time.sleep(5 + (random()+5))
    # wait.until(EC.presence_of_element_located((By.XPATH, playButtonXpath)))

    # driver.quit()
