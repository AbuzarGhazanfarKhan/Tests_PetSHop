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
    #positive
    def test_proceed_to_checkout_when_not_loggedin(self):
        print("\n" + str(test_cases(1)))
        page = CartPage()
        page.open()
        page.search("Tiger")
        page.click_on_searched_item()
        page.add_to_cart()
        result=page.proceed_to_checkout_when_not_loggedin()
        self.assertIn("You must sign on before attempting to check out. Please sign on and try checking out again.", result)


    #negative
    def test_proceed_to_checkout_then_login(self):
        print("\n" + str(test_cases(1)))
        page = CartPage()
        page.open()
        page.search("Tiger")
        page.click_on_searched_item()
        page.add_to_cart()
        result=page.login_after_checkout()
        self.assertIn("https://petstore.octoperf.com/actions/Order.action?newOrderForm=", result)
   
    #positive
    def test_login_then_proceed_to_check_out(self):
        print("\n" + str(test_cases(4)))
        login_page = LoginPage()
        page = CartPage()
        page.open()
        login_page.login_with_valid_user("11111")
        page.search("Tiger")
        page.click_on_searched_item()
        page.add_to_cart()
        page.proceed_to_checkout()
        page.submit_checkout_form()
        page.submit_order_confirmation()
        result=page.generate_receipt()

        self.assertIn("Thank you, your order has been submitted.", result)