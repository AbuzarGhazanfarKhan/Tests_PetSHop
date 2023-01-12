import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.users import *
from Page_Objects.Basepage import BasePage
from utils.locators import HomePageLocators,ShoppingCartPageLocator,LoginPageLocators
from utils.signup import *

class CartPage(BasePage):
    def __init__(self, base_url='https://petstore.octoperf.com/actions/Catalog.action'):
        self.base_url = base_url
        self.driver =  webdriver.Chrome()
        self.locator=ShoppingCartPageLocator
        self.home_locator=HomePageLocators
        self.login_locator=LoginPageLocators
        self.get_user =  getUser
        self.timeout = 30
        
    def open(self):
        self.driver.get(self.base_url)

    def click_cart_Button(self):
        self.driver.find_element(*self.locator.CART_BUTTON).click()
        return self.driver.find_element(*self.locator.CART_PAGE_TITLE).text
    def check_empty_cart(self):
        self.driver.find_element(*self.locator.CART_BUTTON).click()
        return self.driver.find_element(*self.locator.CART_EMPTY_MESSAGE).text
    
    def add_to_cart(self):
        self.driver.find_element(*self.locator.ADD_TO_CART).click()
        # time.sleep(4)
    def click_on_searched_item(self):
        self.driver.find_element(*self.locator.SEARCH_RESULT).click()

    def search(self,value):
        # self.open()
        self.driver.find_element(*self.locator.SEARCH).send_keys(value)
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        # return self.driver.find_element(HomePageLocators.SEARCH_RESULT).text

    def update_cart(self,count):
        self.driver.find_element(*self.locator.CART_PRODUCT_COUNT_INPUT_first).clear()
        self.driver.find_element(*self.locator.CART_PRODUCT_COUNT_INPUT_first).send_keys(count)
        self.driver.find_element(*self.locator.UPDATE_CART).click()
        total=self.driver.find_element(*self.locator.PRODUCT_TOTAL_COST_01_).text
        total=float(total[1:])
        print('total',total)
        listed=self.driver.find_element(*self.locator.PRODUCT_LISTED_COST).text
        listed= float(listed[1:])*count
        print("listed",listed)
        return listed == total

    def get_subTotal(self):
        return self.driver.find_element(*self.locator.CART_SUB_TOTAL).text

    def count_number_of_items_in_cart(self):
       parent= self.driver.find_element(*self.locator.CART_TABLE)
       count= parent.find_element(By.TAG_NAME,"tr")
       return count

    def remove_from_cart(self):
        self.driver.find_element(*self.locator.CART_REMOVE_PRODUCT_01).click()
        return  self.driver.find_element(*self.locator.CART_EMPTY_MESSAGE).text

    def navigate_signin_page(self):
        self.driver.find_element(*self.login_locator.SIGN_IN_BUTTON).click()

    def enter_username(self, username):
        print("------------------------------------------",username)
        self.driver.find_element(*self.login_locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        print("---------------------------------------------",password)
        self.driver.find_element(*self.login_locator.PASSWORD).send_keys(password)

    def login(self, user):
        self.driver.find_element(*self.login_locator.PASSWORD).clear()#negative testcase
        user = self.get_user.get_user(user)
        print("*******************************************************************",user["name"])
        self.enter_username(user["name"])
        self.enter_password(user["password"])
        self.driver.find_element(*self.login_locator.LOGIN_BUTTON).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.locator.PROCEED_TO_CHECKOUT).click()

    def proceed_to_checkout_when_not_loggedin(self):
        self.proceed_to_checkout()
        return self.driver.find_element(*self.locator.PROCEED_TO_CHECKOUT_NOT_LOGGEDIN_MSG).text

    def login_after_checkout(self):
        self.proceed_to_checkout()
        return self.get_url()

    def submit_checkout_form(self):
        self.driver.find_element(*self.locator.CHECKOUT_FORM_SUBMIT).click()

    def submit_order_confirmation(self):
        time.sleep(5)
        print("=================reached Confirm=================")
        self.driver.find_element(*self.locator.CHECKOUT_CONFIRM_ORDER_SUBMIT).click()
        # print(self.driver.find_element(*self.locator.CHECKOUT_CONFIRM_ORDER_SUBMIT).text)
        
    def generate_receipt(self):
       return self.driver.find_element(*self.locator.CONFIRMED_ORDER_MSG).text