import random
import datetime


class ValidUserData:

    NewUserFirstNameList = ('Мария', 'Анна', 'Юлия', 'Алина', 'Елена', 'Ирина', 'София', 'Полина', 'Диана')
    NewUserFirstName = NewUserFirstNameList[random.randint(0, 8)]
    NewUserLastNameList = ('Ким', 'Пак', 'Кан', 'Чхве', 'Чон', 'Шин', 'Хван', 'Сон', 'Мун')
    NewUserLastName = NewUserLastNameList[random.randint(0, 8)]
    NewUserAddress = f"Ул.Ленина д.{random.randint(1, 100)}"
    NewUserPhone = f"8960{random.randint(1000000, 9999999)}"
    DateTomorrow = (datetime.date.today() + datetime.timedelta(days=1))
    OrderDate = str(DateTomorrow.strftime('%d/%m/%Y'))
    TextOrderSuccessButton = "Посмотреть статус"

class ImportantAnswers:

    AnswerTextPrice = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    AnswerTextMany = 'Пока что у нас так: один заказ — один самокат. Если хотите' \
                     ' покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    AnswerTextTime = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая' \
                     ' в течение дня. Отсчёт времени аренды начинается с момента, когда вы' \
                     ' оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная' \
                     ' аренда закончится 9 мая в 20:30.'
    AnswerTextToday = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    AnswerTextReturn = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по' \
                       ' красивому номеру 1010.'
    AnswerTextCharge = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — ' \
                       'даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    AnswerTextCancel = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим.' \
                       ' Все же свои.'
    AnswerTextMkad = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

class YaRuCheck:
    YaRuPopUpText = 'Сделать Яндекс основным поиском?'