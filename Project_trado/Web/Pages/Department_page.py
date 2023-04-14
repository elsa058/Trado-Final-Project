import time

import allure

from Web.BasePage.basepage import BasePage
from Web.Data.data_departments import *
from Web.Locators.Department_loactors import Dep_Locator


class DepartmentPage(BasePage, Dep_Locator,data):

    def select_enter_code(self, locate, phone):
        self._entry(locate, phone)

    @allure.step
    def select_enter_name(self, locate):
        self._entry(self.name_user,locate)

    @allure.step
    def click_button(self):
        self._click(self.send_code)

    @allure.step
    def enter_phone_valid(self, locate, codes):
        self._entry(locate, codes)

    @allure.step
    def select_button(self):
        self._click(self.login)

    @allure.step
    def click_contents(self):
        self._click(self.department)

    @allure.step
    def department_name_displayed(self):
        self._click(self.Name)

    @allure.step
    def department_name_arrow_displayed(self):
        self._click(self.Name_arrow)

    @allure.step
    def department_images(self):
        self._click(self.image)

    @allure.step
    def department_cover_image(self):
        self._click(self.cover_image)

    @allure.step
    def department_active(self):
        self._click(self.active)

    @allure.step
    def department_creatart(self):
        self._click(self.creatart)

    @allure.step
    def department_three_dots(self):
        self._click(self.three_dots)

    @allure.step
    def department_up_down(self):
        self._click(self.up_down_link)

    @allure.step
    def department_plus_add(self):
        self._click(self.plus_add)

    @allure.step
    def department_export(self):
        self._click(self.export)

    @allure.step
    def department_update_button(self):
        self._click(self.update_button)

