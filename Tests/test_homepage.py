# from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Page_Objects.Homepage import HomePage
from Page_Objects.Loginpage import LoginPage
from Page_Objects.Basepage import BasePage
import unittest
from utils.test_cases import test_cases



class HomeTest(unittest.TestCase):

    def test_hoeme_page_load(self):
        print("\n" + str(test_cases(0)))
        page = HomePage()
        self.assertTrue(page.check_page_loaded())

    def test_search_item_from_searchbar(self):
        print("\n" + str(test_cases(1)))
        page = HomePage()
        time.sleep(1)
        search_result = page.search("Tiger")
        self.assertIn("Tiger", search_result)


    def test_category_page(self):
        print("\n" + str(test_cases(2)))
        page = HomePage()
        time.sleep(1)
        search_result = page.navigate_to_category()
        print(search_result)
        self.assertTrue(search_result)


    def test_cart_page_load(self):
        print("\n" + str(test_cases(3)))
        page = HomePage()
        self.assertTrue(page.navigate_cart_page())
        

    def test_signin_page_load(self):
        print("\n" + str(test_cases(4)))
        page = HomePage()
        self.assertTrue(page.navigate_signin_page())





    