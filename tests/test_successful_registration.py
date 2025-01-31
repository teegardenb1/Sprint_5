import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helper_functions.locators import Locators
from helper_functions.data import RandomUserGenerator
from helper_functions.urls import Urls

class TestRegistration:
    def test_successful_registration(self, driver):
        random_user_generator = RandomUserGenerator()
        user_data = random_user_generator.generate_user()
        driver.get(Urls.start_url + 'register')
        driver.find_element(*Locators.register_name_field).send_keys(user_data['name'])
        driver.find_element(*Locators.register_email_field).send_keys(user_data['email'])
        driver.find_element(*Locators.register_password_field).send_keys(user_data['password'])
        driver.find_element(*Locators.register_button).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(Locators.login_header, "Вход")
        )
        button = driver.find_element(*Locators.login_button)
        assert button.is_displayed(), "Кнопка 'Зарегистрироваться' отсутствует на странице."

    def test_incorrect_number_of_characters_in_password_input_field(self, driver):
        random_user_generator = RandomUserGenerator()
        user_data = random_user_generator.generate_user()
        password = '123'
        driver.get(Urls.start_url + 'register')
        driver.find_element(*Locators.register_name_field).send_keys(user_data['name'])
        driver.find_element(*Locators.register_email_field).send_keys(user_data ['email'])
        driver.find_element(*Locators.register_password_field).send_keys(password)
        driver.find_element(*Locators.register_button).click()
        user_exist = driver.find_element(*Locators.user_exists_error)
        assert user_exist.is_displayed()


