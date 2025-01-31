from helper_functions.locators import Locators
from helper_functions.urls import Urls
class TestConstructorTransferToBunsSaucesAndFillings:

    def test_designer_check_tabs_filling(self, driver):
        driver.get(Urls.start_url)
        driver.find_element(*Locators.fillings_section).click()
        current_class = driver.find_element(*Locators.fillings_section).get_attribute('class')
        assert 'tab_tab_type_current' in current_class


    def test_designer_check_tabs_sauce(self, driver):
        driver.get(Urls.start_url)
        driver.find_element(*Locators.sauces_section).click()
        current_class = driver.find_element(*Locators.sauces_section).get_attribute('class')
        assert 'tab_tab_type_current' in current_class

    def test_designer_check_tabs_buns(self, driver):
        driver.get(Urls.start_url)
        driver.find_element(*Locators.fillings_section).click()
        driver.find_element(*Locators.buns_section).click()
        current_class = driver.find_element(*Locators.buns_section).get_attribute('class')
        assert 'tab_tab_type_current' in current_class







