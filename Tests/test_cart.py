# from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Page_Objects.Homepage import HomePage
from Page_Objects.Loginpage import LoginPage
from Page_Objects.Basepage import BasePage
from Page_Objects.SignupPage import SignUpPage
from Page_Objects.Cart import CartPage
import unittest
from utils.test_cases import test_cases

# id = int(input('please insert USERID = '))     
class CartTest(unittest.TestCase):
    # positive
    def test_navigate_to_cart_page(self):
        print("\n" + str(test_cases(1)))

        page = CartPage()
        page.open()
        result=page.click_cart_Button()
        self.assertIn("Shopping Cart", result)
#positive
    def test_check_empty_cart(self):
        print("\n" + str(test_cases(1)))
        page = CartPage()
        page.open()
        result=page.check_empty_cart()
        self.assertIn("Your cart is empty.", result)
#Postive
    def test_add_product_to_cart(self):
        print("\n" + str(test_cases(1)))
        page = CartPage()
        page.open()
        page.search("Tiger")
        page.click_on_searched_item()
        page.add_to_cart()
        updated_prices= page.update_cart(2)
        print(updated_prices)
        self.assertEqual(True,updated_prices)

    #negative
    # def test_cart_product_count(self):
    #     print("\n" + str(test_cases(1)))
    #     page = CartPage()
    #     page.open()
    #     page.click_cart_Button()
    #     result=page.count_number_of_items_in_cart()
    #     print(result)
        # self.assertIn("Shopping Cart", result)

    def test_remove_item(self):
        print("\n" + str(test_cases(1)))
        page = CartPage()
        page.open()
        page.search("Tiger")
        page.click_on_searched_item()
        page.add_to_cart()
        result=page.remove_from_cart()
        self.assertIn("Your cart is empty.", result)

    
    