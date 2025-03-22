from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    ERROR_MESSAGE = (By.CLASS_NAME, "alert-danger")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


    def get_login_page(self):
        self.open_url(f'{self.url}/login')

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    def authenticated_user(self, username, password):
        self.open_url(f'{self.url}/login')
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)