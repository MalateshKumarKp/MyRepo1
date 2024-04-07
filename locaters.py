from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"name").send_keys("Malaetesh")
driver.find_element(By.NAME,"email").send_keys("iammalatesh@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Rdl@12345")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
#Static Dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
msg=driver.find_element(By.CLASS_NAME,'alert-success').text
print(msg)
assert "successfully" in msg
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello_appu")
