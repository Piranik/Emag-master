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

#Find first product
#driver.find_element_by_link_text('Adauga in Cos').click()
driver.find_element_by_xpath('//*[@id="card_grid"]/div[1]/div/div/div[3]/div[3]/form/button').click()
driver.implicitly_wait(5)
#go to cart
driver.find_element_by_link_text('Vezi detalii cos').click()

#cart details
driver.find_element_by_xpath('//*[@id="cartProductsPage"]/div[1]/div[1]/div/div[3]/a').click()
driver.find_element_by_xpath('//*[@id="personalPickup"]/div/fieldset/div[1]/div[3]/div/span[1]').click()
#driver.find_element_by_xpath('/html/body/span[2]/span/span[1]/input').send_keys("Showroom Crangasi")

#driver.find_element_by_xpath('//*[@id="select2-shipping[personal][point]-0t-result-k9s4-caa8cf94-c5cb-11e5-84a8-001a4a8c8303"]').click()

#select location
driver.find_element_by_xpath('//*[@id="showroom-map"]/div[2]/div[2]').click()

driver.find_element_by_xpath('//*[@id="paymentSection"]/div[4]/ul/li[1]/div[1]/label').click()

driver.execute_script("window.scrollTo(0, 19020)")
driver.implicitly_wait(5)
#driver.find_element_by_link_text('Pasul urmator').click()
driver.find_element_by_xpath("/html/body/div[1]/div/form/div/div[1]/div[7]/div/div[3]/button").click()

