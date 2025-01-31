import pytest
from selenium import webdriver
from helper_functions.data import PersonalData
from helper_functions.locators import Locators
from helper_functions.urls import Urls



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def website_open(driver):
    driver.get(Urls.start_url)


@pytest.fixture
def log_in(driver):
    driver.get(Urls.start_url + 'login')
    driver.find_element(*Locators.login_email_field).send_keys(*PersonalData.login_email)
    driver.find_element(*Locators.login_password_field).send_keys(*PersonalData.login_password)
    driver.find_element(*Locators.login_button).click()
    driver.find_element(*Locators.user_account_link).click()
    return driver
