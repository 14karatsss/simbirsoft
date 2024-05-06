from selenium.webdriver.common.by import By

from Utils.BaseApp import BasePage
from Utils.GenerateCSV import parcing


class TransactionsPageLocators():
    LOCATOR_BACK_BTN = (By.CSS_SELECTOR, '[ng-click="back()"]')
    LOCATOR_TABEL = (By.XPATH, '//*[@ng-repeat]')


class TransactionsPage(BasePage):

    def check_back_btn(self):
        back_btn_selector = self.find_element(TransactionsPageLocators.LOCATOR_BACK_BTN)
        return back_btn_selector

    def count_row_table(self):
        table = self.find_elements(TransactionsPageLocators.LOCATOR_TABEL)
        rows = []
        for row in table:
            rows.append(row.text)

        count = len(table)
        parsing_list = rows
        return count, parsing_list

    def parsing_csv(self, table):
        table
        parcing(table)
