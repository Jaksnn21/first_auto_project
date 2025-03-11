import allure
import pytest
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.registration_authorization_page import Registration_authorization_page

"""Начало и завершение работы в браузере"""
@pytest.fixture()
@allure.description('Открываем сайт "Фенко"')
def set_up_1():
    print('\nОткрываем сайт "Фенко"')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    url = 'https://fenkovrn.ru/'
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
    print('\nЗакрываем браузер')


@pytest.fixture()
@allure.description('Открываем сайт "Фенко" и открываем форму "Корзина"')
def set_up_2():
    print('\nОткрываем сайт "Фенко"')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    url = 'https://fenkovrn.ru/'
    driver.get(url)
    driver.maximize_window()
    mp = Main_page(driver)
    mp.open_login_window()
    rap = Registration_authorization_page(driver)
    rap.authorization_with_correct_data()
    mp.open_cart()
    cp = Cart_page(driver)
    cp.verification_added_product()
    yield driver
    driver.quit()
    print('\nЗакрываем браузер')

