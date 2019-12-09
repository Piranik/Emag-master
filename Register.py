from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary

driver = webdriver.Chrome()
driver.maximize_window()

#def emag_register():
driver.get("https://www.emag.ro/user/login?ref=hdr_signup_btn")

driver.find_element_by_id("email").send_keys("kxp51892@bcao.com")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()

driver.implicitly_wait(3)
driver.find_element_by_id("r_name").send_keys("vlad")
driver.find_element_by_id("r_password").send_keys("password123@@@")
driver.find_element_by_id("r_password_confirmation").send_keys("password123@@@")
driver.implicitly_wait(3)

driver.find_element_by_xpath("/html/body/form/div[6]").click()

#element = driver.find_element_by_xpath("/html/body/form/div[5]")
actions = ActionChains(driver)
#actions.move_to_element(element).click(element).perform()
actions.move_by_offset(802,550).click().perform()

driver.find_element_by_xpath("/html/body/form/div[7]/div/button").click()

#for i in range(20):
    #try:
       # driver.find_element_by_xpath(".//*[contains(text(), 'Am citit și sunt de acord cu ')]").click()
    #    break
 #   except NoSuchElementException as e:
 #       print("retry")
 #       time.sleep(1)
#else:
  #  print ('test failed')


