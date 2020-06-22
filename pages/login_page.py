from locators import LoginPageLocators
from tests.helpers.utils import TestData


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def click_login_btn(self):
        self.driver.find_element_by_id(LoginPageLocators.LOGIN_WITH_PASSWORD_BUTTON).click()

    def input_data(self):
        self.driver.find_element_by_id(LoginPageLocators.LOGIN_INPUT).send_keys(TestData.email)
        self.driver.find_element_by_id(LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.password)

    def click_next(self):
        self.driver.find_element_by_id(LoginPageLocators.LOGIN_BUTTON).click()