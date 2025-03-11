
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains

from utilities.logger import Logger


class Finish_order_prage(Base):

    # Locators

    order_save_btn = '(//a[contains(@class, "btn-order-save")])[2]'
    payer_type_individual_checkbox = '//input[@id="radio1"]'
    first_name_field = '//input[@id="soa-property-1"]'
    last_name_field = '//input[@id="soa-property-4"]'
    number_phone_field = '//input[@id="soa-property-2"]'
    mail_field = '//input[@id="soa-property-3"]'
    city_field = '//input[@id="soa-property-5"]'
    street_field = '//input[@id="soa-property-6"]'
    house_field = '//input[@id="soa-property-7"]'
    frame_field = '//input[@id="soa-property-8"]'
    porch_field = '//input[@id="soa-property-9"]'
    floor_field = '//input[@id="soa-property-10"]'
    flat_field = '//input[@id="soa-property-11"]'

    # Getters

    def get_order_save_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.order_save_btn)))

    def get_payer_type_individual_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.payer_type_individual_checkbox)))

    def get_first_name_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.last_name_field)))

    def get_number_phone_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.number_phone_field)))

    def get_mail_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.mail_field)))

    def get_city_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.city_field)))

    def get_street_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.street_field)))

    def get_house_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.house_field)))

    def get_frame_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.frame_field)))

    def get_porch_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.porch_field)))

    def get_floor_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.floor_field)))

    def get_flat_field(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.flat_field)))


    # Actions

    def click_payer_type_individual_checkbox(self):
        try:
           assert self.get_payer_type_individual_checkbox().get_attribute('checked') == 'true'
           print('В чек-боксе "Физическое лицо" уже установлена отметка')
        except AssertionError:
            self.get_screenshot('test_4_finish_order')
            self.get_payer_type_individual_checkbox().click()
            print('Устанавливаем отметку в чек-боксе "Физическое лицо"')

    def assert_firs_name_field(self):
        try:
            assert self.get_first_name_field().get_property('value') == self.reading_file_variables('first_name')
            print(f'В поле "Имя" корректно указано значение "{self.reading_file_variables('first_name')}".')
        except AssertionError:
            self.get_screenshot('test_4_finish_order')
            print(f'В поле "Имя" указано НЕкорректное значение "{self.get_first_name_field().get_property('value')}". Должно быть "{self.reading_file_variables('first_name')}"')
            self.get_first_name_field().send_keys(Keys.CONTROL + 'a')
            self.get_first_name_field().send_keys(Keys.BACKSPACE)
            print('Удаляем некорректное значение поля "Имя"')
            self.get_first_name_field().send_keys(self.reading_file_variables('first_name'))
            print(f'Заполняем поле "Имя" корректным значением "{self.reading_file_variables('first_name')}"')

    def assert_last_name_field(self):
        try:
            assert self.get_last_name_field().get_property('value') == self.reading_file_variables('last_name')
            print(f'В поле "Фамилия" корректно указано значение "{self.reading_file_variables('last_name')}".')
        except AssertionError:
            self.get_screenshot('test_4_finish_order')
            print(f'В поле "Фамилия" указано НЕкорректное значение "{self.get_last_name_field().get_property('value')}". Должно быть "{self.reading_file_variables('last_name')}"')
            self.get_last_name_field().send_keys(Keys.CONTROL + 'a')
            self.get_last_name_field().send_keys(Keys.BACKSPACE)
            print('Удаляем некорректное значение поля "Фамилия"')
            self.get_last_name_field().send_keys(self.reading_file_variables('last_name'))
            print(f'Заполняем поле "Фамилия" корректным значением "{self.reading_file_variables('last_name')}"')

    def assert_mail_field(self):
        try:
            assert self.get_mail_field().get_property('value') == self.reading_file_variables('mail')
            print(f'В поле "E-mail" корректно указано значение "{self.reading_file_variables('mail')}".')
        except AssertionError:
            self.get_screenshot('test_4_finish_order')
            print(f'В поле "E-mail" указано НЕкорректное значение "{self.get_mail_field().get_property('value')}". Должно быть "{self.reading_file_variables('mail')}"')
            self.get_mail_field().send_keys(Keys.CONTROL + 'a')
            self.get_mail_field().send_keys(Keys.BACKSPACE)
            print('Удаляем некорректное значение поля "E-mail"')
            self.get_mail_field().send_keys(self.reading_file_variables('mail'))
            print(f'Заполняем поле "E-mail" корректным значением "{self.reading_file_variables('mail')}"')


    def input_number_phone_field(self):
        fake = Faker("ru_RU")
        self.get_number_phone_field().send_keys(fake.phone_number())
        print('Заполняем поле "Телефон"')

    def assert_city_field(self, city):
        try:
            assert self.get_city_field().get_property('value') != ''
            print(f'В поле "Город" корректно указано значение "{self.get_city_field().get_property('value')}", которое определяется автоматически по геолокации')
        except AssertionError:
            self.get_screenshot('test_4_finish_order')
            print(f'Значение поля "Город" не определилось автоматически')
            self.get_city_field().send_keys(city)
            print(f'Заполняем поле "Город" корректным значением "{city}"')

    def input_street_field(self):
        fake = Faker("ru_RU")
        self.get_street_field().send_keys(fake.street_name())
        print('Заполняем поле "Улица"')

    def input_house_field(self):
        fake = Faker("ru_RU")
        self.get_house_field().send_keys(fake.random.randint(1, 600))
        print('Заполняем поле "Дом"')

    def input_frame_field(self):
        fake = Faker("ru_RU")
        self.get_frame_field().send_keys(fake.building_number())
        print('Заполняем поле "Корпус"')

    def input_porch_field(self):
        fake = Faker("ru_RU")
        self.get_porch_field().send_keys(fake.random.randint(1, 600))
        print('Заполняем поле "Подъезд"')

    def input_floor_field(self):
        fake = Faker("ru_RU")
        self.get_floor_field().send_keys(fake.random.randint(1, 600))
        print('Заполняем поле "Этаж"')

    def input_flat_field(self):
        fake = Faker("ru_RU")
        self.get_flat_field().send_keys(fake.random.randint(1, 600))
        print('Заполняем поле "Квартира"')

    def move_to_flat_field(self):
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.driver.find_element(By.XPATH, self.flat_field))
        print('Скроллим страницу к полю "Квартира"')


    # Methods
    def placing_an_order(self):
        with allure.step('Завершаем оформление товара, заполняем контактную информацию о пользователе'):
            Logger.add_start_step(method='placing_an_order')
            self.assert_word(self.get_order_save_btn(), 'Оформить', 'test_4_finish_order')
            self.click_payer_type_individual_checkbox()
            self.assert_firs_name_field()
            self.assert_last_name_field()
            self.assert_mail_field()
            self.input_number_phone_field()
            self.move_to_flat_field()
            self.assert_city_field('г. Воронеж')
            self.input_street_field()
            self.input_house_field()
            self.input_frame_field()
            self.input_porch_field()
            self.input_floor_field()
            self.input_flat_field()
            Logger.add_end_step(url=self.driver.current_url, method='placing_an_order')



