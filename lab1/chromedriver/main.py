from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

book = Workbook()
xlfile = book.active

options = Options()
options.page_load_strategy = 'eager'
url = 'https://hh.ru/'
driver = webdriver.Chrome(options=options)
driver.get(url)

search_input = driver.find_element("id","a11y-search-input")
search_input.clear()
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)

jobs = driver.find_elements("class name","serp-item__title-link-wrapper")
for x in jobs:
    xlfile.append([x.text])


book.save('jobs.xlsx')


