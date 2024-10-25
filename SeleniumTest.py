import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.cwb.gov.tw/V8/C/'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options = chrome_options)
driver.get(url)

#select district
select_element = driver.find_element(By.XPATH, '//*[@id="home-select-town"]')
selectDistrict = Select(select_element)
selectDistrict.select_by_visible_name('中壢區')

#click button
button = driver.find_element(By.CLASS_NAME, 'btn.btn-default.btn-block.btn-sm')
button.click()

#page down
move = driver.find_element(By.TAG_NAME, 'body')
move.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

r = requests.get(driver.current_url)
result = r.text
print(result)

driver.quit()


