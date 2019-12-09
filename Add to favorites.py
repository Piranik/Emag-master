from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary

driver = webdriver.Chrome()

#step 1/4 purchase area
driver.get("https://www.emag.ro/user/login?ref=hdr_login_btn")
driver.maximize_window()

driver.find_element_by_id("email").send_keys("smz00953@eveav.com")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()

#log in
driver.implicitly_wait(3)
driver.find_element_by_id("password").send_keys("123.ol@h")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()
driver.implicitly_wait(5)

#search for product
driver.find_element_by_id("emg-input-autosuggest").send_keys("monitor")
driver.find_element_by_xpath('//*[@id="emg-category-menu-icon"]').click()
driver.implicitly_wait(5)
driver.execute_script("window.scrollTo(0, 680)")

#Find the first item, and add them to favorites from their page
driver.find_element_by_xpath('//*[@id="card_grid"]/div[1]/div/div/div[2]/h2/a').click()
driver.find_element_by_xpath('//*[@id="page-skin"]/div[2]/div/div[2]/div[2]/div/div/div[2]/form/div[3]/button[2]').click()

