from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxs =driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxs))
for checkbox in checkboxs:
    if checkbox.get_attribute("value")=="option3":
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobuttons=driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
