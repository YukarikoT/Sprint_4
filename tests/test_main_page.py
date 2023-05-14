import allure
import pytest
from data import TestData
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    driver = None

    @pytest.mark.parametrize(
        'question, answer, result',
        [
            [0, 0, TestData.AnswerTextPrice],
            [1, 1, TestData.AnswerTextMany],
            [2, 2, TestData.AnswerTextTime],
            [3, 3, TestData.AnswerTextToday],
            [4, 4, TestData.AnswerTextReturn],
            [5, 5, TestData.AnswerTextCharge],
            [6, 6, TestData.AnswerTextCancel],
            [7, 7, TestData.AnswerTextMkad]
        ]
    )
    @allure.title('Проверка соответствия вопросов и ответов в разделе "Важные вопросы"')
    @allure.description('На главной странице ищем раздел "Важные вопросы", проверяем,'
                        'что каждый ответ соответствует заданным данным. Всего 8 проверок.')
    def test_check_important_question_description(self, browser, question, answer, result):
        browser.get(TestData.MainPageUrl)
        main_page = MainPage(browser)
        main_page.click_cookie_confirm_button()
        main_page.scroll_to_important_questions()
        method_q, locator_q = MainPageLocators.ImpQuestion
        locator_q = locator_q.format(question)
        element_question = browser.find_element(method_q, locator_q)
        method_a, locator_a = MainPageLocators.ImpAnswer
        locator_a = locator_a.format(answer)
        element_answer = browser.find_element(method_a, locator_a)
        main_page.wait_for_important_questions()
        element_question.click()
        text = element_answer.text
        assert text == result, 'Текст ответа не соответствует данным'