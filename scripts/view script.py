from random import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options

# import geckodriver_autoinstaller
# geckodriver_autoinstaller.install() # on mac m1 it doesnt instal correct arch

# allow video autoplay

# options=Options()
# options.set_preference('media.autoplay.default', 1)
# options.set_preference('media.autoplay.allow-muted', False)
# driver = webdriver.Firefox(options=options)


playButtonCssSelector = "#movie_player > .ytp-chrome-bottom > .ytp-chrome-controls > .ytp-left-controls > .ytp-play-button "
playButtonXpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[26]/div[2]/div[1]/button'
videoUrls = [
    'https://www.youtube.com/watch?v=zA1ck3sVL2s&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=1',
    'https://www.youtube.com/watch?v=aWEmLUvrgGc&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=2',
    'https://www.youtube.com/watch?v=PjztvPrrn4Y&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=3',
    'https://www.youtube.com/watch?v=vVfmwVn2U_o&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=4',
    'https://www.youtube.com/watch?v=ARgAHpLq8tg&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=5',
    'https://www.youtube.com/watch?v=DyoCBEeFaOs&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=6',
    'https://www.youtube.com/watch?v=stiPGLXIQEg&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=7',
    'https://www.youtube.com/watch?v=8vdSIs_2ziw&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=8',
    'https://www.youtube.com/watch?v=LAIxGoyYoU4&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=9',
    'https://www.youtube.com/watch?v=nWGV6TSKA9U&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=10',
    'https://www.youtube.com/watch?v=GlUB1Xpd7jA&list=PLOGD79Ikh_BZRVqzegRzgQVX_kwS8YlcZ&index=11'
]
videoLengthInSeconds = 30
gekodriverPath = "/Users/malik/geckodriver 2"


count = 0
#  get system time in miliseconds

while True:
    startTime = int(round(time.time() * 1000))
    count = count + 1
    print("count ===============> ", count)


    print("opening browser...", int(round(time.time() * 1000)) - startTime)
    driver = webdriver.Firefox(executable_path=gekodriverPath)

    print("getting webpage...", int(round(time.time() * 1000)) - startTime)


    url = videoUrls[  int(random() * len(videoUrls))  ];
    print("url:", url)
    driver.get(url)

    print("waiting for webpage to load...", int(round(time.time() * 1000)) - startTime)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, playButtonCssSelector)))


    playButton = driver.find_element(By.CSS_SELECTOR, playButtonCssSelector)
    print("playButton", playButton, int(round(time.time() * 1000)) - startTime)

    print("random wait before click on play button", int(round(time.time() * 1000)) - startTime)
    time.sleep(1+ (random() * 6)) # important randomize
    
    print("click", int(round(time.time() * 1000)) - startTime)
    playButton.click()

    print("playing video for random duration...", int(round(time.time() * 1000)) - startTime)
    time.sleep(6 + (random() * videoLengthInSeconds)) # important randomize

    # driver.refresh()
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.CSS_SELECTOR, playButtonCssSelector)))

    print("closing browser...", int(round(time.time() * 1000)) - startTime)
    driver.quit()

    print ("took: ", int(round(time.time() * 1000)) - startTime); 