import datetime

import allure
from faker import Faker

fake = Faker("ru_RU")


class Base:

    def __init__(self, driver):
        self.driver = driver
        """Generation Variables"""
        self.generation_login = fake.user_name()
        self.generation_password = fake.password()
        self.generation_mail = fake.email(domain='mail.ru')
        self.generation_first_name = fake.first_name()
        self.generation_last_name = fake.last_name()

    def save_created_data(self):
        with allure.step('Создаем персональные данные о пользователе'):
            fl = open('C:\\Users\\SanSanych\PycharmProjects\\fenko_project\\tests\\variables\\variables.txt', 'w')
            fl.write('login=' + self.generation_login + '\n')
            fl.write('password=' + self.generation_password + '\n')
            fl.write('mail=' + self.generation_mail + '\n')
            fl.write('first_name=' + self.generation_first_name + '\n')
            fl.write('last_name=' + self.generation_last_name + '\n')
            fl.close()

    def reading_file_variables(self, variables):
        fl = open('C:\\Users\\SanSanych\PycharmProjects\\fenko_project\\tests\\variables\\variables.txt', 'r')
        s = []
        for line in fl.readlines():
            s.append(line.strip().split('='))
        fl.close()
        content = {}
        for var in s:
            content[var[0]] = var[1]
        return content.get(variables)

    def get_screenshot(self, test_name):
        now_date = datetime.datetime.now().strftime('%d.%m.%Y %H.%M.%S')
        name_screenshot = f'{test_name}' + now_date + '.png'
        self.driver.save_screenshot(f'C:\\Users\\SanSanych\\PycharmProjects\\fenko_project\\screen\\{test_name}\\' + name_screenshot)
        print(f'В директорию "screen\\{test_name}" добавлен скриншот сделанный в момент воспроизведения ошибки.')

    """Метод проверки наименования элемента"""
    def assert_word(self, word, result, test_name):
        value_word = word.text
        try:
            assert value_word == result
            print(f'Наименование элемента "{value_word}" верное')
        except AssertionError:
            self.get_screenshot(test_name)
            print(f'Наименование элемента "{value_word}" неверное')

    """Метод проверки URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        try:
            assert get_url == result
            print(f'URL {get_url} - корректен')
        except AssertionError:
            print(f'URL {get_url} - корректен')

    def save_added_product_name_and_price(self, name_in_catalog, price_in_catalog):
        fl = open('C:\\Users\\SanSanych\PycharmProjects\\fenko_project\\tests\\variables\\data_added_in_cart_product.txt', 'w', encoding="utf-8")
        fl.write('name_product_1=' + name_in_catalog + '\n')
        fl.write('price_product_1=' + price_in_catalog + '\n')
        fl.close()
        print('Сохраняем наименование и цену добавляемого товара их каталога')

    def reading_added_product_name_and_price(self, variables):
        fl = open('C:\\Users\\SanSanych\\PycharmProjects\\fenko_project\\tests\\variables\\data_added_in_cart_product.txt', 'r', encoding="utf-8")
        s = []
        for line in fl.readlines():
            s.append(line.strip().split('='))
        fl.close()
        content = {}
        for var in s:
            content[var[0]] = var[1]
        return content.get(variables)