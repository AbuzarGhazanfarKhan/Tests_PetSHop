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
    SEARCH = (By.XPATH, '/html/body/div[1]/div[3]/div/form/input[1]')
    NAVIGATE_TO_CATEGORY_PAGE_bird=(By.XPATH,CATEGORIES['bird'])
    NAVIGATE_TO_CATEGORY_PAGE_dog=(By.XPATH,CATEGORIES['dog'])
    NAVIGATE_TO_CATEGORY_PAGE_reptile=(By.XPATH,CATEGORIES['reptile'])
    NAVIGATE_TO_CATEGORY_PAGE_cat=(By.XPATH,CATEGORIES['cat'])
    NAVIGATE_TO_CATEGORY_PAGE_fish=(By.XPATH,'//*[@id="SidebarContent"]/a[1]/img')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[3]/div/form/input[2]')
    SEARCH_RESULT = (By.XPATH, '//*[@id="Catalog"]/table/tbody/tr[2]/td[3]')


class LoginPageLocators(object):
    SIGNUP = (By.XPATH, '//*[@id="Catalog"]/a')
    USERNAME = (By.XPATH, '/html/body/div[2]/div/form/p[2]/input[1]')
    PASSWORD = (By.XPATH, '//*[@id="Catalog"]/form/p[2]/input[2]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="Catalog"]/form/input')
    ERROR_MESSAGE = (By.XPATH, '/html/body/div[2]/ul/li')
    EMPTYFORM_MESSAGE = (By.XPATH,'//*[@id="Catalog"]/form/p[1]')
    REGISTER = (By.XPATH,'/html/body/div[2]/div/a')
    MY_ACCOUNT = (By.XPATH,'/html/body/div[1]/div[2]/div/a[3]')
    SIGN_IN_BUTTON = (By.XPATH,'/html/body/div[1]/div[2]/div/a[2]')
    

class SignupPageLocators(object):
    
    SIGNUP_BUTTON = (By.XPATH,'/html/body/div[2]/div/form/input')
    USERID_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[1]/tbody/tr[1]/td[2]/input')
    PASSWORD_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[1]/tbody/tr[2]/td[2]/input')
    REPEAT_PASSWORD_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[1]/tbody/tr[3]/td[2]/input')
    FIRST_NAME_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[1]/td[2]/input')
    LAST_NAME_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input')
    EMAIL_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[3]/td[2]/input')
    PHONE_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[4]/td[2]/input')
    ADDRESS1_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[5]/td[2]/input')
    ADDRESS2_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[6]/td[2]/input')
    CITY_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[7]/td[2]/input')
    STATE_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[8]/td[2]/input')
    ZIP_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[9]/td[2]/input')
    COUNTRY_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[2]/tbody/tr[10]/td[2]/input')
    LANGUAGE_PREFERENCE_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[3]/tbody/tr[1]/td[2]/select')
    FAVOURITE_CATEGORY_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[3]/tbody/tr[2]/td[2]/select')
    ENABLE_MYLIST_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[3]/tbody/tr[3]/td[2]/input')
    ENABLE_MYBANNER_FIELD = (By.XPATH,'/html/body/div[2]/div/form/table[3]/tbody/tr[4]/td[2]/input')
    SUBMIT = (By.XPATH,'/html/body/div[2]/div/form/input')
    SIGN_OUT = (By.XPATH,'/html/body/div[1]/div[2]/div/a[2]')


class ShoppingCartPageLocator(object):
    CART_BUTTON=(By.XPATH,'//*[@id="MenuContent"]/a[1]')
    UPDATE_CART=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[3]/td[1]/input')
    ADD_TO_CART=(By.XPATH,'/html/body/div[2]/div[2]/table/tbody/tr[2]/td[5]/a')
    CART_PAGE_TITLE=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/h2')
    CART_EMPTY_MESSAGE=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[2]/td/b')
    CART_PRODUCT_COUNT_INPUT_first=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[2]/td[5]/input')
    CART_PRODUCT_COUNT_INPUT_02=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[3]/td[5]/input')
    CART_REMOVE_PRODUCT_01=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[2]/td[8]/a')
    CART_REMOVE_PRODUCT_02=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[3]/td[8]/a')
    PRODUCT_LISTED_COST=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[2]/td[6]')
    PRODUCT_TOTAL_COST_01_=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[2]/td[7]')
    PRODUCT_TOTAL_COST_02=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[3]/td[7]')
    CART_SUB_TOTAL=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody/tr[4]/td[1]/text()')
    CART_TABLE=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/table/tbody')
    SEARCH_RESULT=(By.XPATH,'/html/body/div[2]/div[2]/table/tbody/tr[2]/td[1]/a')
    SEARCH = (By.XPATH, '/html/body/div[1]/div[3]/div/form/input[1]')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[3]/div/form/input[2]')
    PROCEED_TO_CHECKOUT=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/a')
    PROCEED_TO_CHECKOUT_NOT_LOGGEDIN_MSG=(By.XPATH,'/html/body/div[2]/ul/li')
    CHECKOUT_FORM_SUBMIT=(By.XPATH,'/html/body/div[2]/div/form/input')
    CHECKOUT_CONFIRM_ORDER_SUBMIT=(By.XPATH,'/html/body/div[2]/div[2]/a')
    CONFIRMED_ORDER_MSG=(By.XPATH,'/html/body/div[2]/ul/li')

class CatogryPageLocator(object):
    
    CatogryPageTITLE=(By.XPATH,'//*[@id="Catalog"]/h2')#//*[@id="Catalog"]/h2
    CATEGORY_PRODUCT=(By.XPATH,'/html/body/div[2]/div[2]/table/tbody/tr[2]/td[1]/a')
