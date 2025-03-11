from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from utilities.logger import Logger
import allure

fake = Faker("ru_RU")


class Registration_authorization_page(Base):
    # Locators

    # Элементы в блоке "Регистрация"

    title_reg_window = '//div[@class="modal__header"]'
    tab_registration_btn = '//a[@data-form="modal-register"]'
    tab_registration = '//div[@id="modal-register"]'
    login_reg_field = '//input[@id="LOGIN_NAME_REG"]'
    password_reg_field = '//input[@id="AUTH_PASSWORD_REQ"]'
    confirm_password_field = '//input[@id="AUTH_CONFIRM"]'
    mail_field = '//input[@id="AUTH_EMAIL"]'
    first_name_field = '//input[@id="AUTH_NAME"]'
    last_name_field = '//input[@id="AUTH_LAST_NAME"]'
    registration_btn = '//input[@name="Register"]'
    sendmail_reg_checkbox = '//div[@id="modal-register"]//input[@name="UF_SENDMAIL"]'

    # Элементы в блоке "Авторизация"

    tab_authorization = '//div[@id="modal-login"]'
    title_auth_window = '//div[@class="modal__header"]'
    login_auth_field = '//input[@id="LOGIN_NAME"]'
    password_auth_field = '//input[@id="LOGIN_PASSWORD"]'
    sendmail_auth_checkbox = '//div[@id="modal-login"]//input[@name="UF_SENDMAIL"]'
    login_btn = '//input[@name="Login"]'

    # Getters

    """Поля в окне 'Регистрация'"""

    def get_tab_registration_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.tab_registration_btn)))

    def get_login_reg_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.login_reg_field)))

    def get_password_reg_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.password_reg_field)))

    def get_confirm_password_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.confirm_password_field)))

    def get_mail_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.mail_field)))

    def get_first_name_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_registration_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.registration_btn)))

    def get_sendmail_reg_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.sendmail_reg_checkbox)))

    """Поля в окне 'Авторизация'"""

    def get_tab_authorization(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.tab_authorization)))

    def get_login_auth_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.login_auth_field)))

    def get_password_auth_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.password_auth_field)))

    def get_sendmail_auth_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.sendmail_auth_checkbox)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))

    # Actions

    """Действия в окне 'Регистрация'"""

    def click_tab_registration_btn(self):
        self.get_tab_registration_btn().click()
        print('Нажимаем на вкладку [Регистрация]')

    def input_login_reg_field(self):
        self.get_login_reg_field().send_keys(self.reading_file_variables('login'))
        print('Заполняем поле "Логин"')

    def input_password_reg_field(self):
        self.get_password_reg_field().send_keys(self.reading_file_variables('password'))
        print('Заполняем поле "Пароль"')

    def input_confirm_password_field(self):
        self.get_confirm_password_field().send_keys(self.reading_file_variables('password'))
        print('Заполняем поле "Подтвердите пароль"')

    def input_mail_field(self):
        self.get_mail_field().send_keys(self.reading_file_variables('mail'))
        print('Заполняем поле "Mail"')

    def input_first_name_field(self):
        self.get_first_name_field().send_keys(self.reading_file_variables('first_name'))
        print('Заполняем поле "Имя"')

    def input_last_name_field(self):
        self.get_last_name_field().send_keys(self.reading_file_variables('last_name'))
        print('Заполняем поле "Фамилия"')

    def click_registration_btn(self):
        self.get_registration_btn().click()
        print('Нажимаем кнопку [Регистрация]')

    def click_sendmail_reg_checkbox(self):
        self.get_sendmail_reg_checkbox().click()
        print('Нажимаем на чек-бокс "Даю согласие на подписку на новости"')

    def tab_registration_is_close(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located((By.XPATH, self.tab_registration)))
            print('Форма регистрации закрылась.')
        except:
            print('Произошла ошибка. Форма регистрации не закрылась')

    def tab_registration_is_open(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.tab_registration)))
            print('Форма регистрации открылась.')
        except:
            self.get_screenshot('test_1_registration')
            print('Произошла ошибка. Форма регистрации не открылась')

    """Действия в окне 'Авторизация'"""

    def input_login_auth_field(self):
        self.get_login_auth_field().send_keys(self.reading_file_variables('login'))
        print('Заполняем поле "Логин" в окне авторизации')

    def input_password_auth_field(self):
        self.get_password_auth_field().send_keys(self.reading_file_variables('password'))
        print('Заполняем поле "Пароль" в окне авторизации')

    def click_login_btn(self):
        self.get_login_btn().click()
        print('Нажимаем кнопку [Войти]')

    def click_sendmail_auth_checkbox(self):
        self.get_sendmail_auth_checkbox().click()
        print('Нажимаем на чек-бокс "Даю согласие на подписку на новости"')

    def tab_authorization_is_open(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.tab_authorization)))
            print('Форма авторизации открылась.')
        except:
            self.get_screenshot('test_2_authorization')
            print('Произошла ошибка. Форма авторизации не открылась')

    def tab_authorization_is_close(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located((By.XPATH, self.tab_authorization)))
            print('Форма авторизации закрылась.')
        except:
            self.get_screenshot('test_2_authorization')
            print('Произошла ошибка. Форма авторизации не закрылась')

    # Methods

    def registration_with_correct_data(self):
        with allure.step('Регистрируем нового пользователя с корректными данными'):
            Logger.add_start_step(method='registration_with_correct_data')
            self.tab_authorization_is_open()
            self.click_tab_registration_btn()
            self.tab_registration_is_open()
            self.input_login_reg_field()
            self.input_password_reg_field()
            self.input_confirm_password_field()
            self.input_mail_field()
            self.input_first_name_field()
            self.input_last_name_field()
            self.click_sendmail_reg_checkbox()
            self.click_registration_btn()
            self.tab_registration_is_close()
            Logger.add_end_step(url=self.driver.current_url, method='registration_with_correct_data')

    def authorization_with_correct_data(self):
        with allure.step('Авторизуемся под пользователями с корректными даными"'):
            Logger.add_start_step(method='authorization_with_correct_data')
            self.tab_authorization_is_open()
            self.input_login_auth_field()
            self.input_password_auth_field()
            self.click_sendmail_auth_checkbox()
            self.click_login_btn()
            self.tab_authorization_is_close()
            Logger.add_end_step(url=self.driver.current_url, method='authorization_with_correct_data')
