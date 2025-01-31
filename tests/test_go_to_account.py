import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helper_functions.locators import Locators
from helper_functions.data import PersonalData
from helper_functions.urls import Urls


class TestLogIn:

    def test_log_in_by_account_button_main_page(self,driver):
        driver.get(Urls.start_url)
        driver.find_element(*Locators.account_login_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.login_header))
        driver.find_element(*Locators.login_email_field).send_keys(PersonalData.login_email)
        driver.find_element(*Locators.register_password_field).send_keys(PersonalData.login_password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.log_in_title, 'Вход'))
        assert driver.find_element(*Locators.log_in_title).is_displayed(), 'Кнопка вход не видна на странице'

    def test_log_in_by_registration_page (self, driver):
        driver.get(Urls.start_url + 'register')
        driver.find_element(*Locators.register_login_link).click()
        WebDriverWait(driver, 5).until((EC.visibility_of_element_located(Locators.login_header)))
        driver.find_element(*Locators.login_email_field).send_keys(PersonalData.login_email)
        driver.find_element(*Locators.login_password_field).send_keys(PersonalData.login_password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.log_in_title, 'Вход'))
        assert driver.find_element(*Locators.log_in_title).is_displayed(), 'Кнопка вход не видна на странице'


    def test_log_in_by_personal_account (self, driver):
        driver.get(Urls.start_url + 'login')
        driver.find_element(*Locators.user_account_link).click()
        WebDriverWait(driver, 5).until((EC.visibility_of_element_located(Locators.login_header)))
        driver.find_element(*Locators.login_email_field).send_keys(PersonalData.login_email)
        driver.find_element(*Locators.login_password_field).send_keys(PersonalData.login_password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.log_in_title, 'Вход'))
        assert driver.find_element(*Locators.log_in_title).is_displayed(), 'Кнопка вход не видна на странице'

    def test_log_in_by_recovery_password (self, driver):
        driver.get(Urls.start_url + 'forgot-password')
        driver.find_element(*Locators.register_login_link).click()
        WebDriverWait(driver, 5).until((EC.visibility_of_element_located(Locators.login_header)))
        driver.find_element(*Locators.login_email_field).send_keys(PersonalData.login_email)
        driver.find_element(*Locators.login_password_field).send_keys(PersonalData.login_password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.log_in_title, 'Вход'))
        assert driver.find_element(*Locators.log_in_title).is_displayed(), 'Кнопка вход не видна на странице'











