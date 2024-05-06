from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from dotenv import load_dotenv

from Utils.BaseApp import BasePage
from Pages.CustomerPage import CustomerPage


class LoginPageLocators:
    LOCATOR_CUSTOMER_LOGIN_BTN = (By.CSS_SELECTOR, '[ng-click="customer()"]')
    LOCATOR_BANK_MANGER_LOGIN_BTN = (By.CSS_SELECTOR, '[ng-click="manager()]')
    LOCATOR_USER_SELECTOR = (By.ID, "userSelect")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR,'[type="submit"]')

class DoLogin(BasePage):

    def choose_customer(self):
        btn = self.find_element(LoginPageLocators.LOCATOR_CUSTOMER_LOGIN_BTN).click()

    def choose_manger(self):
        btn = self.find_element(LoginPageLocators.LOCATOR_BANK_MANGER_LOGIN_BTN).click()

    def check_user_select(self):
        user_selector = self.find_element(LoginPageLocators.LOCATOR_USER_SELECTOR)
        return user_selector

    def choose_user(self):
        load_dotenv()
        login = os.getenv('LOGIN')
        user_list = Select(self.find_element(LoginPageLocators.LOCATOR_USER_SELECTOR))
        user_list.select_by_visible_text(f'{login}')

    def login(self):
        login_btn = self.find_element(LoginPageLocators.LOCATOR_LOGIN_BTN).click()
        return CustomerPage(self.driver)

