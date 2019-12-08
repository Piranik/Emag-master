from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary

driver = webdriver.Chrome()

driver.get("https://www.emag.ro/user/login?ref=hdr_login_btn")

driver.find_element_by_id("email").send_keys("smz00953@eveav.com")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()

driver.implicitly_wait(3)
driver.find_element_by_id("password").send_keys("123.ol@h")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()
driver.implicitly_wait(3)