import allure
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainPage:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, browser):
        self.driver = browser

    @allure.step('Нажимаем кнопку для подтверждения использования cookies')
    def click_cookie_confirm_button(self):
        self.driver.find_element(*MainPageLocators.CookieConfirmButton).click()

    @allure.step('Прокручиваем главную страницу до кнопки "Заказать"')
    def scroll_to_order_big_button(self):
        big_order_button = self.driver.find_element(*MainPageLocators.BigOrderButton)
        self.driver.execute_script("arguments[0].scrollIntoView();", big_order_button)

    @allure.step('Прокручиваем главную страницу до секции "Важные вопросы"')
    def scroll_to_important_questions(self):
        questions = self.driver.find_element(*MainPageLocators.ImpQuestionPrice)
        self.driver.execute_script("arguments[0].scrollIntoView();", questions)

    @allure.step('Ждём видимости кнопки "Заказать"')
    def wait_for_order_big_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BigOrderButton))

    @allure.step('Ждём видимости секции "Важные вопросы"')
    def wait_for_important_questions(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ImpQuestionPrice))

    @allure.step('Нажимаем кнопку "Заказать" на главной странице')
    def click_big_order_button(self):
        self.driver.find_element(*MainPageLocators.BigOrderButton).click()