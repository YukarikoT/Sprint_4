from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--window-size=1200,900")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()