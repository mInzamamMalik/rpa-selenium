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
    {
        "link": 'https://www.youtube.com/watch?v=y1c2Jy19P18&list=PLaZSdijfCCJBMZM40_pDElJ8dZfQIIreF&index=3',
        "durationInMinutes": 10
    },
    {
        "link": 'https://www.youtube.com/watch?v=pHsiCotGxJ0&list=PLaZSdijfCCJBMZM40_pDElJ8dZfQIIreF&index=5',
        "durationInMinutes": 10
    },
    {
        "link": 'https://youtu.be/yHrko6opl_k?fbclid=IwAR3MSCbtTCtLLrNypHcXGkr8ssDxZRYqyRN9lZrEMJG4St2RyUlBW7y5JwQ',
        "durationInMinutes": 103
    },
    {
        "link": 'https://youtu.be/DovNUotK6D8?fbclid=IwAR1ObLpifxHkSwZAjKzF9gI2jDJu0pKiWEfNpZfkfHSXfDt5y8d84KQuqYc',
        "durationInMinutes": 78
    },
]

gekodriverPath = "/Users/malik/geckodriver 2"
numberOfThreads = 20


def oneView(playButtonCssSelector, videoUrls, gekodriverPath):
    count = 0
    while True:

        cpuLoadInPercent = int(psutil.cpu_percent())
        print("CPU Load: ", cpuLoadInPercent, "%")
        ramUsedPercent = psutil.virtual_memory().percent
        print("Ram load: ", ramUsedPercent, "%")

        # if cpu is high keep waiting for it to go below 80 before opening new browser window
        if(cpuLoadInPercent > 80):
            print(
                "waiting for cpu to go below 80 ++++++++++++++++++++++++++++++++++++++++++++++")
            time.sleep(10)
            continue

        # if cpu is high keep waiting for it to go below 80 before opening new browser window
        if(ramUsedPercent > 90):
            print(
                "waiting for ram to go below 90 ++++++++++++++++++++++++++++++++++++++++++++++")
            time.sleep(10)
            continue

        count = count + 1
        startTime = int(round(time.time()))
        print("count ===============> ", count)

        print("opening browser...", int(round(time.time())) - startTime)
        driver = webdriver.Firefox(executable_path=gekodriverPath)

        randomVideoIndex = int(random() * len(videoUrls))
        url = videoUrls[randomVideoIndex]["link"]
        print("url:", url)

        print("random wait before getting the url... ",
              int(round(time.time())) - startTime)
        # important randomize because if not, it make a brust of get request on youtube that is detectable, it also gives little relief to the processor
        # time.sleep(1 + (random() * numberOfThreads)) # looks unnececerry since I have added random wait before each thread starts

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
        videoLengthInSeconds = videoUrls[randomVideoIndex]["durationInMinutes"] * 60
        randomDuration = (videoLengthInSeconds/2) + \
            ((random() * videoLengthInSeconds) / 2)
        print("playing video for random duration of ", randomDuration, "sec  ",
              int(round(time.time())) - startTime)
        time.sleep(randomDuration)  # important randomize

        print("video played for: ", int(round(time.time())) - playStartTime)
        print("closing browser...", int(round(time.time())) - startTime)
        driver.quit()

        print("took: ", int(round(time.time())) - startTime)


for i in range(0, numberOfThreads):
    # wait for 5 to 60 seconds before staring new thread, to avoide sudden processor load on script starting
    threading.Thread(target=oneView, args=(playButtonCssSelector, videoUrls,
                                           gekodriverPath)).start()
    time.sleep(5 + (random() * 30))
