from selenium.webdriver.common.by import By

class MainPageLocators:
    BigOrderButton = By.CLASS_NAME, "Home_FinishButton__1_cWm"
    CookieConfirmButton = By.ID, "rcc-confirm-button"

    ImpQuestionPrice = By.ID, "accordion__heading-0"
    ImpQuestion = By.ID, "accordion__heading-{}"
    ImpAnswer = By.ID, "accordion__panel-{}"