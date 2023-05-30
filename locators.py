from selenium.webdriver.common.by import By


class Locators:
    REGISTER_NAME = [By.XPATH, "//label[text() = 'Имя']/parent::div/input"]  # Ввод имени при регистрации

    REGISTER_EMAIL = [By.XPATH, "//label[text() = 'Email']/parent::div/input"]  # Ввод email при регистрации

    REGISTER_BUTTON = [By.XPATH, "//button[text() = 'Зарегистрироваться']"]  # Кнопка регистрации

    REGISTER_LINK = [By.XPATH, "//a[@href = '/register']"]  #Ссылка "Зарегистрироваться" (переход на форму регистрации)

    INPUT_ERROR_CLASS = [By.CLASS_NAME, 'input__error']  # Сообщение с ошибкой ввода

    LOGIN_EMAIL = REGISTER_EMAIL  # Ввод email при логине

    LOGIN_BUTTON = [By.XPATH, "//button[text() = 'Войти']"]  # кнопка Войти (на странице логина)

    LOGIN_LINK = [By.XPATH, "//a[@href = '/login']"]  #Ссылка "Войти" на форме регистрации (переход на страницу логина)

    ACCOUNT_LINK = [By.XPATH, "//a[@href = '/account']"]  #Ссылка на Личный кабинет

    ACCOUNT_BUTTON = [By.XPATH, "//button[text() = 'Войти в аккаунт']"]  # Кнопка "Войти в аккаунт на главной"

    PLACE_ORDER_BUTTON = [By.XPATH, "//button[text() = 'Оформить заказ']"]  # Кнопка оформления заказа

    FORGOT_PASSWORD_LINK = [By.XPATH, "//a[@href = '/forgot-password']"]  #

    LOGOUT_BUTTON = [By.XPATH, "//button[text() = 'Выход']"]  #Кнопка Выxода

    PASSWORD_INPUT_NAME = [By.NAME, "Пароль"]

    BURGER_CONSTRUCTOR = [By.XPATH, "//p[contains(text(),'Конструктор')]/parent::a"]

    LOGO_STELLAR = [By.XPATH, "//div[contains(@class, 'logo')]/a"]

    SAUCES_BUTTON = [By.XPATH, "//span[contains(text(),'Соусы')]"]

    BUNS_BUTTON = [By.XPATH, "//span[contains(text(),'Булки')]"]

    FILLINGS_BUTTON = [By.XPATH, "// span[contains(text(), 'Начинки')]"]

    BUNS_HEADER = [By.XPATH, "//h2[contains(text(), 'Булки')]"]

    FILLINGS_HEADER = [By.XPATH, "//h2[contains(text(), 'Начинки')]"]

    SAUCES_HEADER = [By.XPATH, "//h2[contains(text(), 'Соусы')]"]

