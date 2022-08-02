from pages.auth_page import AuthPage


class TestAuthPage:
    wrong_password_error = "Не удаётся войти. Пожалуйста, проверьте правильность написания логина и пароля."
    no_such_user_error = "Пользователя с таким логином не существует"

    def test_sign_in(self, driver):
        auth_page = AuthPage(driver, 'https://planetfor.me/')
        auth_page.open()
        auth_page.sign_in_with_mail('ktox', '123456789')

    def test_sign_in_wrong_password(self, driver):
        auth_page = AuthPage(driver, 'https://planetfor.me/')
        auth_page.open()
        auth_page.sign_in_with_mail('ktox', 'wrongpasswd')
        assert auth_page.get_error_message() == self.wrong_password_error

    def test_sign_in_no_such_user(self, driver):
        auth_page = AuthPage(driver, 'https://planetfor.me/')
        auth_page.open()
        auth_page.sign_in_with_mail('nosuchuser', 'anypasswd')
