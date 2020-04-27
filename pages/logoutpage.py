class LogoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.logout_btn="div.components-Layout-styles__root main.components-Layout-styles__main.components-Layout-styles__white.pages-helpers-account-partials-AccountLayout-styles__layout div.components-Container-styles__root div.pages-helpers-account-partials-AccountLayout-styles__headerInner div.pages-helpers-account-partials-AccountLayout-styles__accountMenu button.components-StyledLink-styles__root:nth-child(4) > span:nth-child(1)"

    def click_logout(self):
        self.driver.find_element_by_css_selector(self.logout_btn).click()