from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
#driver=webdriver.Chrome(ChromeDriverManager().install())
options =webdriver.Chrome()

driver = webdriver.Chrome(executable_path="/home/sarada/PycharmProjects/FirstseleniumPythonproject/venv/drivers/chromedriver")
#driver.get("https://www.linkedin.com/jobs/")
browser = webdriver.Chrome()
browser.get('http://www.google.com')
#driver.close()
browser.close()