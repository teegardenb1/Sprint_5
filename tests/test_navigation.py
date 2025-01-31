import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import log_in
from helper_functions.locators import Locators
from helper_functions.urls import Urls


class TestUserAccountNavigation:
    def test_go_to_user_account_from_main_page(self, driver, log_in):
        driver.find_element(*Locators.user_account_link).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.save_button, 'Сохранить'))
        assert driver.current_url == Urls.start_url + 'account/profile'

    def test_go_to_main_page_from_user_account(self, driver, log_in):
        driver.find_element(*Locators.user_account_link).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.profile_text))
        driver.find_element(*Locators.stellar_burgers_logo).click()
        assert driver.current_url == Urls.start_url



    def test_go_to_constructor_from_main_page(self, driver, log_in):
        driver.find_element(*Locators.user_account_link).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.profile_text))
        driver.find_element(*Locators.constructor_link).click()
        assert driver.current_url == Urls.start_url



