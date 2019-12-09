from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary

#prerequirement to have objects in your cart, you can use purchase.py
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.emag.ro/user/login?ref=hdr_login_btn")

driver.find_element_by_id("email").send_keys("smz00953@eveav.com")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()

driver.implicitly_wait(3)
driver.find_element_by_id("password").send_keys("123.ol@h")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()
driver.implicitly_wait(3)

#Access cart
driver.find_element_by_xpath('//*[@id="emg-mini-cart"]').click()
#Delete button
driver.find_element_by_xpath('//*[@id="vendorsContainer"]/div/div[1]/div/div[2]/div[1]/div[3]/a[1]').click()
#Return to home page
driver.find_element_by_xpath('//*[@id="empty-cart"]/div[3]/a[1]').click()
driver.find_element_by_xpath('//*[@id="header"]/div[1]/a').click()

