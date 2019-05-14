import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox(executable_path=r'/home/synerzip/Downloads/geckodriver')
driver = webdriver.Chrome(executable_path=r'/home/synerzip/Downloads/chromedriver')
driver.maximize_window()
driver.get("http://www.python.org")
assert "Python" in driver.title
print driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
driver.find_element_by_id("submit").click()
# elem.send_keys(Keys.RETURN)
time.sleep(3)
assert "No results found." not in driver.page_source
driver.close()
