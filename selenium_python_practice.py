from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
username = driver.find_element_by_id("txtUsername")
username.clear()
username.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.clear()
password.send_keys("admin123")
login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()
title = driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
print title
assertEqual("Dashboard",title)
driver.quit()

