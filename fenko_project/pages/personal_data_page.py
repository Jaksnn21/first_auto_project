import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Personal_data_page(Base):

    # Locators

    first_name_data_field = '//input[@id="main-profile-name"]'
    last_name_data_field = '//input[@id="main-profile-last-name"]'
    mail_data_field = '//input[@id="main-profile-email"]'
    logo_btn = '//img[contains(@alt, "ФЕНКО")]'
    cabinet_btn = '//div[@class="header__buttons align-items-end"]//div[contains(text(), "Кабинет")]'




    # Getters

    def get_first_name_data_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.first_name_data_field)))

    def get_last_name_data_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.last_name_data_field)))

    def get_mail_data_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.mail_data_field)))

    def get_logo_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.logo_btn)))

    def get_cabinet_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cabinet_btn)))


    # Actions

    def click_logo_btn(self):
        self.get_logo_btn().click()
        print('Нажимаем на кнопку для выхода на главную страницу')

    def value_first_name_data_field(self):
        try:
            assert self.get_first_name_data_field().get_attribute('value') == self.reading_file_variables('first_name')
            print('Значение поля "Имя" корректно')
        except:
            self.get_screenshot('test_2_authorization')
            print('Значение поля "Имя" некорректно')

    def value_last_name_data_field(self):
        try:
            assert self.get_last_name_data_field().get_attribute('value') == self.reading_file_variables('last_name')
            print('Значение поля "Фамилия" корректно')
        except AssertionError:
            self.get_screenshot('test_2_authorization')
            print('Значение поля "Фамилия" некорректно')

    def value_mail_data_field(self):
        try:
            assert self.get_mail_data_field().get_attribute('value') == self.reading_file_variables('mail')
            print('Значение поля "Mail" корректно')
        except AssertionError:
            self.get_screenshot('test_2_authorization')
            print('Значение поля "Mail" некорректно')


    # Methods
    def assert_personal_data(self):
        with allure.step('Проверяем пкорректность личных данных пользователя, под которым авторизованы'):
            Logger.add_start_step(method='assert_personal_data')
            self.value_first_name_data_field()
            self.value_last_name_data_field()
            self.value_mail_data_field()
            self.click_logo_btn()
            self.assert_url('https://fenkovrn.ru/')
            self.assert_word(self.get_cabinet_btn(), 'Кабинет', 'test_2_authorization')
            Logger.add_end_step(url=self.driver.current_url, method='assert_personal_data')






