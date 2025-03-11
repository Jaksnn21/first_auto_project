import allure

from base.base_class import Base
from pages.main_page import Main_page
from pages.registration_authorization_page import Registration_authorization_page
from tests.conftest import set_up_1

@allure.description('Регистрация на сайте "Фенко"')
def test_registrarion_in_website(set_up_1):
    print('Старт теста регистрации на сайте "Фенко"')

    driver2 = set_up_1

    bc = Base(driver2)
    bc.save_created_data()

    mp = Main_page(driver2)
    mp.open_login_window()

    rap = Registration_authorization_page(driver2)
    rap.registration_with_correct_data()

    print('Регистрация завершена успешно')
