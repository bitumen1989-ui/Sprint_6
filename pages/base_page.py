from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def click_element_js(self, locator):
        """Кликнуть по элементу через JavaScript (обходит перекрытия)."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def switch_to_window(self, window_index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[window_index])

    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False

    def wait_for_url_contains(self, expected_text):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.url_contains(expected_text)
        )