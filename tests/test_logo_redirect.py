import allure
import pytest
from conftest import driver
from pages.main_page import MainPage


class TestLogoRedirect:
    @allure.title('Проверка перехода на главную страницу сервиса при клике на лого "Самокат" в шапке')
    def test_logo_redirect_to_main_success(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        assert "Дзен" in main_page.get_page_title(), f"Ожидался заголовок с 'Дзен', получен: {main_page.get_page_title()}"