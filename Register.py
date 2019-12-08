from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary

driver = webdriver.Chrome()

#def emag_register():
driver.get("https://www.emag.ro/user/login?ref=hdr_signup_btn")

driver.find_element_by_id("email").send_keys("kxp51892@bcaoo.com")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()

driver.implicitly_wait(3)
driver.find_element_by_id("r_name").send_keys("vlad")
driver.find_element_by_id("r_password").send_keys("password123")
driver.find_element_by_id("r_password_confirmation").send_keys("password123")
driver.implicitly_wait(3)

driver.find_element_by_class_name("gui-form-control -wide -checkboxes tiny-margin").click()
#driver.find_element_by_xpath("/html/body/form/div[5]/div/label").click()
#driver.find_element_by_id("agree_terms").context_click()

#for i in range(20):
    #try:
       # driver.find_element_by_xpath(".//*[contains(text(), 'Am citit și sunt de acord cu ')]").click()
    #    break
 #   except NoSuchElementException as e:
 #       print("retry")
 #       time.sleep(1)
#else:
  #  print ('test failed')

#checkboxElement = driver.find_element_by_id("agree_terms")
#checkboxElement.click()

#driver.find_element_by_id("agree_terms").click()
#driver.find_element_by_id("agree_terms").is_selected()
#driver.find_element_by_id("subsribe_newlsetter").click()

