from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,'//form/div[1]/input').send_keys("demo@gmail.com")
driver.find_element(By.ID,"userPassword").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Confirm Passsword']").send_keys("Hello@1234")