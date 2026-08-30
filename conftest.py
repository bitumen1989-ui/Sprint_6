import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from url import QA_SCOOTER_URL  # ← Импортируем URL


@pytest.fixture(scope="function")
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    firefox_options.set_preference("browser.privatebrowsing.autostart", True)
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(QA_SCOOTER_URL)  # ← Используем URL из url.py
    yield driver
    driver.quit()