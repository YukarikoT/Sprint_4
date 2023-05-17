import allure
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажимаем кнопку для подтверждения использования cookies')
    def click_cookie_confirm_button(self):
        element = MainPageLocators.CookieConfirmButton
        self.click_on_element(element)

    @allure.step('Нажимаем на кнопку "Заказать" в верхней части страницы')
    def click_header_order_button(self):
        self.wait_for_element_clickable_and_click(BasePageLocators.HeaderOrderButton)

    @allure.step('Нажимаем на логотип "Яндекс"')
    def click_header_yandex_logo(self):
        self.wait_for_element_clickable_and_click(BasePageLocators.HeaderYandexLogo)

    @allure.step('Нажимаем на логотип "Самокат"')
    def click_header_scooter_logo(self):
        self.click_on_element(BasePageLocators.HeaderScooterLogo)

    @allure.step('Нажимаем кнопку "Заказать" на главной странице')
    def click_big_order_button(self):
        self.click_on_element(MainPageLocators.BigOrderButton)

    @allure.step('Скроллим до раздела "Важные вопросы" в конце главной страницы')
    def scroll_to_important_questions(self):
        self.scroll_page_till_element(MainPageLocators.ImpQuestionPrice)

    @allure.step('Ждём появление раздела "Важные вопросы"')
    def wait_for_important_questions(self):
        self.wait_for_element_visibility(MainPageLocators.ImpQuestionPrice)

    @allure.step('Скроллим до кнопки "Заказать" в центре страницы и нажимаем на неё')
    def scroll_to_order_big_button_and_click(self):
        self.wait_for_element_clickable_and_click(MainPageLocators.BigOrderButton)

    @allure.step('Проверяем видимость всплывающего окна ya.ru и получаем его текст')
    def ya_ru_check_popup_text(self):
        self.wait_for_element_visibility(BasePageLocators.YaRuPopUP)
        self.get_element_text(BasePageLocators.YaRuPopUP)