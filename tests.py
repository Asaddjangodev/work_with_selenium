from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# class Hosttest(LiveServerTestCase):
#     def testhomepage(self):
#         driver = webdriver.Chrome()
#
#         driver.get('http://127.0.0.1:8000/')
#
#         time.sleep(5)
#
#         assert "Hello, world!" in driver.title

class LoginFormTest(LiveServerTestCase):
    def testform(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/accounts/login/')

        time.sleep(5)

        user_name = driver.find_element(By.NAME, 'username')
        user_password = driver.find_element(By.NAME,'password')
        submit = driver.find_element(By.ID, 'submit')


        user_name.send_keys('test')
        user_password.send_keys('1234')
        submit.send_keys(Keys.RETURN)

        assert 'test' in driver.page_source
        time.sleep(3)


        # find_element_by_id
        # find_element_by_name
        # find_element_by_xpath
        # find_element_by_lint_text
        # find_element_by_partial_link_text
        # find_element_by_tag_name
        # find_element_by_class_name
        # find_element_by_css_selector