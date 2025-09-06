import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    url = 'https://pitergsm.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    # button_entrance = "//button[@class='hcontrols__item js_popup_trigger isinit']"
    # user_name = "//input[@placeholder='Логин']"
    # password = "//input[@placeholder='Пароль']"
    # button_login = "//button[@type='submit' and text()='Войти']"
    # logout_button = "//a[text()='Выйти']"
    main_word = "//img[@class='header__logo-img' and @alt='PiterGSM']"

    # Геттеры
    # def get_button_entrance(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_entrance)))
    #
    # def get_user_name(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    #
    # def get_password(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    #
    # def get_button_login(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))
    #
    # def get_logout_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.logout_button)))
    #
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.main_word)))



    # Действия
    # def click_button_entrance(self):
    #     time.sleep(2)
    #     self.get_button_entrance().click()
    #     print("Click button_entrance")
    #
    # def input_user_name(self, user_name):
    #     self.get_user_name().clear()
    #     self.get_user_name().send_keys(user_name)
    #     print("Input user name")
    #
    # def input_password(self, password):
    #     self.get_password().clear()
    #     self.get_password().send_keys(password)
    #     print("Input password")
    #     time.sleep(10)
    # def click_button_login(self):
    #     # time.sleep(5)
    #     self.get_button_login().click()
    #     print("Click button_login")
    #
    # def check_successful_authorization(self):
    #     try:
    #         # Ждем появление кнопки "Выйти" до определенного таймаута (например, 30 сек.)
    #         logout_button = WebDriverWait(self.driver, 60).until(
    #             EC.visibility_of_element_located((By.XPATH, self.logout_button)))
    #
    #         # Если элемент найден, выводим сообщение успеха
    #         print("Logout button success")
    #
    #     except TimeoutException:
    #         print("Logout button not found")

    # Методы
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_logo_alt("PiterGSM")
        # self.click_button_entrance()
        # self.input_user_name("testuser22")
        # self.input_password("TestUser12345678!")
        # self.click_button_login()
        # self.check_successful_authorization()

