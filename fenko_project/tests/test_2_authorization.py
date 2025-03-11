import allure
from pages.main_page import Main_page
from pages.personal_cabinet_page import Personal_cabinet_page
from pages.personal_data_page import Personal_data_page
from pages.registration_authorization_page import Registration_authorization_page
from tests.conftest import set_up_1

@allure.description('Авторизация на сайте "Фенко"')
def test_authorization_in_website(set_up_1):
    print('Старт теста авторизации на сайте "Фенко"')

    driver2 = set_up_1

    mp = Main_page(driver2)
    mp.open_login_window()

    rap = Registration_authorization_page(driver2)
    rap.authorization_with_correct_data()

    print('Проверяем корректность личных данных пользователя')
    mp.open_personal_cabinet()

    pcp = Personal_cabinet_page(driver2)
    pcp.open_personal_data_page()

    pdp = Personal_data_page(driver2)
    pdp.assert_personal_data()

    print('Авторизация завершена успешно')
