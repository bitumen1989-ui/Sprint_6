import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from url import QA_SCOOTER_URL
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.epic("Главная страница")
class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = QA_SCOOTER_URL
        self.MAIN_PAGE_HEADER = MainPageLocators.MAIN_PAGE_HEADER

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.BUTTON_ACCEPT_COOKIES)
        except:
            pass

    # ============ Логотипы ============

    @allure.step("Дождаться видимости логотипа 'Самокат' в хедере")
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_for_element_visible(MainPageLocators.HEADER_LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип 'Самокат' в хедере")
    def click_on_header_logo_scooter(self):
        self.click_element(MainPageLocators.HEADER_LOGO_SCOOTER)

    @allure.step("Дождаться видимости логотипа 'Яндекс' в хедере")
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_for_element_visible(MainPageLocators.HEADER_LOGO_YANDEX)

    @allure.step("Кликнуть на логотип 'Яндекс' в хедере")
    def click_on_header_logo_yandex(self):
        self.click_element(MainPageLocators.HEADER_LOGO_YANDEX)

    @allure.step("Переключиться на следующую вкладку и дождаться загрузки")
    def switch_to_next_tab(self):
        """Переключиться на следующую вкладку и дождаться загрузки."""
        self.switch_to_window(1)
        self.wait_for_url_contains("dzen.ru")
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.title) > 0
        )
        time.sleep(0.5)

    @allure.step("Получить заголовок страницы")
    def get_page_title(self):
        return self.driver.title

    @allure.step("Проверить отображение заголовка главной страницы")
    def check_displaying_of_main_header(self):
        return self.is_element_displayed(MainPageLocators.MAIN_PAGE_HEADER)

    # ============ Кнопки заказа ============

    @allure.step("Нажать кнопку 'Заказать' вверху страницы")
    def click_order_button_above(self):
        self.click_element(MainPageLocators.BUTTON_ORDER_ABOVE)

    @allure.step("Нажать кнопку 'Заказать' внизу страницы")
    def click_order_button_below(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_BELOW)
        self.click_element(MainPageLocators.BUTTON_ORDER_BELOW)

    # ============ FAQ ============

    @allure.step("Прокрутить до раздела 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.QUESTION_ONE)

    @allure.step("Дождаться видимости вопроса #{question_number}")
    def wait_visibility_of_faq_items(self, question_number):
        questions = [
            MainPageLocators.QUESTION_ONE,
            MainPageLocators.QUESTION_TWO,
            MainPageLocators.QUESTION_THREE,
            MainPageLocators.QUESTION_FOUR,
            MainPageLocators.QUESTION_FIVE,
            MainPageLocators.QUESTION_SIX,
            MainPageLocators.QUESTION_SEVEN,
            MainPageLocators.QUESTION_EIGHT,
        ]
        self.wait_for_element_visible(questions[question_number])

    @allure.step("Кликнуть на вопрос #{question_number}")
    def click_on_faq_items(self, question_number):
        questions = [
            MainPageLocators.QUESTION_ONE,
            MainPageLocators.QUESTION_TWO,
            MainPageLocators.QUESTION_THREE,
            MainPageLocators.QUESTION_FOUR,
            MainPageLocators.QUESTION_FIVE,
            MainPageLocators.QUESTION_SIX,
            MainPageLocators.QUESTION_SEVEN,
            MainPageLocators.QUESTION_EIGHT,
        ]
        self.scroll_to_element(questions[question_number])
        self.wait_for_element_clickable(questions[question_number])
        self.click_element_js(questions[question_number])

    @allure.step("Дождаться видимости ответа на вопрос #{question_number}")
    def wait_visibility_of_faq_answer(self, question_number):
        answers = [
            MainPageLocators.ANSWER_ONE,
            MainPageLocators.ANSWER_TWO,
            MainPageLocators.ANSWER_THREE,
            MainPageLocators.ANSWER_FOUR,
            MainPageLocators.ANSWER_FIVE,
            MainPageLocators.ANSWER_SIX,
            MainPageLocators.ANSWER_SEVEN,
            MainPageLocators.ANSWER_EIGHT,
        ]
        self.wait_for_element_visible(answers[question_number])

    @allure.step("Получить текст ответа на вопрос #{question_number}")
    def get_displayed_text_from_faq_answer(self, question_number):
        answers = [
            MainPageLocators.ANSWER_ONE,
            MainPageLocators.ANSWER_TWO,
            MainPageLocators.ANSWER_THREE,
            MainPageLocators.ANSWER_FOUR,
            MainPageLocators.ANSWER_FIVE,
            MainPageLocators.ANSWER_SIX,
            MainPageLocators.ANSWER_SEVEN,
            MainPageLocators.ANSWER_EIGHT,
        ]
        return self.get_text_from_element(answers[question_number])