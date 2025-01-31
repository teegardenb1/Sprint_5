from selenium.webdriver.common.by import By

class Locators:
    # Поле ввода "Имя"
    register_name_field = (By.XPATH, './/label[text()="Имя"]/../input')
    # Поле ввода "Email"
    register_email_field = (By.XPATH, './/label[text()="Email"]/../input')
    # Поле ввода "Пароль"
    register_password_field = (By.XPATH, './/label[text()="Пароль"]/../input')
    # Кнопка "Зарегистрироваться"
    register_button = (By.XPATH, './/button[text()="Зарегистрироваться"]')
    # Кнопка "Восстановить пароль"
    recovery_password_button = (By.CLASS_NAME, 'Auth_link__1fOlj')
    # Сообщение об ошибке "Такой пользователь уже существует"
    user_exists_error = (By.XPATH, './/*[text()="Некорректный пароль"]')
    # Cссылка "Войти"
    register_login_link = (By.CLASS_NAME, 'Auth_link__1fOlj')
    # Поле ввода "Email"
    login_email_field = (By.XPATH, './/label[text()="Email"]/../input')
    # Поле ввода "Пароль"
    login_password_field = (By.XPATH, './/label[text()="Пароль"]/../input')
    # Кнопка "Войти"
    login_button = (By.XPATH, './/button[text()="Войти"]')
    # Заголовок "Войти"
    login_header = (By.XPATH, './/*[text()="Вход"]')
    # Текст с информацией о разделе
    profile_text = (By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']")
    # Cсылка "Конструктор"
    constructor_link = (By.XPATH, './/p[text()="Конструктор"]')
    # Логотип "Stellar Burgers"
    stellar_burgers_logo = (By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2')
    # Кнопка "Выход"
    logout_button = (By.XPATH, './/button[text()="Выход"]')
    # Кнопка "Оформить заказ"
    order_button = (By.XPATH, './/button[text()="Оформить заказ"]')
    # Кнопка "Войти в аккаунт"
    account_login_button = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    # Кнопка "Личный кабинет"
    user_account_link = (By.XPATH, './/p[text()="Личный Кабинет"]')
    # Заголовок "Соберите бургер"
    constructor_header_logo = (By.XPATH, './/h1[text()="Соберите бургер"]')
    # Вкладка "Булки" в Конструкторе
    buns_section = (By.XPATH, './/span[text()="Булки"]/..')
    # Вкладка "Соусы" в Конструкторе
    sauces_section = (By.XPATH, './/span[text()="Соусы"]/..')
    # Вкладка "Начинки" в Конструкторе
    fillings_section = (By.XPATH, './/span[text()="Начинки"]/..')
    # Вкладка "Начинки" в Конструкторе
    fillings_section_active = (By.XPATH, './/h2[text()="Начинки"]')
    # Кнопка "Вход"
    log_in_title = (By.XPATH, "//h2[text() = 'Вход']")
    save_button = (By.XPATH, "//button[contains(text(), 'Сохранить')]")




