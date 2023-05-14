import allure
import time
from data import TestData
from pages.main_page import MainPage
from pages.base_page import BasePage


class TestBasePage:

    @allure.title('Проверка нажатия на логотип "Яндекс"')
    @allure.description('На странице ищем логотип "Яндекс" и проверяем,'
                        ' что нажатие на него ведёт на главную страницу Яндекса')
    def test_check_yandex_logo_link(self, browser):
        browser.get(TestData.MainPageUrl)
        base_page = BasePage(browser)
        main_page = MainPage(browser)
        main_page.click_cookie_confirm_button()
        window_before = browser.window_handles[0]
        base_page.click_header_yandex_logo()
        time.sleep(3)
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        assert browser.current_url == TestData.YandexMainUrl, \
            'Клик по логотипу "Яндекс" не ведёт на Главную страницу Яндекса'

    @allure.title('Проверка нажатия на логотип "Самокат"')
    @allure.description('На странице ищем логотип "Самокат" и проверяем,'
                        ' что нажатие на него ведёт на главную страницу сервиса "ЯндексСамокат"')
    def test_check_scooter_logo_link(self, browser):
        browser.get(TestData.OrderPageUrl)
        base_page = BasePage(browser)
        base_page.click_header_scooter_logo()
        assert browser.current_url == TestData.MainPageUrl, \
            'Клик по логотипу "Самокат" не ведёт на Главную страницу ЯндексСамокат'