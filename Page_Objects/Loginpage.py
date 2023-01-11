from utils.locators import *
from utils.users import *
from selenium import webdriver
from utils.locators import LoginPageLocators,SignupPageLocators
from Page_Objects.Basepage import BasePage
import time

class LoginPage(BasePage):
    def __init__(self,  base_url='https://petstore.octoperf.com/actions/Account.action'):
        self.locator  =  LoginPageLocators
        self.base_url =  base_url
        self.driver   =  webdriver.Chrome()
        self.get_user =  getUser
        self.locatorSignup = SignupPageLocators
        
         # Python2 version
    
    def open_login_page(self):
        self.driver.get(self.base_url)

    def enter_username(self, username):
        print("------------------------------------------",username)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        print("---------------------------------------------",password)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.open_login_page()
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()
        return self.driver.find_element(*self.locator.EMPTYFORM_MESSAGE).text
    
    def login(self, user):
        self.open_login_page()
        self.driver.find_element(*self.locator.PASSWORD).clear()#negative testcase
        user = self.get_user.get_user(user)
        print("*******************************************************************",user["name"])
        self.enter_username(user["name"])
        self.enter_password(user["password"])
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()
        

    def login_with_valid_user(self, user):
        self.login(user)

    def login_with_in_valid_user(self, user):
        self.login(user)
        time.sleep(2)
        print(self.driver.find_element(*self.locator.ERROR_MESSAGE).text)
        return self.driver.find_element(*self.locator.ERROR_MESSAGE).text

    def update_account(self,user):
        self.login(user)
        self.driver.find_element(*self.locator.MY_ACCOUNT).click()
        time.sleep(2)
    
    def update_user_password(self,user):
        self.update_account(user)
        user = self.get_user.get_user(user)        
        self.driver.find_element(*self.locatorSignup.PASSWORD_FIELD).send_keys(user["password"].upper())
        self.driver.find_element(*self.locatorSignup.REPEAT_PASSWORD_FIELD).send_keys(user["password"].upper())
        self.driver.find_element(*self.locatorSignup.SUBMIT).click()
        time.sleep(2)
        self.driver.find_element(*self.locatorSignup.SIGN_OUT).click()
        time.sleep(1)
        self.driver.find_element(*self.locator.SIGN_IN_BUTTON).click()
        self.enter_username(user["name"])
        self.enter_password(user["password"].upper())
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()