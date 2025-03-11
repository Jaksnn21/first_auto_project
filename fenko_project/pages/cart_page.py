
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure

from utilities.logger import Logger


class Cart_page(Base):

    # Locators

    product_price_in_cart = '(//span[@class="basket-item-price-current-text"])[1]'
    product_name_in_cart = '(//span[@data-entity="basket-item-name"])[1]'
    checkout_btn = '//button[@data-entity="basket-checkout-button"]'

    # Getters

    def get_product_price_in_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.product_price_in_cart)))

    def get_product_name_in_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.product_name_in_cart)))

    def get_checkout_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.checkout_btn)))


    # Actions

    def assert_data_product_in_catalog_and_in_cart(self):
        try:
            assert self.get_product_name_in_cart().text == self.reading_added_product_name_and_price('name_product_1')
            print(f'Наименование в каталоге - {self.reading_added_product_name_and_price('name_product_1')}', f'Наименование в корзине- {self.get_product_name_in_cart().text}', sep='\n')
            print('Наименование товара в корзине совпадает с наименованием выбраного товара в каталоге')
        except AssertionError:
            self.get_screenshot('test_3_add_product_in_cart')
            print(f'Наименование в каталоге - {self.reading_added_product_name_and_price('name_product_1')}',f'Наименование в корзине - {self.get_product_name_in_cart().text}', sep='\n')
            print('Наименование товара в корзине НЕ совпадает с наименованием выбраного товара в каталоге')
        try:
            assert self.get_product_price_in_cart().text == self.reading_added_product_name_and_price('price_product_1')
            print(f'Наименование в каталоге - {self.reading_added_product_name_and_price('price_product_1')}',
                  f'Наименование в корзине - {self.get_product_price_in_cart().text}', sep='\n')
            print('Цена товара в корзине совпадает с ценой выбраного товара в каталоге')
        except AssertionError:
            self.get_screenshot('test_3_add_product_in_cart')
            print(f'Наименование в каталоге - {self.reading_added_product_name_and_price('price_product_1')}',
                  f'Наименование в корзине- {self.get_product_price_in_cart().text}', sep='\n')
            print('Цена товара в корзине НЕ совпадает с ценой выбраного товара в каталоге')

    def click_checkout_btn(self):
        self.get_checkout_btn().click()
        print('Нажимаем кнопку [Перейти к оформлению]')


    # Methods

    def verification_added_product(self):
        with allure.step('Проверяем, что выбранный товар из Каталога совпадает с товаром в Корзине'):
            Logger.add_start_step(method='verification_added_product')
            self.assert_data_product_in_catalog_and_in_cart()
            self.click_checkout_btn()
            self.assert_url('https://fenkovrn.ru/personal/order/make/')
            Logger.add_end_step(url=self.driver.current_url, method='verification_added_product')





