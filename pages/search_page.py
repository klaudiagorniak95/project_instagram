from locators import Navigation, Search
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchPage():
    def __init__(self, driver):
        self.driver = driver

    def move_to_search(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Navigation.SEARCH_BUTTON))).click()

    def search_for_profile(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, Search.SEARCH_INPUT))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, Search.SEARCH_INPUT))).send_keys('k._dusia')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Search.SEARCH_RESULT_KDUSIA))).click()