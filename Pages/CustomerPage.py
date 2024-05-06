from selenium.webdriver.common.by import By

from Utils.DepositFibanachi import fibonacci
from Utils.BaseApp import BasePage

import os
from dotenv import load_dotenv

from Pages.TransactionsPage import TransactionsPage


class CustomerPageLocators():
    LOCATOR_CUSTOMER_NAME = (By.CSS_SELECTOR, '.ng-binding')
    LOCATOR_TRANSACTIONS_BTN = (By.CSS_SELECTOR, '[ng-click="transactions()"]')

    LOCATOR_WITHDRAWL_BTN = (By.CSS_SELECTOR, '[ng-click="withdrawl()"]')
    LOCATOR_DEPOSIT_BTN = (By.CSS_SELECTOR, '[ng-click="deposit()"]')
    LOCATOR_DEP_WIT_FLD = (By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input')
    LOCATOR_DO_DEP_WIT = (By.CSS_SELECTOR, '[type="submit"]')

    LOCATOR_CHANGE_CURRENCY = (By.XPATH, '//*[@id="accountSelect"]')
    LOCATOR_START_CURRENCY = (By.XPATH, '//*[@id="accountSelect"]/option[1]')
    LOCATOR_SECOND_CURRENCY = (By.XPATH, '//*[@id="accountSelect"]/option[2]')
    LOCATOR_BALACE_TEXT = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/strong[2]')


class CustomerPage(BasePage):

    def check_name_customer(self):
        customer_selector = self.find_element(CustomerPageLocators.LOCATOR_CUSTOMER_NAME)
        return customer_selector

    def check_login(self):
        load_dotenv()
        login = os.getenv("LOGIN")
        return login

    def click_deposit(self):
        dep_btn = self.find_element(CustomerPageLocators.LOCATOR_DEPOSIT_BTN).click()

    def write_deposit(self):
        deposit = fibonacci()
        dep_fld_send_keys = self.find_element(CustomerPageLocators.LOCATOR_DEP_WIT_FLD).send_keys(deposit)

    def do_deposit(self):
        dep_btn = self.find_element(CustomerPageLocators.LOCATOR_DO_DEP_WIT).click()

    def update_balance(self):
        change_currency = self.find_element(CustomerPageLocators.LOCATOR_CHANGE_CURRENCY).click()
        second_curency = self.find_element(CustomerPageLocators.LOCATOR_SECOND_CURRENCY).click()
        change_currency = self.find_element(CustomerPageLocators.LOCATOR_CHANGE_CURRENCY).click()
        start_currency = self.find_element(CustomerPageLocators.LOCATOR_START_CURRENCY).click()
        balance = self.find_element(CustomerPageLocators.LOCATOR_BALACE_TEXT)
        return balance

    def take_deposit(self):
        balance = fibonacci()
        return str(balance)

    def click_withdrawl(self):
        self.driver.refresh()
        self.find_element(CustomerPageLocators.LOCATOR_WITHDRAWL_BTN).click()

    def write_withdrawl(self):
        deposit = fibonacci()
        with_fld_send_keys = self.find_element(CustomerPageLocators.LOCATOR_DEP_WIT_FLD).send_keys(deposit)

    def do_withdrawl(self):
        with_btn = self.find_element(CustomerPageLocators.LOCATOR_DO_DEP_WIT).click()

    def go_to_transactions(self):
        transactions_btn = self.find_element(CustomerPageLocators.LOCATOR_TRANSACTIONS_BTN).click()
        return TransactionsPage(self.driver)