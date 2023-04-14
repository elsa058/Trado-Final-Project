from Web.BasePage.basepage import BasePage
from Web.Data.data import *
from Web.Locators.business_common_locators import Promo_Locators


class PromotionPage(BasePage, Promo_Locators, Data):

    def select_option1(self):
        self._click(self.option1)

    def click_save(self):
        self._click(self.save)

    def select_option2(self):
        self._click(self.option2)

    def select_the_link(self):
        self._find(self.common_Question)
        return self._find(self.common_Question)

    def verify_page_title(self):
        return self._find(self.for_all_Question).text

    def verify_page_title_text(self):
        return self._find(self.create_new_business).text

    def scrolling_page(self, locate, amount):
        self.scroll(locate, amount)

    def check_clikable_Question(self,locate):
        return self._click(locate)

    def the_text_is_displayed(self,locate):
        return self._is_displayed(locate)

    def text_displayed(self):
        return self._is_displayed(self.blue_box_logo)

    def alert_switch_text(self,text):
        self._driver(text)
        return self.alert_switch()

    def image_clikable(self,locate):
        return self._click(locate)

    # def entry_text_type(self, locate, content):
    #     self._find(locate,content)

    def enter_lastname(self,locate,lastname):
        self._entry(locate,lastname)

    def enter_firstname(self,locate,firstname):
        self._entry(locate,firstname)

    def enter_name_business(self, locate, name):
        self._entry(locate, name)

    def enter_select_catagories(self, locate, name_of_catagories):
        self._entry(locate, name_of_catagories)

    def enter_HFTMC(self, locate, HFME):
        self._entry(locate, HFME)

    def enter_email(self,locate,email):
        self._entry(locate,email)

    def enter_phone_number(self,locate,phone):
        self._entry(locate,phone)

    def enter_city(self,locate,city):
        self._entry(locate,city)

    def enter_street(self,locate,street):
        self._entry(locate,street)

    def enter_house_number(self, locate,number):
        self._entry(locate, number)












