from locators import Navigation, Camera
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from time import sleep
import random
from tests.helpers.utils import TestData


class AddPhotoPage():
    def __init__(self, driver):
        self.driver = driver

    def move_to_add_photo(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Navigation.CAMERA_BUTTON))).click()

    def move_to_camera(self):
        sleep(3)
        TouchAction(self.driver).tap(x=Camera.CAMERA_BUTTON_COOR[0], y=Camera.CAMERA_BUTTON_COOR[1]).perform()

    def make_a_photo(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, Camera.SHUTTER_BUTTON))).click()

    def add_filter(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Camera.ADD_FILTER))).click()

    def zoom_photo(self):
        TouchAction(self.driver).tap(x=Camera.EDIT_PHOTO_COOR[0], y=Camera.EDIT_PHOTO_COOR[1]).perform()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Camera.CROP_IMAGE))).click()

        action1 = TouchAction(self.driver).long_press(x=490, y=690).move_to(x=640, y=540).release()
        action2 = TouchAction(self.driver).long_press(x=490, y=690).move_to(x=340, y=840).release()
        m_action = MultiAction(self.driver)
        m_action.add(action1, action2)
        m_action.perform()

        self.driver.find_element_by_id(Camera.CROP_READY_BUTTON).click()
        self.driver.find_element_by_id(Camera.NEXT_BUTTON).click()

    def add_caption(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, Camera.ADD_CAPTION_INPUT))).\
            send_keys(random.choice(TestData.photo_description))
        self.driver.find_element_by_id(Camera.NEXT_BUTTON).click()
