from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("scrshot.png")
sleep(2)