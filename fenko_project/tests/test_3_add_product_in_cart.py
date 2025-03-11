import allure

from pages.cart_page import Cart_page
from pages.category_product_page import Category_product_page
from pages.main_page import Main_page
from pages.registration_authorization_page import Registration_authorization_page
from tests.conftest import set_up_1

@allure.description('Добавляем товар в корзину')
def test_add_product_in_cart(set_up_1):
    print('Старт теста по добавлению товара в корзину')

    driver2 = set_up_1

    mp = Main_page(driver2)
    mp.open_login_window()

    rap = Registration_authorization_page(driver2)
    rap.authorization_with_correct_data()

    mp.select_category_product()

    cpp = Category_product_page(driver2)
    cpp.set_filters_and_add_product_to_cart()

    cp = Cart_page(driver2)
    cp.verification_added_product()

    print('Завершение теста по добавлению товара в корзину')