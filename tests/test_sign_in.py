import time

from pages.auth_page import AuthPage
from pages.profile_page import ProfilePage


class TestAuthPage:
    wrong_password_error = "Не удаётся войти. Пожалуйста, проверьте правильность написания логина и пароля."
    no_such_user_error = "Пользователя с таким логином не существует"
    incorrect_email = 'E-mail введен некорректно'

    def test_sign_in(self, driver):
        profile_page = ProfilePage(driver)
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', '123123123')
        auth_page.submit()
        assert profile_page.get_login() == 'ktox', 'Неправильный логин'

    def test_sign_in_wrong_password(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', 'wrongpasswd')
        auth_page.submit()
        assert auth_page.get_error_message() == self.wrong_password_error

    def test_sign_in_no_such_user(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('nosuchuser', 'anypasswd')
        auth_page.submit()
        assert auth_page.get_error_message() == self.no_such_user_error

    def test_reset_password(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('email', 'password')
        auth_page.reset_password('email\n')
        # assert auth_page.get_error_message() == self.incorrect_email нет data-qa у сообщение об ошибке
