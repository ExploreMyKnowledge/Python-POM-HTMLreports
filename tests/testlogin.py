#Performing selenium unit test python
from selenium import webdriver
import time
import unittest
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

        self.driver.find_element_by_class_name("components-ImportantMessage-styles__closeButton").click()
        self.driver.find_element_by_class_name("components-Nav-partials-UserButton-styles__loggedInState").click()
        time.sleep(2)
        self.driver.find_element_by_name("email").send_keys("xxx@gmail.com")
        self.driver.find_element_by_name("password").send_keys("yyy")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/button[1]").click()
        time.sleep(2)

        self.driver.find_element_by_class_name("components-Nav-partials-UserButton-styles__loggedInState").click()
        time.sleep(2)
        print("clicked on mittconto")

        #self.driver.find_element_by_class_name("pages-helpers-account-partials-AccountLayout-styles__accountMenu").click()
        time.sleep(2)
        print("clicked on logout")

        self.driver.find_element_by_css_selector("div.components-Layout-styles__root main.components-Layout-styles__main.components-Layout-styles__white.pages-helpers-account-partials-AccountLayout-styles__layout div.components-Container-styles__root div.pages-helpers-account-partials-AccountLayout-styles__headerInner div.pages-helpers-account-partials-AccountLayout-styles__accountMenu button.components-StyledLink-styles__root:nth-child(4) > span:nth-child(1)").click()
        print("element found")
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

#generating html reports
if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/sarada/PycharmProjects/POMProjectDemo/Reports/"))




