class LandingPage():

    def __init__(self,driver):
        self.driver=driver
        self.login_btn = "components-Nav-partials-UserButton-styles__loggedInState"

    def navigate_to_loginpage(self):

        self.driver.find_element_by_class_name(self.login_btn).click()