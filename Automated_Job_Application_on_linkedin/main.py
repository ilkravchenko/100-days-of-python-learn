from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3465189078&distance=25&f_AL=true&geoId=102264497&keywords=junior%20python%20developer&refresh=true'
LOGIN = 'il.kravchenko115@gmail.com'
PASSWORD = 'Family.115'
PHONE = '+380995327348'

chrome_webdriver_path = r'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(chrome_webdriver_path)

driver.get(url=URL)

sign_in = driver.find_element(By.CSS_SELECTOR,
                              'body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis')
sign_in.click()

time.sleep(5)

email = driver.find_element(By.CSS_SELECTOR, '#username')
email.send_keys(LOGIN)

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(PASSWORD)

click_sign_in = driver.find_element(By.CSS_SELECTOR, '#organic-div > form > div.login__form_action_container > button')
click_sign_in.click()

time.sleep(3)
first_job = driver.find_element(By.CSS_SELECTOR, '.scaffold-layout__list-container li')
first_job.click()

time.sleep(3)
easy_apply = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
easy_apply.click()

time.sleep(3)
phone = driver.find_element(By.CSS_SELECTOR,
                            '#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3577797371-87520773-phoneNumber-nationalNumber')
if phone.text == '':
    phone.send_keys(PHONE)

next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
next_button.click()

next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
next_button.click()

experience = driver.find_element(By.CSS_SELECTOR,
                                 '#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3577797371-87520877-numeric')
experience.click()
experience.send_keys('1')

yes_button = driver.find_element(By.CSS_SELECTOR,
                                 '#urn:li:fsd_formElement:urn:li:jobs_applyformcommon_easyApplyFormElement:(3577797371,87520869,multipleChoice)-0')
yes_button.click()

salary = driver.find_element(By.CSS_SELECTOR,
                             '#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3577797371-87520861-numeric')
salary.click()
salary.send_keys('800')

review = driver.find_element(By.CSS_SELECTOR, 'footer div .artdeco-button--primary')
review.click()

submit = driver.find_element(By.CSS_SELECTOR, "#ember861")
