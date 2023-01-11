# from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Page_Objects.Homepage import HomePage
from Page_Objects.Loginpage import LoginPage
from Page_Objects.Basepage import BasePage
import unittest
from utils.test_cases import test_cases


class LoginTest(unittest.TestCase):

    def test_sign_in_button(self):
        print("\n" + str(test_cases(3)))
        page = LoginPage()
        login_page = page.click_login_button()
        self.assertIn("please enter your username and password", login_page.lower())

    def test_sign_in_with_valid_user(self):
        print("\n" + str(test_cases(4)))
        login_page = LoginPage()
        login_page.login_with_valid_user("11111")
        self.assertIn("https://petstore.octoperf.com/actions/Catalog.action", login_page.get_url())

    def test_sign_in_with_invalid_user(self):
        print("\n" + str(test_cases(5)))
        login_page = LoginPage()
        result = login_page.login_with_in_valid_user("invalid_user")
        print("*******",result)
        self.assertIn("Invalid username or password. Signin failed", result) #Negative