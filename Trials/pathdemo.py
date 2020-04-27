from selenium import webdriver
#from selenium.webdriver.common.keys import keys
driver =webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.google.com/")
driver.close()