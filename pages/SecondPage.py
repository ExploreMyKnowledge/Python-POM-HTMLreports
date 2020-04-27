class SecondPage():

    def __init__(self,driver):
        self.driver=driver
        self.mittkont_btn = "components-Nav-partials-UserButton-styles__loggedInState"

    def click_mittkonto(self):
        self.driver.find_element_by_class_name(self.mittkont_btn).click()