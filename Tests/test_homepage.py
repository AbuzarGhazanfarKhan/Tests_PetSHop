# from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Page_Objects.Homepage import HomePage
from Page_Objects.Loginpage import LoginPage
import unittest
from utils.test_cases import test_cases



class HomeTest(unittest.TestCase):

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = HomePage()
        self.assertTrue(page.check_page_loaded())

    def test_search_item(self):
        print("\n" + str(test_cases(1)))
        page = HomePage()
        time.sleep(1)
        search_result = page.search("Tiger")
        self.assertIn("Tiger", search_result)

    def test_category(self):
        print("\n" + str(test_cases(2)))
        page = HomePage()
        time.sleep(1)
        search_result = page.navigate_to_category()
        self.assertIn("fish", search_result.lower())


    # def test_sign_up_button(self):
    #     print("\n" + str(test_cases(2)))
    #     page = HomePage()
    #     sign_up_page = page.click_sign_up_button()
    #     self.assertIn("ap/register", sign_up_page.get_url())

    def test_sign_in_button(self):
        print("\n" + str(test_cases(3)))
        page = LoginPage()
        login_page = page.click_login_button()
        self.assertIn("please enter your username and password", login_page.lower())

    def test_sign_in_with_valid_user(self):
        print("\n" + str(test_cases(4)))
        main_page = LoginPage()
        login_page = main_page.click_login_button()
        result = main_page.login_with_valid_user("valid_user")
        self.assertIn("yourstore/home", result.get_url())

    # def test_sign_in_with_in_valid_user(self):
    #     print("\n" + str(test_cases(5)))
    #     main_page = HomePage()
    #     login_page = main_page.click_sign_in_button()
    #     result = login_page.login_with_in_valid_user("invalid_user")
    #     self.assertIn("There was a problem with your request", result)


# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="SidebarContent"]/a[1]/img').click()
# # driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/a').click()
# time.sleep(4)
# driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/table/tbody/tr[2]/td[1]/a').click()
# time.sleep(4)

# driver.find_element(By.XPATH,'//*[@id="Catalog"]/table/tbody/tr[2]/td[5]/a').click()

# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="Cart"]/form/table/tbody/tr[2]/td[5]/input').send_keys(Keys.BACKSPACE)
# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="Cart"]/form/table/tbody/tr[2]/td[5]/input').send_keys("hey")
# time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="Cart"]/form/table/tbody/tr[3]/td[1]/input').click()