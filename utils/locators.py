from selenium.webdriver.common.by import By
# for maintainability we can seperate web objects by page name

class HomePageLocators(object):
    CATEGORIES = {
  "fish": '//*[@id="MainImageContent"]/map/area[2]',
  "dog": '//*[@id="MainImageContent"]/map/area[3]',
  "reptile":'//*[@id="MainImageContent"]/map/area[4]',
  "cat" : '//*[@id="MainImageContent"]/map/area[5]',
  "bird": '//*[@id="MainImageContent"]/map/area[6]',
}
    BASEURL="https://petstore.octoperf.com/actions/Catalog.action"
    LOGO = (By.XPATH, '//*[@id="LogoContent"]/a/img')
    # ACCOUNT = (By.ID, 'nav-link-accountList')
    LOGIN = (By.XPATH , '//*[@id="MenuContent"]/a[2]')
    SEARCH = (By.NAME, 'keyword')
    NAVIGATE_TO_CATEGORY_PAGE_bird=(By.XPATH,CATEGORIES['bird'])
    NAVIGATE_TO_CATEGORY_PAGE_dog=(By.XPATH,CATEGORIES['dog'])
    NAVIGATE_TO_CATEGORY_PAGE_reptile=(By.XPATH,CATEGORIES['reptile'])
    NAVIGATE_TO_CATEGORY_PAGE_cat=(By.XPATH,CATEGORIES['cat'])
    NAVIGATE_TO_CATEGORY_PAGE_fish=(By.XPATH,CATEGORIES['fish'])
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[3]/div/form/input[2]')
    SEARCH_RESULT = (By.XPATH, '//*[@id="Catalog"]/table/tbody/tr[2]/td[3]')


class LoginPageLocators(object):
    SIGNUP = (By.XPATH, '//*[@id="Catalog"]/a')
    USERNAME = (By.ID, 'stripes-1782927696')
    PASSWORD = (By.XPATH, '//*[@id="Catalog"]/form/p[2]/input[2]')
    SUBMIT = (By.XPATH, '//*[@id="Catalog"]/form/input')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="Content"]/ul/li/text()')

class SignupPageLocators(object):
    pass


class ShoppingCartPage(object):
    pass
    # by_name_search=''
    # by_name_submitButton="searchProducts"
    # search_result='//*[@id="Catalog"]/table/tbody/tr[2]/td[3]'

class CatogryPage(object):
    
    CatogryPageTITLE=(By.XPATH,'//*[@id="Catalog"]/h2')