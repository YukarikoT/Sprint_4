import allure
from data import ValidUserData
from urls import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderPage:

    @allure.title('Проверка создания нового заказа с валидными данными через кнопку'
                  ' "Заказать" в верхней части страницы.')
    @allure.description('В верхней части страницы ищем элемент - кнопку "Заказать", нажимаем на него и переходим'
                        ' к формам для оформления заказа. Заполняем обязательные поля произвольными валидными данными.'
                        'Делаем заказ. Подтверждаем его. Проверяем, что получили окно об успешном создании заказа.')
    def test_make_order_from_header_order_button_success(self, browser):
        browser.get(Urls.MainPageUrl)
        MainPage(browser).click_cookie_confirm_button()
        MainPage(browser).click_header_order_button()
        first_name = ValidUserData.NewUserFirstName
        last_name = ValidUserData.NewUserLastName
        address = ValidUserData.NewUserAddress
        phone = ValidUserData.NewUserPhone
        order_date = ValidUserData.OrderDate
        OrderPage(browser).make_new_order(first_name, last_name, address, phone, order_date)
        OrderPage(browser).get_order_number()
        assert ValidUserData.TextOrderSuccessButton == OrderPage(browser).check_success_order_popup()

    @allure.title('Проверка создания нового заказа с валидными данными через кнопку "Заказать" на главной странице')
    @allure.description('На главной странице ищем элемент - кнопку "Заказать", нажимаем на него и переходим'
                        ' к формам для оформления заказа. Заполняем обязательные поля произвольными валидными данными.'
                        'Делаем заказ. Подтверждаем его. Проверяем, что получили окно об успешном создании заказа.')
    def test_make_order_from_main_order_button_success(self, browser):
        browser.get(Urls.MainPageUrl)
        MainPage(browser).click_cookie_confirm_button()
        MainPage(browser).scroll_to_order_big_button_and_click()
        first_name = ValidUserData.NewUserFirstName
        last_name = ValidUserData.NewUserLastName
        address = ValidUserData.NewUserAddress
        phone = ValidUserData.NewUserPhone
        order_date = ValidUserData.OrderDate
        OrderPage(browser).make_new_order(first_name, last_name, address, phone, order_date)
        OrderPage(browser).get_order_number()
        assert ValidUserData.TextOrderSuccessButton == OrderPage(browser).check_success_order_popup()








