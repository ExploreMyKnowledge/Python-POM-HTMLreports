import importlib

from selenium import webdriver
import time
import unittest
import sys
sys.path.append("/home/sarada/PycharmProjects/POMProjectDemo")
from pages.landingpage import LandingPage
from pages.LoiginPage import LoginPage
from pages.SecondPage import SecondPage
from pages.logoutpage import LogoutPage
import HtmlTestRunner


class Logintest(unittest.TestCase):
    #cla can be anything, cls1, cl2 etc....

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        cls.driver.get("https://mtrx.travel/sv?gclid=EAIaIQobChMI_JHoqpyD6QIVxIGyCh3T0A4TEAAYASAAEgKmM_D_BwE")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_verify(self):
        #driver = self.driver
        self.driver.get("https://mtrx.travel/sv?gclid=EAIaIQobChMI_JHoqpyD6QIVxIGyCh3T0A4TEAAYASAAEgKmM_D_BwE")
        landingpage1 = LandingPage(self.driver)
        landingpage1.navigate_to_loginpage()
        print("homepage displayed")

        Loginpage1 = LoginPage(self.driver)
        Loginpage1.enter_username("xxx@gmail.com")
        Loginpage1.enter_password("yyyyy")
        Loginpage1.click_login()
        time.sleep(3)
        secondpage1 = SecondPage(self.driver)
        secondpage1.click_mittkonto()

        logoutpage1 = LogoutPage(self.driver)
        logoutpage1.click_logout()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

#to generate html reports reports
if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/"))
