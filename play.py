from random import shuffle
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchWindowException
from time import sleep

with open('likes_links.txt', 'r', encoding="utf-8") as f:
    links_list = f.read().split('\n')  # readlines() doesnt work
    links_list.pop(len(links_list) - 1)  # pops EOF "\n"

# un-shuffled
# shuffle w/ return type returns None. https://stackoverflow.com/questions/17649875/why-does-random-shuffle-return-none
shuffle(links_list)
# shuffled

driver = webdriver.Chrome('D:/Download/chromedriver_win32/chromedriver.exe')
# keeps checking 2 times in 1 second if the DOM element has loaded for 5 seconds
driver.implicitly_wait(5)

for current_link in links_list:
    try:
        driver.get(current_link)

        print("Now Playing = ", current_link)  # log

        duration = driver.find_element_by_css_selector(
            '#app > div.playControls.g-z-index-control-bar.m-visible > div > div > div.playControls__elements > div.playControls__timeline > div > div.playbackTimeline__duration > span:nth-child(2)')
        # duration in the lower playback controller

        print("Track length = ", duration.text)  # log
        # duration.text is in the form minutes:seconds
        duration = str(duration.text).split(':')

        if len(duration) == 3:  # hour long songs
            hours = duration[0]
            minutes = duration[1]
            seconds = duration[2]
        else:
            hours = 0
            minutes = float(duration[0])
            seconds = float(duration[1])

        # print(driver.find_element_by_css_selector('.playControl').text)

        if driver.find_element_by_css_selector('.playControl').text != 'Pause current':
            # .playControl is the class that is in button in the bottom overlay that controls play-pause
            driver.find_element_by_css_selector('.playControl').click()
            sleep((hours * 60 + minutes) * 60 + seconds + 0.5)
        else:
            # 1st window takes more than required time hence - 10
            sleep(minutes * 60 + seconds - 10)
    except WebDriverException or NoSuchWindowException:
        print("Window closed!")
        driver.quit()
        exit(0)
