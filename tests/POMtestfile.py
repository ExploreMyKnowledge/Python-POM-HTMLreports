from selenium import webdriver
import time
import unittest
from pages import LandingPage
from pages import LoginPage
from pages import SecondPage
from pages import LogoutPage

class Logintest(unittest.TestCase):
    #cla can be anything, cls1, cl2 etc....

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_verify(self):
        driver =self.driver
        driver.get("https://mtrx.travel/sv?gclid=EAIaIQobChMI_JHoqpyD6QIVxIGyCh3T0A4TEAAYASAAEgKmM_D_BwE")
        landingpage1 = LandingPage(driver)
        landingpage1.navigate_to_loginpage()
        Loginpage1 = LoginPage(driver)
        Loginpage1.username_txtbox("par.sar.7711@gmail.com")
        Loginpage1.password_txtbox("allpurpose")
        Loginpage1.click_login()
        secondpage1 = SecondPage(driver)
        secondpage1.click_mittkonto()
        logoutpage1=LogoutPage(driver)
        logoutpage1.click_logout()
        time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

