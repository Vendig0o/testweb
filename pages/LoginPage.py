from  pages.BasePage import BasePage
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
class LoginPageHelper(BasePage):
    pass