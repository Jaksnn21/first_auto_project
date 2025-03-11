import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains

from utilities.logger import Logger


class Main_page(Base):

    # Locators

    login_btn = '//div[@class="header__buttons align-items-end"]//div[contains(text(), "Войти")]'
    cabinet_btn = '//div[@class="header__buttons align-items-end"]//div[contains(text(), "Кабинет")]'
    cart_btn = '//div[@class="header__buttons align-items-end"]//div[contains(text(), "Корзина")]'
    catalog_btn = '//div[@class="header__catalog--button"]'
    large_household_technique = '//button[@class="megamenu__left--buttom"]//div[contains(text(), "Крупная бытовая техника")]'
    garden_technique = '//button[@class="megamenu__left--buttom"]//div[contains(text(), "Садовая техника")]'
    product_grass_cutter = '//div[@class="megamenu__section--name"]//a[contains(text(), "Газонокосилки")]'


    # Getters

    def get_login_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))

    def get_cabinet_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cabinet_btn)))

    def get_cart_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cart_btn)))

    def get_catalog_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.catalog_btn)))

    def get_large_household_technique(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.large_household_technique)))

    def get_garden_technique(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.garden_technique)))

    def get_product_grass_cutter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.product_grass_cutter)))

    # Actions
    def click_login_btn(self):
        self.get_login_btn().click()
        print('Нажимаем кнопку [Войти]')

    def click_cabinet_btn(self):
        self.get_cabinet_btn().click()
        print('Нажимаем кнопку [Кабинет]')

    def click_cart_btn(self):
        self.get_cart_btn().click()
        print('Нажимаем кнопку [Корзина]')

    def click_catalog_btn(self):
        self.get_catalog_btn().click()
        print('Нажимаем на кнопку [Каталог]')

    def move_to_product(self):
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.driver.find_element(By.XPATH, self.garden_technique))
        print('Наводимся на раздел "Садовая техника"')

    def click_garden_technique(self):
        self.get_garden_technique().click()
        print('Нажимаем на раздел "Садовая техника"')

    def click_product_grass_cutter(self):
        self.get_product_grass_cutter().click()
        print('Нажимаем на категорию товара "Газонокосилки"')


    # Methods
    def open_login_window(self):
        with allure.step('Открываем форму "Авторизация"'):
            Logger.add_start_step(method='open_login_window')
            self.click_login_btn()
            Logger.add_end_step(url=self.driver.current_url, method='open_login_window')



    def open_personal_cabinet(self):
        with allure.step('Открываем форму "Личный кабинет"'):
            Logger.add_start_step(method='open_personal_cabinet')
            self.click_cabinet_btn()
            self.assert_url('https://fenkovrn.ru/personal/')
            Logger.add_end_step(url=self.driver.current_url, method='open_personal_cabinet')

    def select_category_product(self):
        with allure.step('Выбираем категорию товара'):
            Logger.add_start_step(method='select_category_product')
            self.click_catalog_btn()
            self.assert_word(self.get_large_household_technique(), 'Крупная бытовая техника', 'test_3_add_product_in_cart')
            self.move_to_product()
            self.click_garden_technique()
            self.assert_word(self.get_product_grass_cutter(), 'Газонокосилки', 'test_3_add_product_in_cart')
            self.click_product_grass_cutter()
            self.assert_url('https://fenkovrn.ru/catalog/sadovaya-tekhnika/gazonokosilki/')
            Logger.add_end_step(url=self.driver.current_url, method='select_category_product')

    def open_cart(self):
        with allure.step('Открываем форму "Корзина"'):
            Logger.add_start_step(method='open_cart')
            self.click_cart_btn()
            self.assert_url('https://fenkovrn.ru/personal/cart/')
            Logger.add_end_step(url=self.driver.current_url, method='open_cart')