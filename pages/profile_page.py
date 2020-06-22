from locators import Navigation, Profile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage():
    def __init__(self, driver):
        self.driver = driver

    def move_to_profile(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Navigation.PROFILE_BUTTON))).click()

    def check_ID(self):
        return self.driver.find_element_by_id(Profile.ID).text

    def check_photos_quantity(self):
        return int(self.driver.find_element_by_id(Profile.POSTS_COUNT).text)