import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
user_name = driver.find_element_by_id("txtUsername")
user_name.send_keys("admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(3)

directory_menu = driver.find_element_by_link_text("Directory")
directory_menu.click()
time.sleep(3)
# searchbox = driver.find_element_by_id("searchDirectory_emp_name_empName")
# searchbox.clear()
# searchbox.send_keys("oankar")
# driver.find_element_by_id("searchBtn").click()
# assert "No Records Found" in driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]").text

pim_menu = driver.find_element_by_link_text("PIM")
pim_menu.click()
driver.implicitly_wait(10)
directory_menu.click()

# admin_menu = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
# submenu = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
# inner_submenu = driver.find_element_by_id("menu_admin_viewSystemUsers")
# ActionChains(driver).move_to_element(admin_menu).move_to_element(submenu).click(inner_submenu).perform()
# time.sleep(5)
# print driver.title

# driver.find_element_by_id("btnAdd").click()
# role_dropdown = Select(driver.find_element_by_id("systemUser_userType"))
# role_dropdown.select_by_index(0)
# time.sleep(5)

# status_dropdown = Select(driver.find_element_by_id("systemUser_status"))
# # status_dropdown.select_by_value("0")
# status_dropdown.select_by_visible_text("Disabled")
# time.sleep(5)

driver.quit()
