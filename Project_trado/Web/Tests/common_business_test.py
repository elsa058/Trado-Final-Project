import allure
import pytest

from Web.Pages.business_common_page import *

class Test_Promotion(PromotionPage, BasePage):

    def handling_the_first_popup(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save()

    @allure.description("Test the title of Common Questions it is properly aligned or not")
    @pytest.mark.sanity
    def test_title_displayed(self):
        self.handling_the_first_popup()
        assert self.text_reading(self.common_Question) == 'שאלות נפוצות'

    @allure.description("Test For all Questions properly aligned correctly ")
    @pytest.mark.sanity
    def test_check_title(self):
        self.handling_the_first_popup()
        self.scrolling_page(self.for_all_Question, "window.scrollBy(0, 250)")
        self.select_the_link()
        assert self.the_text_is_displayed(self.for_all_Question) == True

    @allure.description("Test For all Questions button  is clickable correctly ")
    @pytest.mark.sanity
    def test_for_all_question_clikcable(self):
        self.handling_the_first_popup()
        self.scrolling_page(self.for_all_Question, "window.scrollBy(0, 250)")
        self.select_the_link()
        self._click(self.for_all_Question)

    @allure.description("Test The left side of the men's image is clickable ")
    @pytest.mark.sanity
    def test_men_image_clickable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.men_image)

    @allure.description("Test The left side of the women's image is clickable ")
    @pytest.mark.sanity
    def test_women_image_clikable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.women_image)

    @allure.description("Test The header on the top right side of the screen blue button logo is clickable")
    @pytest.mark.sanity
    def test_logo_trado_clikable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.logo_Trado)

    @allure.description("Test The Products Pages button work properly")
    @pytest.mark.sanity
    def test_product_page_clicakble(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.product_upload_page)

    @allure.description("Test The Upload Product button work properly")
    @pytest.mark.sanity
    def test_product_upload_clickable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.product_upload_page)

    @allure.description("Test common question link")
    @pytest.mark.sanity
    def test_question_link_is_displayed(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.question_link)

    @allure.description("Test Verify that the Bussiness Interface link being clickable")
    @pytest.mark.sanity
    def test_Business_interface_link_clikable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)

    @allure.description("Test common question link is to work properly")
    @pytest.mark.sanity
    def test_common_Question_link_clikable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.common_Question_link)

    @allure.description("Test the blue box logo is displayed correctly")
    @pytest.mark.sanity
    def test_empty_blue_box_logo_clikable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.blue_box_logo)
        assert self.text_displayed() == True

    @allure.description("Test the page's WhatsApp service logo is clickable correctly")
    @pytest.mark.sanity
    def test_trado_support_type_message(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.whatsapp_logo)

    @allure.description("Test the page's WhatsApp service logo is displayed and correctly existing data")
    @pytest.mark.sanity
    def test_trado_whatsapp_image(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.whatsapp_logo)
        self._click(self.whatsapp_logo_link)

    @allure.description("Test The Trado Support Send button is clickable")
    @pytest.mark.sanity
    def test_whatsapp_type(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.whatsapp_logo)
        self._click(self.whatsapp_logo_link)
        self._wait_until_element_is_visible(self.whatsapp_type)
        self._click(self.whatsapp_send_button)

    @allure.description("Test valid user account name")
    @pytest.mark.sanity
    def test_business_register(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._wait_until_element_is_visible(self.business_interface_firstname)

    @allure.description("Test user last num is null")
    @pytest.mark.sanity
    def test_business_register_last_name_null(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname,"sfdgfg")
        self.enter_lastname(self.business_interface_lastname,"")
        self.enter_HFTMC(self.business_interface_HTR,"1")
        self.enter_name_business(self.name_of_the_business,"sale")
        self.enter_select_catagories(self.select_catagories,"cocktail")
        self.enter_phone_number(self.phone_number,"0923456734")
        self.enter_email(self.business_interface_email,"elasadessie@gmail.com")
        self.enter_city(self.city_business,"bersheva")
        self.enter_street(self.street_business,"baleeer")
        self.enter_house_number(self.house_number,"1")
        self._click(self.submit_button)

    @allure.description("Test user's registration phone number is null")
    @pytest.mark.sanity
    def test_business_register_phone_number_null(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname,"sfdgfg")
        self.enter_lastname(self.business_interface_lastname,"")
        self.enter_HFTMC(self.business_interface_HTR,"1")
        self.enter_name_business(self.name_of_the_business,"sale")
        self.enter_select_catagories(self.select_catagories,"cocktail")
        self.enter_phone_number(self.phone_number,"")
        self.enter_email(self.business_interface_email,"elasadessie@gmail.com")
        self.enter_city(self.city_business,"bersheva")
        self.enter_street(self.street_business,"baleeer")
        self.enter_house_number(self.house_number,"1")
        self._click(self.submit_button)

    @allure.description("Test user's registration email is null")
    @pytest.mark.sanity
    def test_business_register_email_null(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname,"sfdgfg")
        self.enter_lastname(self.business_interface_lastname,"dfgh")
        self.enter_HFTMC(self.business_interface_HTR,"1")
        self.enter_name_business(self.name_of_the_business,"sale")
        self.enter_select_catagories(self.select_catagories,"cocktail")
        self.enter_phone_number(self.phone_number,"0923456734")
        self.enter_email(self.business_interface_email,"")
        self.enter_city(self.city_business,"bersheva")
        self.enter_street(self.street_business,"baleeer")
        self.enter_house_number(self.house_number,"1")
        self._click(self.submit_button)

    @allure.description("Test invalid user's registration email")
    @pytest.mark.sanity
    def test_business_register_email_invalid(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "sfdgfg")
        self.enter_lastname(self.business_interface_lastname, "dfgh")
        self.enter_HFTMC(self.business_interface_HTR, "1")
        self.enter_name_business(self.name_of_the_business, "sale")
        self.enter_select_catagories(self.select_catagories, "cocktail")
        self.enter_phone_number(self.phone_number, "0923456734")
        self.enter_email(self.business_interface_email, "asdfg@gmail.com")
        self.enter_city(self.city_business, "bersheva")
        self.enter_street(self.street_business, "baleeer")
        self.enter_house_number(self.house_number, "1")
        self._click(self.submit_button)

    @allure.description("Test user's registration city is null")
    @pytest.mark.sanity
    def test_business_register_city_null(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "sfdgfg")
        self.enter_lastname(self.business_interface_lastname, "dfgh")
        self.enter_HFTMC(self.business_interface_HTR, "1")
        self.enter_name_business(self.name_of_the_business, "sale")
        self.enter_select_catagories(self.select_catagories, "cocktail")
        self.enter_phone_number(self.phone_number, "0923456734")
        self.enter_email(self.business_interface_email, "dessisdfghj@gmail.com")
        self.enter_city(self.city_business, "")
        self.enter_street(self.street_business, "baleeer")
        self.enter_house_number(self.house_number, "1")
        self._click(self.submit_button)

    @allure.description("Test user's registration phone number is null")
    @pytest.mark.sanity
    def test_business_register_emai_city_phonenumber_null(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "sfdgfg")
        self.enter_lastname(self.business_interface_lastname, "dfgh")
        self.enter_HFTMC(self.business_interface_HTR, "1")
        self.enter_name_business(self.name_of_the_business, "sale")
        self.enter_select_catagories(self.select_catagories, "cocktail")
        self.enter_phone_number(self.phone_number, "")
        self.enter_email(self.business_interface_email, "")
        self.enter_city(self.city_business, "")
        self.enter_street(self.street_business, "baleeer")
        self.enter_house_number(self.house_number, "1")
        self._click(self.submit_button)

    @allure.description("Test invalid user's registration phone number")
    @pytest.mark.sanity
    def test_business_register_emai_city_phonenumber_invalid(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "sfdgfg")
        self.enter_lastname(self.business_interface_lastname, "dfgh")
        self.enter_HFTMC(self.business_interface_HTR, "1")
        self.enter_name_business(self.name_of_the_business, "sale")
        self.enter_select_catagories(self.select_catagories, "cocktail")
        self.enter_phone_number(self.phone_number, "0523478657")
        self.enter_email(self.business_interface_email, "")
        self.enter_city(self.city_business, "")
        self.enter_street(self.street_business, "baleeer")
        self.enter_house_number(self.house_number, "1")
        self._click(self.submit_button)
        assert self.text_reading(self.submit_button) == ''

    @allure.description("Test invalid a new Business account")
    @pytest.mark.sanity
    def test_business_register_invalid(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "")
        self.enter_lastname(self.business_interface_lastname, "")
        self.enter_HFTMC(self.business_interface_HTR, "")
        self.enter_name_business(self.name_of_the_business, "")
        self.enter_select_catagories(self.select_catagories, "")
        self.enter_phone_number(self.phone_number, "")
        self.enter_email(self.business_interface_email, "")
        self.enter_city(self.city_business, "")
        self.enter_street(self.street_business, "")
        self.enter_house_number(self.house_number, "")
        self._click(self.submit_button)
        assert self.text_reading(self.submit_button) == ''

    @allure.description("Test valid street name")
    @pytest.mark.sanity
    def test_business_register_valid_street(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "")
        self.enter_lastname(self.business_interface_lastname, "")
        self.enter_HFTMC(self.business_interface_HTR, "")
        self.enter_name_business(self.name_of_the_business, "")
        self.enter_select_catagories(self.select_catagories, "")
        self.enter_phone_number(self.phone_number, "")
        self.enter_email(self.business_interface_email, "")
        self.enter_city(self.city_business, "")
        self.enter_street(self.street_business, "sdfghjkdfg")
        self.enter_house_number(self.house_number, "")
        self._click(self.submit_button)

    @allure.description("Test valid user's phone number")
    @pytest.mark.sanity
    def test_business_register_valid_phonenumber(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "")
        self.enter_lastname(self.business_interface_lastname, "")
        self.enter_HFTMC(self.business_interface_HTR, "")
        self.enter_name_business(self.name_of_the_business, "")
        self.enter_select_catagories(self.select_catagories, "")
        self.enter_phone_number(self.phone_number, "232456784")
        self.enter_email(self.business_interface_email, "")
        self.enter_city(self.city_business, "")
        self.enter_street(self.street_business, "")
        self.enter_house_number(self.house_number, "")
        self._click(self.submit_button)
        assert self.text_reading(self.submit_button) == ''

    @allure.description("Test valid categories invalid business name")
    @pytest.mark.sanity
    def test_business_register_valid_categories(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "")
        self.enter_lastname(self.business_interface_lastname, "")
        self.enter_HFTMC(self.business_interface_HTR, "")
        self.enter_name_business(self.name_of_the_business, "sdfgh")
        self.enter_select_catagories(self.select_catagories, "cocktail")
        self.enter_phone_number(self.phone_number, "2324567844567654345654")
        self.enter_email(self.business_interface_email, "")
        self.enter_city(self.city_business, "")
        self.enter_street(self.street_business, "")
        self.enter_house_number(self.house_number, "")
        self._click(self.submit_button)
        assert self.text_reading(self.submit_button) == ''

    @allure.description("Test valid user's registration")
    @pytest.mark.sanity
    def test_business_register_valid(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "erty")
        self.enter_lastname(self.business_interface_lastname, "ert")
        self.enter_HFTMC(self.business_interface_HTR, "1")
        self.enter_name_business(self.name_of_the_business, "sale")
        self.enter_select_catagories(self.select_catagories, "cocktail")
        self.enter_phone_number(self.phone_number, "2345634213")
        self.enter_email(self.business_interface_email, "asdfgh@gmail.com")
        self.enter_city(self.city_business, "bery")
        self.enter_street(self.street_business, "sdf")
        self.enter_house_number(self.house_number, "2")
        self._click(self.submit_button)

    @allure.description("Test invalid select categories invalid house number")
    @pytest.mark.sanity
    def test_business_register_invalid_select_categories(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self._entry(self.business_interface_firstname, "erty")
        self.enter_lastname(self.business_interface_lastname, "ert")
        self.enter_HFTMC(self.business_interface_HTR, "1")
        self.enter_name_business(self.name_of_the_business, "sale")
        self.enter_select_catagories(self.select_catagories, "")
        self.enter_phone_number(self.phone_number, "2345634213")
        self.enter_email(self.business_interface_email, "asdfgh@gmail.com")
        self.enter_city(self.city_business, "bery")
        self.enter_street(self.street_business, "sdf")
        self.enter_house_number(self.house_number, "0")
        self._click(self.submit_button)
        assert self.text_reading(self.submit_button) == ''

    @allure.description("Test the 'create new business' text is  aligned  correctly ")
    @pytest.mark.sanity
    def test_check_page_title(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self.text_reading(self.create_new_business)

    @allure.description("Test the header side of the business message logo image clikcable")
    @pytest.mark.sanity
    def test_check_image_message_logo_clikable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self.text_reading(self.create_new_business)
        self._click(self.message_image)

    @allure.description("Test the private business company name is aligned to users")
    @pytest.mark.sanity
    def test_private_business_company_name_read(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.business_interface_link)
        self.text_reading(self.private_business_company_name)

    @allure.description("Test the who we are link existing")
    @pytest.mark.sanity
    def test_who_are_you_link_clikcable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.who_are_link)

    @allure.description("Test the account link is clickable")
    @pytest.mark.sanity
    def test_account_link_clikcable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.account_link)

    @allure.description("Test trado logo link displayed correctly")
    @pytest.mark.sanity
    def test_eTrado_clikable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.eTrado_link)

    @allure.description("Test check on contact us link is working correctly")
    @pytest.mark.sanity
    def test_contact_clikable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.contact_us_link)

    @allure.description("Test check payment link is displayed")
    @pytest.mark.sanity
    def test_payment_clikcable(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.payment)

    @allure.description("Test check max button clikable")
    @pytest.mark.sanity
    def test_Max(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._click(self.MAX)

    @allure.description("Test the common question page of card container is aligned")
    @pytest.mark.sanity
    def test_container_text(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._is_displayed(self.card_container_but)

    @allure.description("Test the container title is aligned")
    @pytest.mark.sanity
    def test_container_right(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._is_displayed(self.container_right)

    @allure.description("Test check on how to pay title is displayed")
    @pytest.mark.sanity
    def test_do_i_pay_text(self):
        self.handling_the_first_popup()
        self.select_the_link()
        self._click(self.for_all_Question)
        self._is_displayed(self.how_do_i_pay)



























































