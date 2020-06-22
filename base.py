import os
import unittest
from appium import webdriver
from pages.login_page import LoginPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '9'
        desired_caps['deviceName'] = 'Xperia XZ1'
        desired_caps['app'] = PATH('Instagram_v130.0.0.31.121_apkpure.com.apk')
        desired_caps['appPackage'] = 'com.instagram.android'
        desired_caps['appActivity'] = 'com.instagram.mainactivity.MainActivity'
        desired_caps['autoGrantPermissions'] = 'true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        lp = LoginPage(self.driver)
        lp.click_login_btn()
        lp.input_data()
        lp.click_next()

    def tearDown(self):
        self.driver.quit()

