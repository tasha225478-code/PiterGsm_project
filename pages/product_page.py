import time

import self
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    card_price = "//div[@class='product__price' and @itemprop='offers']"
    MAC = "//a[@class='prodcard__name' and contains(@href, '/noutbuk-apple-macbook-air-15-m3-8c-cpu-10c-gpu-2024-24-gb-512-gb-ssd-35-w-space-grey-seryy-kosmos-mc9h4/') and contains(normalize-space(), 'Apple MacBook Air 15') and contains(normalize-space(), 'серый космос')]"

    buy_button = "//div[@class='product__buy-btn btn btn_sm btn_cta buy_link' and @data-product-id='67676']"
    cookie_consent_btn = "//button[@id='cookie-consent-btn']"



    # Getters
    def get_card_price(self):
        element = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.card_price))
        )
        return element.text.strip()


    def get_MAC(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.MAC)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))


    # Actions
    def click_MAC(self):
        self.safe_click(self.MAC)
        print("Click MAC")
    def click_buy_button(self):
        self.safe_click(self.buy_button)
        print("Click buy button")

    # Methods

    def product_confirmation(self):
        self.get_current_url()
        self.click_MAC()
        card_card__price = self.get_card_price()

        # Выведем полученные значения
        print(f"Цена товара в карточке: {card_card__price}")


        self.click_buy_button()

    # Helpers
    def close_cookie_if_present(self):
        try:
            button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self.cookie_consent_btn))
            )
            try:
                button.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", button)
            time.sleep(0.5)
        except TimeoutException:
            pass

    def scroll_into_view(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
            time.sleep(0.2)
        except Exception:
            pass

    def safe_click(self, xpath_expression):
        self.close_cookie_if_present()
        element = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        self.scroll_into_view(element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.close_cookie_if_present()
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_expression))
                )
                self.scroll_into_view(element)
                self.driver.execute_script("arguments[0].click();", element)
            except Exception:
                element.click()



