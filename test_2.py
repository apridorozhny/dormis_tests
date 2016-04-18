# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_2(self):
        success = True
        wd = self.wd
        wd.get("https://www.dormis.com/")
        wd.find_element_by_name("send").click()
        wd.find_element_by_xpath("//div[@class='search-filters']/div/div[3]/div[4]/div[3]").click()
        wd.find_element_by_css_selector("a.ngm-thumb-img").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
