import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на элемент')
    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step('Скролл страницы до элемента')
    def scroll_page_till_element(self, element):
        element_new = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_new)

    @allure.step('Ждём видимость элемента')
    def wait_for_element_visibility(self, element):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(element))

    @allure.step('Ждём, когда элемент станет кликабельным и нажимаем на него')
    def wait_for_element_clickable_and_click(self, element):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(element)).click()

    @allure.step('Заполняем поле данными')
    def set_data(self, element, user_data):
        self.driver.find_element(*element).send_keys(user_data)

    @allure.step('Получаем текст элемента')
    def get_element_text(self, element):
        return self.driver.find_element(*element).text