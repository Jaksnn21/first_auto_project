import allure

from pages.finish_order_page import Finish_order_prage
from tests.conftest import set_up_2

@allure.description('Завершаем оформление товара')
def test_finish_order(set_up_2):
    print('Старт теста по оформлению заказа')

    driver2 = set_up_2

    fop = Finish_order_prage(driver2)
    fop.placing_an_order()

    print('Завершение теста по оформлению заказ')