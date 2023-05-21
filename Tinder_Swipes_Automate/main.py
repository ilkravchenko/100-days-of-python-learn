from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

LOGIN = 'illiakravchenko804@gmail.com'
PASSWORD = 'Zwer.190'
URL = 'https://tinder.com/'

chrome_webdriver_path = r'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(chrome_webdriver_path)

driver.get(URL)

# time.sleep(2000)

time.sleep(5)
sign_in = driver.find_element(By.CSS_SELECTOR, '#t-317638561 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div.D\(f\).Ai\(c\).Fxs\(0\) > div:nth-child(2) > a > div.w1u9t036 > div.l17p5q9z')
sign_in.click()
time.sleep(2)

other = driver.find_element(By.CSS_SELECTOR, '#t-2046019637 > main > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div.H\(100\%\).D\(f\).Fxd\(c\) > div.Mt\(a\) > span > button')
other.click()
time.sleep(2)

facebook_login = driver.find_element(By.CSS_SELECTOR, '#t-2046019637 > main > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div.H\(100\%\).D\(f\).Fxd\(c\) > div.Mt\(a\) > span > div:nth-child(2) > button')
facebook_login.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(2)

email_input = driver.find_element(By.CSS_SELECTOR, '#email')
email_input.send_keys(LOGIN)
time.sleep(2)

password_input = driver.find_element(By.CSS_SELECTOR, '#pass')
password_input.send_keys(PASSWORD)
time.sleep(2)

enter = driver.find_element(By.CSS_SELECTOR, "#u_0_0_sA")
enter.click()
time.sleep(5)

driver.switch_to.window(base_window)
print(driver.title)

location = driver.find_element(By.CSS_SELECTOR, "#t-2046019637 > main > div > div > div > div.Bgc\(\$c-ds-background-primary\).Py\(24px\).Px\(36px\) > button:nth-child(1)")
location.click()
time.sleep(5)

notification = driver.find_element(By.CSS_SELECTOR, "#t-2046019637 > main > div > div > div > div.Bgc\(\$c-ds-background-primary\).Py\(24px\).Px\(36px\) > button.c1p6lbu0.W\(100\%\).Mt\(8px\)")
notification.click()
time.sleep(5)

cockie = driver.find_element(By.CSS_SELECTOR, "#t-317638561 > div > div.Pos\(f\).Start\(0\).End\(0\).Z\(2\).Bxsh\(\$bxsh-4-way-spread\).B\(0\).Bgc\(\$c-ds-background-primary\).C\(\$c-ds-text-secondary\) > div > div > div.D\(f\)--ml > div:nth-child(1) > button")
cockie.click()
time.sleep(5)

swipes = 0

while swipes < 100:
    time.sleep(2)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

        # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()

