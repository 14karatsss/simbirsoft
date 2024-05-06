import allure

from Pages.LogiPage import DoLogin

import time

@allure.feature('parcing')
@allure.story('create csv file')
@allure.severity('critical')
def test_parcing(browser):
    main_page = DoLogin(browser)
    main_page.go_to_site()
    main_page.choose_customer()
    element = main_page.check_user_select()
    assert "---Your Name---" in element.text
    main_page.choose_user()
    customer_page = main_page.login()
    time.sleep(1)
    element = customer_page.check_name_customer()
    login = customer_page.check_login()
    assert login in element.text
    customer_page.click_deposit()
    customer_page.write_deposit()
    customer_page.do_deposit()
    balance = customer_page.update_balance()
    deposit = customer_page.take_deposit()
    assert deposit in balance.text
    customer_page.click_withdrawl()
    customer_page.write_withdrawl()
    customer_page.do_withdrawl()
    balance = customer_page.update_balance()
    assert "0" in balance.text
    transactions_page = customer_page.go_to_transactions()
    element = transactions_page.check_back_btn()
    assert "Back" in element.text
    count = transactions_page.count_row_table()
    assert 2 == count[0]
    transactions_page.parsing_csv(count[1])

