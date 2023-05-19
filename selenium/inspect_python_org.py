from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_webdriver_path = r'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(chrome_webdriver_path)

driver.get('https://www.python.org/')
time.sleep(1)

times = [item.text for item in driver.find_elements(By.CSS_SELECTOR, '.event-widget time')]
names = [item.text for item in driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')]
years = [item.get_attribute("innerHTML") for item in driver.find_elements(By.CSS_SELECTOR, '.event-widget time .say-no-more')]

# for time in times:
#     print(time.text)
# for name in names:
#     print(name.text)

events = {}

for index, item in enumerate(times):
    events[index] = {
        'date' : f'{years[index]}{item}',
        'name' : names[index]
    }

print(events)