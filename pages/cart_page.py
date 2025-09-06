from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    go_to_cart_and_go = "//a[@class='btn btn_cta' and contains(text(), 'Перейти в корзину')]"
    main_cart_word = "//h1[@class='section__title' and text()='Корзина']"
    prodcard_price_current = "//div[@class='cart-prodcard__price-current']"
    total_price = "//div[@class='total__price']"
    go_to_checkout= "//a[@class='btn btn_cta' and contains(text(), 'Перейти к оформлению')]"
    main_check_word = "//h1[@class='section__title'][contains(text(), 'Оформление')]"

    card_price = "//div[@class='product__price' and @itemprop='offers']"



    # Геттеры

    def get_go_to_cart_and_go(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_and_go)))

    def get_main_cart_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.main_cart_word)))
    def get_prodcard_price_current(self):
        return WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.prodcard_price_current))).text.strip()

    def get_total_price(self):
        return WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.total_price))).text.strip()

    def get_go_to_checkout(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.go_to_checkout)))

    def get_main_check_word(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.main_check_word)))

    def get_card_price(self):
        return WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.card_price))).text.strip()



    # Действия

    def click_go_to_cart_and_go(self):
        self.get_go_to_cart_and_go().click()

    def click_go_to_checkout(self):
        self.get_go_to_checkout().click()

    # Методы

    def to_cart(self, product_card_price=None):
        self.get_current_url()
        self.click_go_to_cart_and_go()
        self.assert_word(self.get_main_cart_word(), "Корзина")


        # Получение текущего значения цены товара и общей суммы заказа
        current_product_price = self.get_prodcard_price_current()
        total_order_price = self.get_total_price()

        # Выведем полученные значения
        print(f"Текущая цена товара: {current_product_price}")
        print(f"Общая сумма заказа: {total_order_price}")
        if product_card_price:
            print(f"Цена товара в карточке (переданная): {product_card_price}")

        # Преобразование строковых значений в численные (убираем знаки валюты и преобразовываем строку в число)
        try:
            float_current_price = float(current_product_price.replace(' ', '').replace('руб.', ''))
            float_total_price = float(total_order_price.replace(' ', '').replace('руб.', ''))

            # Сравнение цены товара в корзине с общей суммой заказа
            if float_current_price == float_total_price:
                print("Цена товара в корзине равна общей сумме заказа.")
            else:
                print("Внимание! Цена товара не равна общей сумме заказа!")


        except ValueError:
            print("Ошибка преобразования цены в число.")

        print("Add to cart successful")

        self.click_go_to_checkout()
        self.assert_word(self.get_main_check_word(), "Оформление заказа")
        print("Click go to checkout")

