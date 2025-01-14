import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL ="https://ok.ru/"
@allure.suite("Проверка регистрации")
@allure.title("Проверка страны и ее номера")
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    SelectedCountryCode = RegistrationPage.select_random_country()
    ActualCountryCode = RegistrationPage.get_phone_field_value()
    with allure.step("Проверяем актуальный код с предполагаемым"):
        assert SelectedCountryCode == ActualCountryCode