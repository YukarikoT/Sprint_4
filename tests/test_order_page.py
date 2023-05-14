import allure
from data import TestData
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.order_page import OrderPage

class TestOrderPage:

    driver = None

    @allure.title('Проверка создания нового заказа с валидными данными через кнопку'
                  ' "Заказать" в верхней части страницы.')
    @allure.description('В верхней части страницы ищем элемент - кнопку "Заказать", нажимаем на него и переходим'
                        ' к формам для оформления заказа. Заполняем обязательные поля произвольными валидными данными.'
                        'Делаем заказ. Подтверждаем его. Проверяем, что получили окно об успешном создании заказа.')
    def test_make_order_from_header_order_button_success(self, browser):
        browser.get(TestData.MainPageUrl)
        main_page = MainPage(browser)
        base_page = BasePage(browser)
        order_page = OrderPage(browser)
        main_page.click_cookie_confirm_button()
        base_page.click_header_order_button()
        first_name = TestData.NewUserFirstName
        last_name = TestData.NewUserLastName
        address = TestData.NewUserAddress
        phone = TestData.NewUserPhone
        order_date = TestData.OrderDate
        order_page.make_new_order(first_name, last_name, address, phone, order_date)
        order_page.get_order_number()
        assert TestData.TextOrderSuccessButton == order_page.check_success_order_popup()

    @allure.title('Проверка создания нового заказа с валидными данными через кнопку "Заказать" на главной странице')
    @allure.description('На главной странице ищем элемент - кнопку "Заказать", нажимаем на него и переходим'
                        ' к формам для оформления заказа. Заполняем обязательные поля произвольными валидными данными.'
                        'Делаем заказ. Подтверждаем его. Проверяем, что получили окно об успешном создании заказа.')
    def test_make_order_from_main_order_button_success(self, browser):
        browser.get(TestData.MainPageUrl)
        main_page = MainPage(browser)
        order_page = OrderPage(browser)
        main_page.click_cookie_confirm_button()
        main_page.scroll_to_order_big_button()
        main_page.wait_for_order_big_button()
        main_page.click_big_order_button()
        first_name = TestData.NewUserFirstName
        last_name = TestData.NewUserLastName
        address = TestData.NewUserAddress
        phone = TestData.NewUserPhone
        order_date = TestData.OrderDate
        order_page.make_new_order(first_name, last_name, address, phone, order_date)
        order_page.get_order_number()
        assert TestData.TextOrderSuccessButton == order_page.check_success_order_popup()








