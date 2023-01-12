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

id = int(input('please insert USERID = '))     
class SignupTest(unittest.TestCase):
    # positive
    def test_submit_empty_signup(self):
        print("\n" + str(test_cases(9)))
        page = SignUpPage()
        page.click_signUp_Button()
        self.assertIn("https://petstore.octoperf.com/actions/Account.action", page.get_url())

    #negative
    def test_Userid_field_validation(self):
        print("\n" + str(test_cases(2)))
        page = SignUpPage()
        page.userId_validation()
        self.assertIn("https://petstore.octoperf.com/actions/Catalog.action", page.get_url())
    
    # # #negative
    def test_repeat_password_match(self):
        print("\n" + str(test_cases(3)))
        page = SignUpPage()
        page.repeatPassword_validation(str(id+100))
        self.assertIn("https://petstore.octoperf.com/actions/Account.action", page.get_url())
    
    # # #negative
    def test_wrong_email_format(self):
        print("\n" + str(test_cases(4)))
        page = SignUpPage()
        page.wrong_email_format_validation(str(id+200))
        self.assertIn("https://petstore.octoperf.com/actions/Account.action", page.get_url())

    # # #negative
    def test_wrong_phone_number_format(self):
        print("\n" + str(test_cases(5)))
        page = SignUpPage()
        result = page.wrong_phone_number_validation(str(id+300))
        self.assertIn("https://petstore.octoperf.com/actions/Account.action", page.get_url())
    
    # #positive
    def test_submitting_form_with_empty_userID(self):
        print("\n" + str(test_cases(6)))
        page = SignUpPage()
        result = page.submitting_form_with_empty_userID()
        self.assertIn("https://petstore.octoperf.com/actions/Account.action", page.get_url())
    
    # #positive
    def test_submitting_form_with_correct_data(self):
        print("\n" + str(test_cases(7)))
        page = SignUpPage()
        page.submitting_form_with_correct_data(str(id+500))
        self.assertIn("https://petstore.octoperf.com/actions/Catalog.action", page.get_url())
    
    
    