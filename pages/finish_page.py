from selenium import webdriver
from os import name

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.base_class import Base


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FIO ="//input[@name='ORDER_PROP_1']"
    email = "//input[@name='ORDER_PROP_2']"
    number_phone = "//input[@name='ORDER_PROP_3']"
    final_price = "//span[@class='m-nowrap js-order-price']"
    button_order ="//button[contains(@class, 'btn btn_cta') and normalize-space()='Оформить заказ']"

    # Getters
    def get_FIO(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.FIO)))
    def get_email(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_number_phone(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.number_phone)))

    def get_final_price(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.final_price)))

    def get_button_order(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_order)))

    # Actions

    def input_FIO(self, FIO):
        self.get_FIO().send_keys(FIO)
        print("input first FIO")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("input email")

    def input_number_phone(self, number_phone):
        self.get_number_phone().send_keys(number_phone)
        print("input number phone")

    def click_button_order(self):
        self.get_button_order().click()
        print("Click button_order")


    # Methods
    def finish(self):
        self.get_current_url()
        self.input_FIO("Иванов Иван Иванович")
        self.input_email("crulksb@king.vsmailpro.com")
        self.input_number_phone("79999999999")
        self.click_button_order()
        # self.assert_url('https://pitergsm.ru/personal/order/make/?ORDER_ID')
        self.get_screenshot()