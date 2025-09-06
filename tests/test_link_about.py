import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.product_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_link_about():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_driver_path = r'C:\Users\Cat\PycharmProjects02\resourse\chromedriver.exe'
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    time.sleep(10)

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish Test")
    time.sleep(10)
    driver.quit()


























































































































