import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Personal_cabinet_page(Base):

    # Locators

    personal_data_btn = "//h2[contains(text(), 'Личные данные')]//ancestor::a[@class='sale-personal-section-index-block-link']"


    # Getters

    def get_personal_data_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.personal_data_btn)))


    # Actions

    def click_personal_data_btn(self):
        self.get_personal_data_btn().click()
        print('Нажимаем кнопку [Личные данные]')



    # Methods

    def open_personal_data_page(self):
        with allure.step('Открываем форму "Личные данные"'):
            Logger.add_start_step(method='open_personal_data_page')
            self.click_personal_data_btn()
            self.assert_url('https://fenkovrn.ru/personal/private/')
            Logger.add_end_step(url=self.driver.current_url, method='open_personal_data_page')
