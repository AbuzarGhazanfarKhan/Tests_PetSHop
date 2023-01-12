import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Page_Objects.Homepage import HomePage
from Page_Objects.Loginpage import LoginPage
from Page_Objects.Basepage import BasePage
import unittest
from utils.test_cases import test_cases

class UpdateAccountInfo(unittest.TestCase):  

    def test_update_account(self):
        print("\n" + str(test_cases(23)))
        main_page = LoginPage()
        main_page.update_account("11111")
        self.assertIn("https://petstore.octoperf.com/actions/Account.action?editAccountForm=", main_page.get_url()) #Positive

    def test_update_user_password(self):
        print("\n" + str(test_cases(24)))
        main_page = LoginPage()
        main_page.update_user_password("11111")
        self.assertIn("https://petstore.octoperf.com/actions/Catalog.action", main_page.get_url()) #Positive
