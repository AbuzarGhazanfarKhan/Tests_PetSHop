from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Page_Objects.Basepage import BasePage
from utils.locators import HomePageLocators,CatogryPageLocator,SignupPageLocators
from utils.signup import *
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
    
    def form_filling(self,data):
        self.driver.find_element(*self.locator.USERID_FIELD).send_keys(data['userId'])
        self.driver.find_element(*self.locator.PASSWORD_FIELD).send_keys(data['password'])
        self.driver.find_element(*self.locator.REPEAT_PASSWORD_FIELD).send_keys(data['new_password'])
        self.driver.find_element(*self.locator.FIRST_NAME_FIELD).send_keys(data['first_name'])
        self.driver.find_element(*self.locator.LAST_NAME_FIELD).send_keys(data['last_name'])
        self.driver.find_element(*self.locator.EMAIL_FIELD).send_keys(data['email'])
        self.driver.find_element(*self.locator.PHONE_FIELD).send_keys(data['phone'])
        self.driver.find_element(*self.locator.ADDRESS1_FIELD).send_keys(data['address1'])
        self.driver.find_element(*self.locator.ADDRESS2_FIELD).send_keys(data['address2'])
        self.driver.find_element(*self.locator.COUNTRY_FIELD).send_keys(data['country'])
        self.driver.find_element(*self.locator.CITY_FIELD).send_keys(data['city'])
        self.driver.find_element(*self.locator.STATE_FIELD).send_keys(data['state'])
        self.driver.find_element(*self.locator.ZIP_FIELD).send_keys(data['zip'])
        language = self.driver.find_element(*self.locator.LANGUAGE_PREFERENCE_FIELD)
        category = self.driver.find_element(*self.locator.FAVOURITE_CATEGORY_FIELD)
        drop=Select(language)
        drop2=Select(category)
        print("he,l")
        drop.select_by_visible_text(data['language_preference'])
        drop2.select_by_visible_text(data['favourite_category'])
        
        self.driver.find_element(*self.locator.ENABLE_MYLIST_FIELD).click()
        self.driver.find_element(*self.locator.ENABLE_MYBANNER_FIELD).click()

    
    def userId_validation(self):
        self.open_signup_page()
        self.form_filling(user1_for_userId_validation)
        self.driver.find_element(*self.locator.SUBMIT).click()
        


    