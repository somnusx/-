# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, webbrowser, requests

class Logined(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        #self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "http://n.njcit.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def opinion(self):
        time.sleep(3)
        if requests.get("https://www.baidu.com/", allow_redirects=False).status_code==200:
            print 'login success'
            webbrowser.open("https://www.baidu.com/")
            time.sleep(12000)
        else:return

    def click(self):
        driver = self.driver
        try:
            driver.find_element_by_id("login").click()
            time.sleep(0.4)
        except Exception, e:
            print u"\u9519\u8bef1"
            driver.find_element_by_id("logout").click()        
            time.sleep(1)
            self.opinion()
        try:
            driver.find_element_by_id("logout").click()
            time.sleep(0.9)
        except Exception, e:
            print u"\u9519\u8bef2"
            driver.find_element_by_id("login").click()
            time.sleep(0.5)
            self.opinion()
        
    def test_logined(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("71441P20")
        Select(driver.find_element_by_id("domain")).select_by_visible_text("student")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("714412")
        i = 1
        while True:
            print u"\u7b2c%d\u6b21\u5c1d\u8bd5...... " %i
            i = i + 1
            try:
                self.click()
            except Exception, e:
                self.click()
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
