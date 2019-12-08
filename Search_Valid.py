from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary

driver = webdriver.Chrome()

driver.get("https://www.emag.ro/homepage#opensearch")
driver.find_element_by_id("searchboxTrigger").send_keys("monitor")
driver.find_element_by_css_selector('#masthead > div > div > div.navbar-searchbox > div > form > div.input-group.searchbox-input > div.input-group-btn > button.btn.btn-default.searchbox-submit-button').click()

driver.implicitly_wait(3)

