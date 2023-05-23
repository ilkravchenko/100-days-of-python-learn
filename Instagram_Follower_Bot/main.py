from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

chrome_webdriver_path = r'C:\Development\chromedriver.exe'
SIMILAR_ACCOUNT = 'verbaaa.verbaaa'
USERNAME = 'laykatty201@gmail.com'
PASSWORD = 'anastasiats2019'


class InstaFollower():

    def __init__(self, path):
        self.driver = webdriver.Chrome(path)

    def login(self):
        URL = 'https://www.instagram.com/'
        self.driver.get(URL)
        time.sleep(5)

        email_input = self.driver.find_element(By.CSS_SELECTOR,
                                               '#loginForm > div > div:nth-child(1) > div > label > input')
        email_input.send_keys(USERNAME)

        pass_input = self.driver.find_element(By.CSS_SELECTOR,
                                              '#loginForm > div > div:nth-child(2) > div > label > input')
        pass_input.send_keys(PASSWORD)
        pass_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def find_followers(self):
        URL = f'https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/'
        self.driver.get(URL)
        time.sleep(10)

        modal = self.driver.find_element(By.XPATH,
                                         '//*[@id="mount_0_0_ky"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[3]/div/button')
        time.sleep(5)

        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

        time.sleep(5)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(chrome_webdriver_path)
bot.login()
bot.find_followers()
bot.follow()
