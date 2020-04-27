class LoginPage():

    #creating a constructor
    def __init__(self,driver):
        self.driver=driver
        self.username_txtbox="email"
        self.password_txtbox="password"
        self.login_button="/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/button[1]"

    def enter_username(self,username):
        self.driver.find_element_by_name(self.username_txtbox).clear()
        self.driver.find_element_by_name(self.username_txtbox).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_name(self.password_txtbox).clear()
        self.driver.find_element_by_name(self.password_txtbox).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button).click()