from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies=[]

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
#driver.get_screenshot_as_file("sorted.png")
veggiWebElements=driver.find_elements(By.XPATH,'//tr/td[1]')
for ele in veggiWebElements:
    browserSortedVeggies.append(ele.text)
originalSortedVeggiesList=browserSortedVeggies
browserSortedVeggies.sort()
assert browserSortedVeggies == originalSortedVeggiesList

