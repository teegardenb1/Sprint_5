import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helper_functions.locators import Locators


class TestLogOutFromPersonalAccount:

    def test_exit_from_personal_account(self, driver,log_in):
        driver.find_element(*Locators.user_account_link).click()
        driver.find_element(*Locators.logout_button).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.log_in_title, 'Вход'))
        assert driver.find_element(*Locators.log_in_title).is_displayed()







