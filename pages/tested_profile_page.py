from locators import TestedPage
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from tests.helpers.utils import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestedProfilePage():
    def __init__(self, driver):
        self.driver = driver

    def pick_a_first_photo(self):
        TouchAction(self.driver).press(x=480, y=1409).move_to(x=480, y=728).release().perform()
        self.driver.find_element_by_xpath(TestedPage.FIRST_PHOTO_KDUSIA).click()

    def give_a_like(self):
        self.driver.find_element_by_id(TestedPage.LIKE_BUTTON).click()

    def add_a_comment(self):
        self.driver.find_element_by_id(TestedPage.COMMENT_BUTTON).click()
        self.driver.find_element_by_id(TestedPage.COMMENT_INPUT).send_keys(TestData.comment_content)
        self.driver.find_element_by_id(TestedPage.COMMENT_POST_BUTTON).click()

    def get_added_comment_content(self):
        comment = self.driver.find_element_by_xpath(TestedPage.COMMENT_CONTENT).text
        return comment

    def follow_profile(self):
        self.driver.find_element_by_xpath(TestedPage.FOLLOW_ACCOUNT_BUTTON).click()

    def check_followers_list(self):
        self.driver.find_element_by_id(TestedPage.FOLLOWERS_COUNT).click()
        element = self.driver.find_element_by_xpath(TestedPage.FOLLOWERS_LIST_MY_LOGIN)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def send_message(self, message):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, TestedPage.SEND_MESSAGE_BUTTON))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, TestedPage.EDIT_TEXT_INPUT))).send_keys(message)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, TestedPage.SEND_BUTTON))).click()

    def check_message_content(self):
        message_list = self.driver.find_elements_by_id(TestedPage.SENT_TEXT)
        return message_list[-1].text





