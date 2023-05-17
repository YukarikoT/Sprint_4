import allure
from urls import Urls
import time
from pages.main_page import MainPage


class TestBasePage:

    @allure.title('Проверка нажатия на логотип "Яндекс"')
    @allure.description('На странице ищем логотип "Яндекс" и проверяем,'
                        ' что нажатие на него ведёт на главную страницу Яндекса')
    def test_check_yandex_logo_link(self, browser):
        browser.get(Urls.MainPageUrl)
        MainPage(browser).click_cookie_confirm_button()
        MainPage(browser).click_header_yandex_logo()
        window_before = browser.window_handles[0]
        MainPage(browser).click_header_yandex_logo()
        time.sleep(3)
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        assert browser.current_url == Urls.YandexMainUrl, \
            'Клик по логотипу "Яндекс" не ведёт на Главную страницу Яндекса'

    @allure.title('Проверка нажатия на логотип "Самокат"')
    @allure.description('На странице ищем логотип "Самокат" и проверяем,'
                        ' что нажатие на него ведёт на главную страницу сервиса "ЯндексСамокат"')
    def test_check_scooter_logo_link(self, browser):
        browser.get(Urls.OrderPageUrl)
        MainPage(browser).click_header_scooter_logo()
        assert browser.current_url == Urls.MainPageUrl, \
            'Клик по логотипу "Самокат" не ведёт на Главную страницу ЯндексСамокат'