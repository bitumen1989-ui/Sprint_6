import allure
from pages.base_page import BasePage
from locators.order_page_locators import (
    FirstFormSection,
    SecondFormSection,
    OrderConfirmationWindow,
    OrderIsCompletedWindow
)
from selenium.webdriver.common.by import By
import time


@allure.epic("Страница заказа")
class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Дождаться видимости элемента")
    def wait_visibility_of_element(self, locator):
        return self.wait_for_element_visible(locator)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        self.click_element(locator)

    @allure.step("Заполнить первую часть формы (персональные данные)")
    def data_entry_first_form(self, test_data):
        allure.attach(
            f"Имя: {test_data['FIRST_NAME']}\nФамилия: {test_data['SECOND_NAME']}\nАдрес: {test_data['ADDRESS']}\nТелефон: {test_data['PHONE_NUMBER']}\nСтанция метро: {test_data['METRO_STATION']}",
            name="Данные пользователя",
            attachment_type=allure.attachment_type.TEXT
        )
        
        self.send_keys_to_element(FirstFormSection.INPUT_FIRST_NAME, test_data['FIRST_NAME'])
        self.send_keys_to_element(FirstFormSection.INPUT_SECOND_NAME, test_data['SECOND_NAME'])
        self.send_keys_to_element(FirstFormSection.INPUT_ADDRESS, test_data['ADDRESS'])

        with allure.step("Выбрать станцию метро"):
            self.click_element(FirstFormSection.METRO_DROPDOWN_LIST_HIDDEN)
            metro_locator = (FirstFormSection.METRO_DROPDOWN_LIST_ELEMENT_BUTTON[0],
                            FirstFormSection.METRO_DROPDOWN_LIST_ELEMENT_BUTTON[1].format(test_data['METRO_STATION']))
            self.click_element(metro_locator)

        self.send_keys_to_element(FirstFormSection.INPUT_PHONE, test_data['PHONE_NUMBER'])
        
        with allure.step("Нажать кнопку 'Далее'"):
            self.click_element(FirstFormSection.BUTTON_NEXT)
            time.sleep(1)

    @allure.step("Заполнить вторую часть формы (данные об аренде)")
    def data_entry_second_form(self, test_data):
        allure.attach(
            f"Дата доставки: {test_data['DELIVERY_DATE']}\nПериод аренды: {test_data['RENTAL_PERIOD']}\nЦвет: {test_data['COLOR']}\nКомментарий: {test_data['COMMENT']}",
            name="Данные об аренде",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Ожидание загрузки второй формы"):
            self.wait_for_element_visible(SecondFormSection.ORDER_PAGE_HEADER)
            self.wait_for_element_visible(SecondFormSection.DATE_LIST_HIDDEN)

        with allure.step("Ввести дату доставки"):
            self.send_keys_to_element(SecondFormSection.DATE_LIST_HIDDEN, test_data['DELIVERY_DATE'])
            self.driver.find_element(By.TAG_NAME, "body").click()

        with allure.step("Выбрать период аренды"):
            self.click_element(SecondFormSection.RENTAL_PERIOD_LIST_HIDDEN)
            period_locator = (SecondFormSection.RENTAL_PERIOD_IS_NOT_SELECTED[0],
                             SecondFormSection.RENTAL_PERIOD_IS_NOT_SELECTED[1].format(test_data['RENTAL_PERIOD']))
            self.click_element(period_locator)

        with allure.step(f"Выбрать цвет: {test_data['COLOR']}"):
            if test_data['COLOR'] == "black":
                checkbox_black = (By.ID, "black")
                self.click_element(checkbox_black)
            elif test_data['COLOR'] == "grey":
                checkbox_grey = (By.ID, "grey")
                self.click_element(checkbox_grey)

        with allure.step("Ввести комментарий для курьера"):
            self.send_keys_to_element(SecondFormSection.INPUT_COMMENT, test_data['COMMENT'])

        with allure.step("Нажать кнопку 'Заказать'"):
            self.click_element(SecondFormSection.BUTTON_ORDER)

        with allure.step("Подтвердить заказ в модальном окне"):
            self.wait_for_element_visible(OrderConfirmationWindow.WINDOW_HEADER)
            self.click_element(OrderConfirmationWindow.BUTTON_CONFIRM)

    @allure.step("Проверить отображение кнопки 'Посмотреть статус'")
    def check_displaying_of_button_check_status_of_order(self):
        try:
            self.wait_for_element_visible(OrderIsCompletedWindow.BUTTON_CHECK_STATUS)
            return True
        except:
            return False