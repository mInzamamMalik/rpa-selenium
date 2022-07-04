from random import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
from multiprocessing import Process
import threading
import psutil  # processor stats


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
videoLengthInSeconds = 162
gekodriverPath = "/Users/malik/geckodriver 2"
numberOfThreads = 15


def oneView(playButtonCssSelector, videoUrls, videoLengthInSeconds, gekodriverPath):
    count = 0
    while True:

        cpuLoadInPercent = int(psutil.cpu_percent())
        print("CPU Load: ", cpuLoadInPercent, "%")
        
        # if cpu is high keep waiting for it to go below 90 before opening new browser window
        if(cpuLoadInPercent > 80):
            print(
                "waiting for cpu to go below 80 ++++++++++++++++++++++++++++++++++++++++++++++")
            time.sleep(10)
            continue

        count = count + 1
        startTime = int(round(time.time()))
        print("count ===============> ", count)

        print("opening browser...", int(round(time.time())) - startTime)
        driver = webdriver.Firefox(executable_path=gekodriverPath)

        url = videoUrls[int(random() * len(videoUrls))]
        print("url:", url)

        print("random wait before getting the url... ",
              int(round(time.time())) - startTime)
        # important randomize because if not, it make a brust of get request on youtube that is detectable, it also gives little relief to the processor
        time.sleep(1 + (random() * numberOfThreads))

        print("getting webpage...", int(round(time.time())) - startTime)
        driver.get(url)

        print("waiting for webpage to load...", int(
            round(time.time())) - startTime)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, playButtonCssSelector)))

        playButton = driver.find_element(
            By.CSS_SELECTOR, playButtonCssSelector)
        print("playButton", playButton, int(
            round(time.time())) - startTime)

        print("random wait before click on play button",
              int(round(time.time())) - startTime)
        time.sleep(1 + (random() * 6))  # important randomize

        print("click", int(round(time.time())) - startTime)
        playButton.click()

        playStartTime = int(round(time.time()))

        # from 50% to 100% of video length
        randomDuration = (videoLengthInSeconds/2) + \
            ((random() * videoLengthInSeconds) / 2)
        print("playing video for random duration of ", randomDuration, "sec  ",
              int(round(time.time())) - startTime)
        time.sleep(randomDuration)  # important randomize

        # driver.refresh()
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, playButtonCssSelector)))
        print("video played for: ", int(round(time.time())) - playStartTime)
        print("closing browser...", int(round(time.time())) - startTime)
        driver.quit()

        print("took: ", int(round(time.time())) - startTime)


for i in range(0, numberOfThreads):
    threading.Thread(target=oneView, args=(playButtonCssSelector, videoUrls,
                                           videoLengthInSeconds, gekodriverPath)).start()
