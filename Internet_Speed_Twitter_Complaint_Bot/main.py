from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time


PROMISED_SPEED = 100
LOGIN = 'bilbob172839@gmail.com'
NAME = 'illiakrav'
PASSWORD = 'Family.115'

chrome_webdriver_path = r'C:\Development\chromedriver.exe'

class InternetSpeedTwitterBot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        URL = 'https://www.speedtest.net/'
        self.driver.get(URL)

        time.sleep(5)
        run_test = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        run_test.click()

        time.sleep(100)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').get_attribute("innerHTML")
        print(f"{self.up}")

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').get_attribute("innerHTML")
        print(f"{self.down}")

        time.sleep(2)
        self.driver.quit()


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sign_up = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
        sign_up.click()
        time.sleep(2)

        email_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(LOGIN)
        email_input.send_keys(Keys.ENTER)
        time.sleep(1)

        user_name = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        user_name.send_keys(NAME)
        user_name.send_keys(Keys.ENTER)
        time.sleep(1)

        pass_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys(PASSWORD)
        pass_input.send_keys(Keys.ENTER)
        time.sleep(1)

        make_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/textarea')
        make_tweet.send_keys(f'Hey Internet Provider, why is my internet speed {self.up}, when I pay for {PROMISED_SPEED}?')
        time.sleep(3)

        send_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send_tweet.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(chrome_webdriver_path)
bot.get_internet_speed()
if bot.up + 10 < PROMISED_SPEED:
    bot.tweet_at_provider()
else:
    print('Your speed is good')
