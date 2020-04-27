from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://mtrx.travel/sv?gclid=EAIaIQobChMI_JHoqpyD6QIVxIGyCh3T0A4TEAAYASAAEgKmM_D_BwE")
driver.maximize_window()
driver.implicitly_wait(10)



driver.find_element_by_class_name("components-ImportantMessage-styles__closeButton").click()
driver.find_element_by_class_name("components-Nav-partials-UserButton-styles__loggedInState").click()
time.sleep(2)
driver.find_element_by_name("email").send_keys("cxxxx@gmail.com")
driver.find_element_by_name("password").send_keys("yyyyy")
driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/button[1]").click()
time.sleep(2)

driver.find_element_by_class_name("components-Nav-partials-UserButton-styles__loggedInState").click()
time.sleep(2)
print("clicked on mittconto")
#driver.find_element_by_class_name("pages-helpers-account-partials-AccountLayout-styles__accountMenu").click()
print("clicked on logout")
driver.find_element_by_css_selector("div.components-Layout-styles__root main.components-Layout-styles__main.components-Layout-styles__white.pages-helpers-account-partials-AccountLayout-styles__layout div.components-Container-styles__root div.pages-helpers-account-partials-AccountLayout-styles__headerInner div.pages-helpers-account-partials-AccountLayout-styles__accountMenu button.components-StyledLink-styles__root:nth-child(4) > span:nth-child(1)").click()
print("element found")
time.sleep(3)


driver.close()
driver.quit()
print("test completed")
