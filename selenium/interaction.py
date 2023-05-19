from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_webdriver_path = r'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(chrome_webdriver_path)

driver.get('https://en.m.wikipedia.org/wiki/Main_Page')
time.sleep(1)

articles_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
#print(articles_count.text)
#articles_count.click()

#wiktionary = driver.find_element(By.CSS_SELECTOR, "#sister-projects-list li:nth-child(12) div:nth-child(2) a")
wiktionary = driver.find_element(By.LINK_TEXT, 'Wiktionary')
#wiktionary.click()

time.sleep(1)
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(5)