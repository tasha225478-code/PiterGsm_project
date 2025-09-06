import time
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Filters_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    filter_memory = "//span[contains(text(), '512')]"
    filter_RAM = "//span[@class='filter__item-text-option' and text()='24 GB']"
    CPU = "//div[@data-prop-code='CPU_LINEUP']//button[contains(@class,'js_toggle_trigger')]"
    filter_CPU = "//span[@class='filter__item-text-option' and normalize-space(text())='Apple M3']"
    CORES = "//div[@data-prop-code='CPU_CORES_PIN_TO_TOP']//button[contains(@class,'js_toggle_trigger')]"
    filter_cores = "//span[@class='filter__item-text-option' and text()='10']"
    colour = "//button[contains(@class, 'js_toggle_trigger') and .//span[contains(text(), 'Цвет')]]"
    filter_color = "//span[contains(text(), 'Серый космос')]"
    apply_button = "//button[contains(@class, 'btn_cta') and normalize-space()='Показать товары']"
    cookie_consent_btn = "//button[@id='cookie-consent-btn']"

    # Геттеры
    def get_filter_memory(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.filter_memory)))

    def get_filter_RAM(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.filter_RAM)))

    def get_CPU(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.CPU)))

    def get_filter_CPU(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.filter_CPU)))

    def get_CORES(self):
        return WebDriverWait(self.driver, 80).until(EC.element_to_be_clickable((By.XPATH, self.CORES)))

    def get_filter_cores(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.filter_cores)))

    def get_colour(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.colour)))

    def get_filter_color(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.filter_color)))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.apply_button)))

    # Вспомогательные методы
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
            # Попытка закрыть баннер и кликнуть снова через JS
            self.close_cookie_if_present()
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_expression))
                )
                self.scroll_into_view(element)
                self.driver.execute_script("arguments[0].click();", element)
            except Exception:
                # последний ретрай обычным кликом
                element.click()

    # Действия
    def click_filter_memory(self):
        try:
            self.safe_click(self.filter_memory)
            print("Clicked filter memory successfully")
        except Exception as e:
            print(f"Error clicking filter memory: {e}")
            raise

    def click_filter_RAM(self):
        self.safe_click(self.filter_RAM)
        print("Clicked filter_RAM")

    def click_CPU(self):
        self.safe_click(self.CPU)
        print("Clicked CPU")

    def click_filter_CPU(self):
        self.safe_click(self.filter_CPU)
        print("Clicked filter CPU")

    def click_CORES(self):
        time.sleep(0.2)
        self.safe_click(self.CORES)
        print("Clicked link CORES")

    def click_filter_cores(self):
        self.safe_click(self.filter_cores)
        print("Clicked filter cores")

    def click_colour(self):
        self.safe_click(self.colour)
        print("Clicked link colour")

    def click_filter_color(self):
        self.safe_click(self.filter_color)
        print("Clicked filter color")

    def click_apply_button(self):
        self.safe_click(self.apply_button)
        print("Clicked apply button")

    # Methods
    def apply_filters(self):
        try:
            print("Starting to apply filters...")
            self.close_cookie_if_present()

            # Клик на фильтр памяти
            self.click_filter_memory()
            print("Memory filter applied")

            # Клик на фильтр RAM
            # self.click_filter_RAM()
            # print("RAM filter applied")

            # Открытие секции выбора CPU
            self.click_CPU()
            print("CPU section opened")

            # Выбор конкретного CPU
            self.click_filter_CPU()
            print("CPU filter applied")

            # Раскрываем количество ядер процессора
            # self.click_CORES()
            # print("CORES section opened")
            #
            # # Фильтруем по количеству ядер
            # self.click_filter_cores()
            # print("CORES filter applied")

            # Раскрываем выбор цвета
            self.click_colour()
            print("Colour section opened")

            # # Фильтруем по цвету
            # self.click_filter_color()
            # print("Color filter applied")

            # Применяем фильтры
            time.sleep(5)
            self.click_apply_button()
            print("Filters applied successfully!")
        except Exception as e:
            print(f"Error applying filters: {e}")
            raise
