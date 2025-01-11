from  pages.BasePage import BasePage
from  selenium.webdriver.common.by import By
from  selenium.webdriver.remote import webelement
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
class LoginPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
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
    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def send_login(self,text):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text)


    def get_error_text(self):
        return  self.find_element(LoginPageLocators.ERROR_TEXT).text