import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Создаём новый заказ через кнопку "Заказать" в верхней части страницы')
    def make_new_order(self, first_name, last_name, address, phone, order_date):
        self.set_data(OrderPageLocators.InputFirstName, first_name)
        self.set_data(OrderPageLocators.InputLastName, last_name)
        self.set_data(OrderPageLocators.InputAddress, address)
        self.click_on_element(OrderPageLocators.SelectSubway)
        self.click_on_element(OrderPageLocators.Subway)
        self.set_data(OrderPageLocators.InputPhoneNumber, phone)
        self.wait_for_element_clickable_and_click(OrderPageLocators.NextButton)
        self.set_data(OrderPageLocators.InputDate, order_date)
        self.click_on_element(OrderPageLocators.SelectHowLong)
        self.click_on_element(OrderPageLocators.HowLong)
        self.wait_for_element_clickable_and_click(OrderPageLocators.MakeOrderButton)
        self.click_on_element(OrderPageLocators.PopUpConfirm)

    @allure.step('Проверка, что заказ оформлен успешно')
    def check_success_order_popup(self):
        return self.get_element_text(OrderPageLocators.CheckOrderButton)

    @allure.step('Получаем номер и сообщение об успешном заказе')
    def get_order_number(self):
        print(self.get_element_text(OrderPageLocators.SuccessOrderMessage))