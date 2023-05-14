import allure
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class OrderPage:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, browser):
        self.driver = browser

    @allure.step('Создаём новый заказ через кнопку "Заказать" в верхней части страницы')
    def make_new_order(self, first_name, last_name, address, phone, order_date):
        self.driver.find_element(*OrderPageLocators.InputFirstName).send_keys(first_name)
        self.driver.find_element(*OrderPageLocators.InputLastName).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.InputAddress).send_keys(address)
        self.driver.find_element(*OrderPageLocators.SelectSubway).click()
        self.driver.find_element(*OrderPageLocators.Subway).click()
        self.driver.find_element(*OrderPageLocators.InputPhoneNumber).send_keys(phone)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(OrderPageLocators.NextButton)).click()
        self.driver.find_element(*OrderPageLocators.InputDate).send_keys(order_date)
        self.driver.find_element(*OrderPageLocators.SelectHowLong).click()
        self.driver.find_element(*OrderPageLocators.HowLong).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(OrderPageLocators.MakeOrderButton)).click()
        self.driver.find_element(*OrderPageLocators.PopUpConfirm).click()

    @allure.step('Создаём новый заказ через кнопку "Заказать" на главной странице')
    def check_success_order_popup(self):
        return self.driver.find_element(*OrderPageLocators.CheckOrderButton).text

    @allure.step('Получаем номер и сообщение при успешном заказе')
    def get_order_number(self):
        print(self.driver.find_element(*OrderPageLocators.SuccessOrderMessage).text)

