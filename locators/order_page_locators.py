from selenium.webdriver.common.by import By

class OrderPageLocators:
    InputFirstName = By.XPATH, ".//div[2]/div[1]/input"
    InputLastName = By.XPATH, ".//div[2]/div[2]/input"
    InputAddress = By. XPATH, ".//div[2]/div[3]/input"
    SelectSubway = By. CLASS_NAME, "select-search__input"
    Subway = By.XPATH, ".//li[2]/button/div[2][text()='Черкизовская']"
    InputPhoneNumber = By.XPATH, ".//div[2]/div[5]/input"
    NextButton = By.XPATH, ".//button[text()='Далее']"
    InputDate = By.XPATH, ".//div[1]/div/input"
    SelectHowLong = By.CLASS_NAME, "Dropdown-arrow"
    HowLong = By.XPATH, ".//div[2][text()='двое суток']"
    MakeOrderButton = By.XPATH, ".//button[2][text()='Заказать']"
    PopUpConfirm = By.XPATH, ".//button[2][text()='Да']"
    PopUpOrderSuccess = By.CLASS_NAME, "Order_ModalHeader__3FDaJ"
    CheckOrderButton = By.XPATH, ".//button[text()='Посмотреть статус']"
    SuccessOrderMessage = By.CLASS_NAME, "Order_Text__2broi"
