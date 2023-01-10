# from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Page_Objects.Homepage import HomePage
from Page_Objects.Loginpage import LoginPage
from Page_Objects.Basepage import BasePage
from Page_Objects.SignupPage import SignUpPage
import unittest
from utils.test_cases import test_cases


class SignupTest(unittest.TestCase):
    
    
    def test_submit_empty_signup(self):
        print("\n" + str(test_cases(1)))
        page = SignUpPage()
        result = page.click_signUp_Button()
        self.assertIn("fields are empty", result)


    def test_Userid_field_validation(self):
        print("\n" + str(test_cases(1)))
        page = SignUpPage()
        result = page.click_signUp_Button()
        self.assertIn("fields are empty", result)
