from datetime import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def assert_logo_alt(self, expected_alt: str):
        logo = self.get_main_word()
        actual_alt = logo.get_attribute('alt') or ''
        assert actual_alt == expected_alt, f"Logo alt mismatch. Expected: {expected_alt}, got: {actual_alt}"
        print("Good value logo")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d.%H.%M")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Cat\\PycharmProjects02\\main_project\\screen\\' + name_screenshot)
        print("Screen done")

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")