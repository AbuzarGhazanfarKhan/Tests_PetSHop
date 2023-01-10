from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Page_Objects.Basepage import BasePage
from utils.locators import HomePageLocators,CatogryPageLocator,SignupPageLocators
import time


class SignUpPage(BasePage):
    def __init__(self, base_url='https://petstore.octoperf.com/actions/Account.action?newAccountForm='):
        self.base_url = base_url
        self.driver =  webdriver.Chrome()
        self.locator=SignupPageLocators
        self.timeout = 30
    
    def open_signup_page(self):
        self.driver.get(self.base_url)

    def click_signUp_Button(self):
        self.open_signup_page()
        result = self.driver.find_element(*self.locator.SIGNUP_BUTTON).click()
        return result
