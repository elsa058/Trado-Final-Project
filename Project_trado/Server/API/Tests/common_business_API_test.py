from Server.API.Constants.business_registration_locators import LoginConstants
import allure
import requests


class Test_Registration:
    @allure.description('valid registration user account')
    def test_login_correctly(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    @allure.description('Invalid registration user account')
    def test_login_correctly(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_invalid_email
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description('invalid user account phonenumbers')
    def test_login_correctly(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_invalid_phone_numbers
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10