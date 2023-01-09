from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.locators import HomePageLocators

driver= webdriver.Firefox()

class HomePage(object):

    def __init__(self, base_url='https://petstore.octoperf.com/actions/Catalog.action'):
        self.base_url = base_url
        self.driver =  webdriver.Firefox()
        self.locator=HomePageLocators
        self.timeout = 30

    def check_page_loaded(self):
        return True if self.driver.find_element(*self.locator.LOGO) else False

    def open_home_page(self):
        self.driver.get(self.base_url)

    def search(self,value):
        self.open_home_page()
        self.driver.find_element(By.NAME, 'keyword').send_keys(value)
        self.driver.find_element(self.locator.SEARCH_BUTTON).click()
        return self.driver.find_element(self.locator.SEARCH_RESULT).text
    
    def navigate_to_category(self,category):
        self.driver.find_element(self.locator.CATEGORIES[category])
        
    def quit(self):
        self.driver.quit()