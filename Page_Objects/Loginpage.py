from utils.locators import *
from utils.users import users
from selenium import webdriver


class LoginPage():
    def __init__(self, driver):
        self.locator = LoginPageLocators
        # self.base_url = base_url
        self.driver =  webdriver.Firefox()
         # Python2 version

    def enter_username(self, username):
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.locator.SUBMIT).click()

    def login(self, user):
        user = users.get_user(user)
        print(user)
        self.enter_email(user["email"])
        self.enter_password(user["password"])
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.driver.find_element(*self.locator.ERROR_MESSAGE).text