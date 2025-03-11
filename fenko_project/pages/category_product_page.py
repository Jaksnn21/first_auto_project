import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from base.base_class import Base
from utilities.logger import Logger


class Category_product_page(Base):

    # Locators

    page_title = '//h1[@id="pagetitle"]'

    filter_price_btn = '//span[contains(text(), "Цена")]/../span[@data-role="prop_angle"]'
    filter_brand_btn = '//span[contains(text(), "Бренд")]/../span[@data-role="prop_angle"]'
    filter_power_btn = '//span[contains(text(), "Мощность")]/../span[@data-role="prop_angle"]'
    filter_voltage_btn = '//span[contains(text(), "Напряжение сети")]/../span[@data-role="prop_angle"]'
    filter_engine_type_btn = '//span[contains(text(), "Тип двигателя")]/../span[@data-role="prop_angle"]'
    filter_cutting_system_btn = '//span[contains(text(), "Тип режущей системы")]/../span[@data-role="prop_angle"]'
    filter_cutting_height_btn = '//span[contains(text(), "Высота среза")]/../span[@data-role="prop_angle"]'

    left_slider_price = '//a[@id="left_slider_c4ca4238a0b923820dcc509a6f75849b"]'
    right_slider_price = '//a[@id="right_slider_c4ca4238a0b923820dcc509a6f75849b"]'
    brand_huter_checkbox_name = '//label[contains(text(), "HUTER")]'
    brand_huter_checkbox = '//input[@id="arrFilter_9235_1234114054"]'
    power_1100_checkbox_name = '//label[contains(text(), "1100")]'
    power_1100_checkbox = '//input[@id="arrFilter_8295_34506063"]'
    power_1400_checkbox_name = '//label[contains(text(), "1400")]'
    power_1400_checkbox = '//input[@id="arrFilter_8295_744741355"]'
    voltage_220_checkbox_name = '//label[contains(text(), "220")]'
    voltage_220_checkbox = '//input[@id="arrFilter_8313_2925294190"]'
    engine_electric_checkbox_name = '//label[contains(text(), "Электрический")]'
    engine_electric_checkbox = '//input[@id="arrFilter_8315_1803501697"]'
    rotary_cutting_system_checkbox_name = '//label[contains(text(), "Роторная")]'
    rotary_cutting_system_checkbox = '//input[@id="arrFilter_8323_477655063"]'
    cutting_heigt_25_55_checkbox_name = '//label[contains(text(), "25-55")]'
    cutting_heigt_25_55_checkbox = '//input[@id="arrFilter_8326_249014180"]'

    set_filter_btn = '//input[@id="set_filter"]'

    cart_add_btn = '//button[contains(text(), "В корзину")]'
    product_in_cart_btn_text = '//span[contains(@class, "btn-green")]'
    cart_img = '//div[@class="header__buttons align-items-end"]//div[@class="header__mobile--cart cart__desktop"]'
    go_to_cart_btn = '//div[@class="header__buttons align-items-end"]//div[contains(text(), "Корзина")]'
    product_price_in_catalog = '//span[@id="bx_3966226736_44741_7e1b8e3524755c391129a9d7e6f2d206_price"]'
    product_name_in_catalog = '//a[@title="Huter ELM-1400P"]'



    # Getters

    def get_page_title(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.page_title)))

    def get_filter_price_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_btn)))

    def get_filter_brand_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand_btn)))

    def get_filter_power_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_power_btn)))

    def get_filter_voltage_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_voltage_btn)))

    def get_filter_engine_type_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_engine_type_btn)))

    def get_filter_cutting_system_btn(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_cutting_system_btn)))

    def get_filter_cutting_height_btn(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_cutting_height_btn)))

    def get_left_slider_price(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.left_slider_price)))

    def get_right_slider_price(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.right_slider_price)))

    def get_brand_huter_checkbox_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.brand_huter_checkbox_name)))

    def get_power_1100_checkbox_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.power_1100_checkbox_name)))

    def get_power_1400_checkbox_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.power_1400_checkbox_name)))

    def get_voltage_220_checkbox_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.voltage_220_checkbox_name)))

    def get_engine_electric_checkbox_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.engine_electric_checkbox_name)))

    def get_rotary_cutting_system_checkbox_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.rotary_cutting_system_checkbox_name)))

    def get_cutting_heigt_25_55_checkbox_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.cutting_heigt_25_55_checkbox_name)))

    def get_brand_huter_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.brand_huter_checkbox)))

    def get_power_1100_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.power_1100_checkbox)))

    def get_power_1400_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.power_1400_checkbox)))

    def get_voltage_220_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.voltage_220_checkbox)))

    def get_engine_electric_checkbox(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.engine_electric_checkbox)))

    def get_rotary_cutting_system_checkbox(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.rotary_cutting_system_checkbox)))

    def get_cutting_heigt_25_55_checkbox(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.cutting_heigt_25_55_checkbox)))

    def get_set_filter_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.set_filter_btn)))

    def get_cart_add_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cart_add_btn)))

    def get_cart_img(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.cart_img)))

    def get_go_to_cart_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_btn)))

    def get_product_price_in_catalog(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.product_price_in_catalog)))

    def get_product_name_in_catalog(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.product_name_in_catalog)))

    # Actions


    def click_filter_price_btn(self):
        self.get_filter_price_btn().click()
        print('Раскрываем фильтр "Цена"')

    def click_filter_brand_btn(self):
        self.get_filter_brand_btn().click()
        print('Раскрываем фильтр "Бренд"')

    def click_filter_power_btn(self):
        self.get_filter_power_btn().click()
        print('Раскрываем фильтр "Мощность, вт"')

    def click_filter_voltage_btn(self):
        self.get_filter_voltage_btn().click()
        print('Раскрываем фильтр "Напряжение сети, В"')

    def click_filter_engine_type_btn(self):
        self.get_filter_engine_type_btn().click()
        print('Раскрываем фильтр "Тип двигателя"')

    def click_filter_cutting_system_btn(self):
        self.get_filter_cutting_system_btn().click()
        print('Раскрываем фильтр "Тип режущей системы"')

    def click_filter_cutting_height_btn(self):
        self.get_filter_cutting_height_btn().click()
        print('Раскрываем фильтр "Высота среза"')

    def click_brand_huter_checkbox(self):
        self.get_brand_huter_checkbox().click()
        print('Устанавливаем отметку в чек-бокс "HUTER"')

    def click_power_1100_checkbox(self):
        self.get_power_1100_checkbox().click()
        print('Устанавливаем отметку в чек-бокс "1100"')

    def click_power_1400_checkbox(self):
        self.get_power_1400_checkbox().click()
        print('Устанавливаем отметку в чек-бокс "1400"')

    def click_voltage_220_checkbox(self):
        self.get_voltage_220_checkbox().click()
        print('Устанавливаем отметку в чек-бокс "220"')

    def click_engine_electric_checkbox(self):
        self.get_engine_electric_checkbox().click()
        print('Устанавливаем отметку в чек-бокс "Электрический"')

    def click_rotary_cutting_system_checkbox(self):
        self.get_rotary_cutting_system_checkbox().click()
        print('Устанавливаем отметку в чек-бокс "Роторная"')

    def click_cutting_heigt_25_55_checkbox(self):
        self.get_cutting_heigt_25_55_checkbox().click()
        print('Устанавливаем отметку в чек-бокс "25-55"')

    def click_set_filter_btn(self):
        self.get_set_filter_btn().click()
        print('Нажимаем кнопку [Показать]')


    def swipe_left_slider_price(self):
        action = ActionChains(self.driver)
        try:
            action.click_and_hold(self.get_left_slider_price()).move_by_offset(80, 0).release().perform()
            print('Устанавливаем цену "от"')
        except TimeoutException:
            self.get_screenshot('test_3_add_product_in_cart')
            self.click_filter_price_btn()
            action.click_and_hold(self.get_left_slider_price()).move_by_offset(80, 0).release().perform()
            print('Устанавливаем цену "от"')


    def swipe_right_slider_price(self):
        action = ActionChains(self.driver)
        try:
            action.click_and_hold(self.get_right_slider_price()).move_by_offset(-150, 0).release().perform()
            print('Устанавливаем цену "до"')
        except TimeoutException:
            self.get_screenshot('test_3_add_product_in_cart')
            self.click_filter_price_btn()
            action.click_and_hold(self.get_left_slider_price()).move_by_offset(-150, 0).release().perform()
            print('Устанавливаем цену "до"')

    def scroll_window(self):
        self.driver.execute_script("window.scrollTo(0, 600);")
        print('Скроллим страницу вниз')

    def wait_set_filters(self):
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element_attribute((By.XPATH, self.set_filter_btn), 'value', 'Показать 1'))
        print('Ждем, пока не изменится значение кнопки [Показать]')

    def click_cart_add_btn(self):
        self.get_cart_add_btn().click()
        print('Нажимаем кнопку [В корзину]')

    def check_product_add_to_cart(self, result):
        try:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.XPATH, self.product_in_cart_btn_text), 'В корзине'))
            print('Кнопка карсного цвета [В корзину] поменялась на кнопку зеленого цвета [В корзине]')
        except:
            self.get_screenshot('test_3_add_product_in_cart')
            print('Кнопка карсного цвета [В корзину] НЕ поменялась на кнопку зеленого цвета [В корзине]')
        try:
            assert self.get_cart_img().text == result
            print(f'Кол-во добавленных товаров в корзину отображается верно - {self.get_cart_img().text}')
        except AssertionError:
            self.get_screenshot('test_3_add_product_in_cart')
            print(
                f'Кол-во добавленных товаров в корзину посчитано НЕ верно - {self.get_cart_img().text}, должно быть - {result}')

    def click_go_to_cart_btn(self):
        self.get_go_to_cart_btn().click()
        print('Нажимаем кнопку [Корзина]')

    def save_product_price_in_catalog(self):
        self.price_in_catalog = self.get_product_price_in_catalog().text
        return self.price_in_catalog

    def save_product_name_in_catalog(self):
        self.name_in_catalog = self.get_product_name_in_catalog().get_attribute('title')
        return self.name_in_catalog


    # Methods
    def set_filters_and_add_product_to_cart(self):
        with allure.step('Сортируем товар по фильтрам и добавляем в корзину'):
            Logger.add_start_step(method='set_filters_and_add_product_to_cart')
            self.assert_word(self.get_page_title(), 'Газонокосилки', 'test_3_add_product_in_cart')
            self.swipe_left_slider_price()
            self.swipe_right_slider_price()
            self.click_filter_brand_btn()
            self.assert_word(self.get_brand_huter_checkbox_name(), 'HUTER', 'test_3_add_product_in_cart')
            self.click_brand_huter_checkbox()
            self.click_filter_power_btn()
            self.assert_word(self.get_power_1100_checkbox_name(), '1100', 'test_3_add_product_in_cart')
            self.assert_word(self.get_power_1400_checkbox_name(), '1400', 'test_3_add_product_in_cart')
            self.click_power_1100_checkbox()
            self.click_power_1400_checkbox()
            self.scroll_window()
            time.sleep(1)
            self.click_filter_voltage_btn()
            self.assert_word(self.get_voltage_220_checkbox_name(), '220', 'test_3_add_product_in_cart')
            self.click_voltage_220_checkbox()
            self.click_filter_engine_type_btn()
            self.assert_word(self.get_engine_electric_checkbox_name(), 'Электрический', 'test_3_add_product_in_cart')
            self.click_engine_electric_checkbox()
            self.click_filter_cutting_system_btn()
            self.assert_word(self.get_rotary_cutting_system_checkbox_name(), 'Роторная', 'test_3_add_product_in_cart')
            self.click_rotary_cutting_system_checkbox()
            self.click_filter_cutting_height_btn()
            self.assert_word(self.get_cutting_heigt_25_55_checkbox_name(), '25-55', 'test_3_add_product_in_cart')
            self.click_cutting_heigt_25_55_checkbox()
            self.wait_set_filters()
            self.click_set_filter_btn()
            self.assert_word(self.get_page_title(), 'Газонокосилки', 'test_3_add_product_in_cart')
            self.click_cart_add_btn()
            self.check_product_add_to_cart('1')
            self.save_added_product_name_and_price(self.save_product_name_in_catalog(), self.save_product_price_in_catalog())
            self.click_go_to_cart_btn()
            self.assert_url('https://fenkovrn.ru/personal/cart/')
            Logger.add_end_step(url=self.driver.current_url, method='set_filters_and_add_product_to_cart')
