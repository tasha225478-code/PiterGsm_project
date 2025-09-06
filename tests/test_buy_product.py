import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.filters_page import Filters_page
from pages.product_page import Product_page
from pages.cart_page import Cart_page
from pages.finish_page import Finish_page

# @pytest.mark.order(3)
def test_buy_product_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_driver_path = r'C:\Users\Cat\PycharmProjects02\resourse\chromedriver.exe'
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    time.sleep(10)
    print("Start Test 1")

    # Авторизация
    login = Login_page(driver)
    login.authorization()
    #
    mp = Main_page(driver)
    mp.select_link()

    fp = Filters_page(driver)
    fp.apply_filters()

    pp = Product_page(driver)
    pp.product_confirmation()

    cp = Cart_page(driver)
    cp.to_cart()

    f = Finish_page(driver)
    f.finish()
#
#     time.sleep(10)
#     driver.quit()
#

#
