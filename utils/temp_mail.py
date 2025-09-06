import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class TempMailService:
    """Класс для работы с временной почтой через Boomlify"""
    
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://boomlify.com/ru/temp-mail-instant/"
        self.current_email = None
        
    def get_temp_email(self):
        """Получает временный email с сайта Boomlify"""
        try:
            print("Переходим на сайт временной почты...")
            self.driver.get(self.base_url)
            time.sleep(3)
            
            # Ждем загрузки страницы и ищем поле с email
            email_selectors = [
                "//input[@id='email']",
                "//input[contains(@class, 'email')]",
                "//input[contains(@placeholder, 'email')]",
                "//div[contains(@class, 'email')]//input",
                "//span[contains(@class, 'email')]",
                "//div[contains(text(), '@')]",
                "//input[@type='email']"
            ]
            
            email_element = None
            for selector in email_selectors:
                try:
                    email_element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, selector)))
                    if email_element:
                        break
                except TimeoutException:
                    continue
            
            if not email_element:
                # Пробуем найти email в тексте страницы
                try:
                    email_element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '@')]")))
                except TimeoutException:
                    pass
            
            if email_element:
                # Получаем значение email
                if email_element.tag_name == 'input':
                    email_value = email_element.get_attribute('value')
                else:
                    email_value = email_element.text
                
                if email_value and '@' in email_value:
                    self.current_email = email_value.strip()
                    print(f"Получен временный email: {self.current_email}")
                    return self.current_email
                else:
                    # Пробуем найти email в атрибутах
                    email_value = email_element.get_attribute('data-email') or email_element.get_attribute('data-value')
                    if email_value and '@' in email_value:
                        self.current_email = email_value.strip()
                        print(f"Получен временный email: {self.current_email}")
                        return self.current_email
            
            # Если не нашли через селекторы, пробуем через JavaScript
            try:
                email_js = self.driver.execute_script("""
                    var elements = document.querySelectorAll('*');
                    for (var i = 0; i < elements.length; i++) {
                        var text = elements[i].textContent || elements[i].value || '';
                        if (text.includes('@') && text.includes('.')) {
                            return text.trim();
                        }
                    }
                    return null;
                """)
                
                if email_js and '@' in email_js:
                    self.current_email = email_js.strip()
                    print(f"Получен временный email через JS: {self.current_email}")
                    return self.current_email
                    
            except Exception as e:
                print(f"Ошибка при получении email через JS: {e}")
            
            print("Не удалось получить временный email")
            return None
            
        except Exception as e:
            print(f"Ошибка при получении временного email: {e}")
            return None
    
    def generate_new_email(self):
        """Генерирует новый временный email"""
        try:
            # Ищем кнопку "Изменить" или "Новый email"
            change_selectors = [
                "//button[contains(text(), 'Изменить')]",
                "//button[contains(text(), 'Новый')]",
                "//button[contains(text(), 'Generate')]",
                "//a[contains(text(), 'Изменить')]",
                "//button[contains(@class, 'change')]",
                "//button[contains(@class, 'generate')]"
            ]
            
            for selector in change_selectors:
                try:
                    change_button = WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, selector)))
                    change_button.click()
                    print("Нажата кнопка изменения email")
                    time.sleep(2)
                    break
                except TimeoutException:
                    continue
            
            # Получаем новый email
            return self.get_temp_email()
            
        except Exception as e:
            print(f"Ошибка при генерации нового email: {e}")
            return None
    
    def get_inbox_messages(self):
        """Получает список сообщений из временного почтового ящика"""
        try:
            # Ищем контейнер с сообщениями
            inbox_selectors = [
                "//div[contains(@class, 'inbox')]",
                "//div[contains(@class, 'message')]",
                "//div[contains(@class, 'email')]",
                "//ul[contains(@class, 'messages')]"
            ]
            
            messages = []
            for selector in inbox_selectors:
                try:
                    inbox_elements = self.driver.find_elements(By.XPATH, selector)
                    for element in inbox_elements:
                        text = element.text.strip()
                        if text and len(text) > 10:  # Фильтруем пустые элементы
                            messages.append(text)
                    if messages:
                        break
                except NoSuchElementException:
                    continue
            
            return messages
            
        except Exception as e:
            print(f"Ошибка при получении сообщений: {e}")
            return []
    
    def wait_for_message(self, timeout=60):
        """Ждет появления нового сообщения в почтовом ящике"""
        try:
            print(f"Ожидание сообщения в течение {timeout} секунд...")
            start_time = time.time()
            
            while time.time() - start_time < timeout:
                messages = self.get_inbox_messages()
                if messages:
                    print(f"Получено {len(messages)} сообщений")
                    return messages
                
                time.sleep(2)
                self.driver.refresh()  # Обновляем страницу для получения новых сообщений
            
            print("Время ожидания истекло, сообщений не получено")
            return []
            
        except Exception as e:
            print(f"Ошибка при ожидании сообщения: {e}")
            return []


def get_temp_email_simple():
    """Простая функция для получения временного email без использования Selenium"""
    try:
        # Используем API или простой парсинг
        response = requests.get("https://boomlify.com/ru/temp-mail-instant/", timeout=10)
        if response.status_code == 200:
            # Простой поиск email в HTML
            import re
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, response.text)
            if emails:
                return emails[0]
    except Exception as e:
        print(f"Ошибка при получении email через requests: {e}")
    
    return None
