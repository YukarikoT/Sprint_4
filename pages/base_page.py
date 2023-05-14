import allure
from locators.base_page_locators import BasePageLocators

class BasePage:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, browser):
        self.driver = browser

    @allure.step('Нажимаем на кнопку "Заказать" в верхней части страницы')
    def click_header_order_button(self):
        self.driver.find_element(*BasePageLocators.HeaderOrderButton).click()

    @allure.step('Нажимаем на логотип "Яндекс"')
    def click_header_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.HeaderYandexLogo).click()

    @allure.step('Нажимаем на логотип "Самокат"')
    def click_header_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.HeaderScooterLogo).click()