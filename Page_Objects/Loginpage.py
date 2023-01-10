from utils.locators import *
from utils.users import *
from selenium import webdriver
from utils.locators import LoginPageLocators
from Page_Objects.Basepage import BasePage
import time

class LoginPage(BasePage):
    def __init__(self,  base_url='https://petstore.octoperf.com/actions/Account.action'):
        self.locator  =  LoginPageLocators
        self.base_url =  base_url
        self.driver   =  webdriver.Chrome()
        self.get_user =  getUser
         # Python2 version
    
    def open_login_page(self):
        self.driver.get(self.base_url)

    def enter_username(self, username):
        print(*self.locator.USERNAME,"************",username)
        self.driver.find_element(By.XPATH, '//*[@id="stripes-1265403013"]').send_keys(username)

    def enter_password(self, password):
        print(*self.locator.PASSWORD)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.open_login_page()
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()
        return self.driver.find_element(*self.locator.EMPTYFORM_MESSAGE).text

    def login(self, user):
        self.open_login_page()
        user = self.get_user.get_user(user)
        print("*****",user)
        # self.driver.find_element(By.ID, 'stripes-1620867368').click()

        # self.driver.find_element(By.ID, 'stripes-1620867368').send_keys("abcd")
        self.enter_username(user["name"])
        self.enter_password(user["password"])
        time.sleep(5)
        time.sleep(5)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.driver.find_element(*self.locator.ERROR_MESSAGE).text

