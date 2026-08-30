import allure
from pages.base_page import BasePage
from url import DZEN_URL  # ← Импортируем URL Дзена


@allure.epic("Управление окнами")
class SwitchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dzen_url = DZEN_URL

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        self.switch_to_window(1)

    @allure.step("Переключиться на окно по индексу {index}")
    def switch_to_window_by_index(self, index):
        self.switch_to_window(index)

    @allure.step("Закрыть текущее окно")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Получить количество открытых окон")
    def get_window_handles_count(self):
        return len(self.driver.window_handles)

    @allure.step("Открыть Дзен напрямую")
    def open_dzen_directly(self):
        """Открыть Дзен используя URL из url.py."""
        self.driver.get(self.dzen_url)

    @allure.step("Проверить, что открыт Дзен")
    def is_dzen_opened(self):
        """Проверить, что текущий URL содержит URL Дзена."""
        return self.dzen_url in self.driver.current_url