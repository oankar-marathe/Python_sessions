import unittest
import time
from selenium import webdriver
 
 
class TestOrangeHrm(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def testOrangehrmlogin(self):
    	browser =self.browser
    	browser.get("https://opensource-demo.orangehrmlive.com/")
    	username = browser.find_element_by_id("txtUsername")
    	username.clear()
    	username.send_keys("admin")
    	password = browser.find_element_by_id("txtPassword")
    	password.clear()
    	password.send_keys("admin123")
    	browser.find_element_by_id("btnLogin").click()
        time.sleep(3)
    	assert "OrangeHRM" in  browser.title

	def tearDown(self):
		self.browser.close()
 
 
if __name__ == '__main__':
    unittest.main()