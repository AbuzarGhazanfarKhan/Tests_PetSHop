from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Page_Objects.Basepage import BasePage
from utils.locators import HomePageLocators,CatogryPageLocator
import time


class HomePage(BasePage):

    def __init__(self, base_url='https://petstore.octoperf.com/actions/Catalog.action'):
        self.base_url = base_url
        self.driver =  webdriver.Chrome()
        self.locator=HomePageLocators
        self.categoryLocator = CatogryPageLocator
        self.timeout = 30

    def check_page_loaded(self):
        self.open_home_page()
        return True if self.driver.find_element(*self.locator.LOGO) else False

    def open_home_page(self):
        self.driver.get(self.base_url)


    def search(self,value):
        self.open_home_page()
        self.driver.find_element(*self.locator.SEARCH).send_keys(value)
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        return self.driver.find_element(*self.locator.SEARCH_RESULT).text
    
    def navigate_to_category(self):
        self.open_home_page()
        self.driver.find_element(*self.locator.NAVIGATE_TO_CATEGORY_PAGE_fish).click()
        return self.driver.find_element(*self.categoryLocator.CatogryPageTITLE).text
    def quit(self):
        self.driver.quit()