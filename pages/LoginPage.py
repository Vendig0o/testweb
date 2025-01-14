import allure
from  pages.BasePage import BasePageHelper
from  selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH,'//*[@data-l="t,login_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    CANT_LOG_IN =(By.XPATH,'//*[@tsid="restore"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login_title mt-6x"]')
    PROFILE_RECOVERY_BUTTON = (By.NAME, 'st.go_to_recovery')
class LoginPageHelper(BasePageHelper):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()

    @allure.step("Проверяем наличие указанных элементов")
    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.CANT_LOG_IN)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)
    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Отправляем текст в окно ввода логина")
    def send_login(self,text):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text)

    @allure.step("Отправляем текст в окно ввода пароля")
    def send_password(self, text):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(text)


    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return  self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step("перейти к востановалению")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()

    @allure.step("Переходим к регистрации")
    def click_registration(self):
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()