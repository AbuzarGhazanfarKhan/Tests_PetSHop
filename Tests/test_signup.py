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
    
    # #negative
    def test_submit_empty_signup(self):
        print("\n" + str(test_cases(1)))
        page = SignUpPage()
        result = page.click_signUp_Button()
        self.assertIn("fields are empty", result)

    # #negative
    def test_Userid_field_validation(self):
        print("\n" + str(test_cases(2)))
        page = SignUpPage()
        page.userId_validation()
        self.assertIn("https://petstore.octoperf.com/actions/Catalog.action", page.get_url())
    
    #negative
    def test_repeat_password_match(self):
        print("\n" + str(test_cases(3)))
        page = SignUpPage()
        result = page.repeatPassword_validation()
        self.assertIn("password do not match", result)
    
    #negative
    def test_wrong_email_format(self):
        print("\n" + str(test_cases(4)))
        page = SignUpPage()
        result = page.wrong_email_format_validation()
        self.assertIn("Invalid email", result)

    #negative
    def test_wrong_phone_number_format(self):
        print("\n" + str(test_cases(5)))
        page = SignUpPage()
        result = page.wrong_phone_number_validation()
        self.assertIn("Invalid phone nmumber", result)
    