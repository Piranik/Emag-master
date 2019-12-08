from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary

driver = webdriver.Chrome()

driver.get("https://www.emag.ro/user/login?ref=hdr_login_btn")
driver.maximize_window()

driver.find_element_by_id("email").send_keys("smz00953@eveav.com")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()

driver.implicitly_wait(3)
driver.find_element_by_id("password").send_keys("123.ol@h")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()
driver.implicitly_wait(13)

driver.find_element_by_id("emg-input-autosuggest").send_keys("monitor")
driver.find_element_by_xpath('//*[@id="emg-category-menu-icon"]').click()
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, 780)")

driver.find_element_by_xpath('//*[@id="card_grid"]/div[1]/div/div/div[3]/div[3]/form/button').click()
driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div/div[3]/a').click()

