import unittest
from selenium import webdriver

 
 
class TestUbuntuHomepage(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        
    def testTitle(self):
        self.browser.get('http://www.ubuntu.com/')
        print "Page Title: ", self.browser.title
        self.assertEqual('The leading operating system for PCs, IoT devices, servers and the cloud | Ubuntu', self.browser.title)
        
    def tearDown(self):
        self.browser.quit()
 
 
if __name__ == '__main__':
    unittest.main()