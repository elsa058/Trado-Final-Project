from random import randint


class LoginConstants:
    num = randint(1, 2500)
    url_login = 'https://www.trado.co.il/api/user/registerUser'
    success_key = 'success'
    message_key_invalid = "store validation failed"
    data_valid = {"email": "elsa des", "password": f"elsa@{123}"}
    data_invalid_password = {"email": "elsdgh", "password": "123edsdf"}
    data_invalid_email = {"email": "m@fg", "password": "123456"}
    data_invalid_password_and_email = {"email": "m@fg", "password": "efgha123"}
    data_null_password_and_email = {"email": "","password":""}
    data_valid_business_name={"sales"}
    data_invalid_business_name={"hgfsdfghj"}
    data_valid_phone_numbers={"0568435216"}
    data_invalid_phone_numbers={"2436577643"}



