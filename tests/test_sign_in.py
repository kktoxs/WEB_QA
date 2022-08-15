import time

from pages.auth_page import AuthPage
from pages.profile_page import ProfilePage


class TestAuthPage:
    wrong_password_error = "Не удаётся войти. Пожалуйста, проверьте правильность написания логина и пароля."
    wrong_password_error_eng = 'Wrong credentials. Please check your login and password.'

    no_such_user_error = "Пользователя с таким логином не существует"
    no_such_user_error_eng = 'User with this login is not registered'

    incorrect_email = 'E-mail введен некорректно'
    incorrect_email_eng = 'Please check the e-mail is correct'

    unregistered_email = 'Данный e-mail не зарегистрирован'
    unregistered_email_eng = 'User with this e-mail is not registered'

    def test_sign_in(self, driver):
        profile_page = ProfilePage(driver)
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', '123123123')
        # auth_page.submit()
        assert profile_page.get_login() == 'ktox', 'Неправильный логин в профиле'

    def test_sign_in_wrong_password(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', 'wrongpasswd')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.wrong_password_error
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.wrong_password_error_eng

    def test_sign_in_no_such_user(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('nosuchuser', 'anypasswd')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.no_such_user_error
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.unregistered_email_eng

    def test_reset_password_incorrect(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('email', 'password')
        auth_page.reset_password('email\n')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.incorrect_email
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.incorrect_email_eng

    def test_reset_password_unregistered(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('email', 'password')
        auth_page.reset_password('somefakemail@mail.ru\n')
        time.sleep(1)
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.unregistered_email
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.unregistered_email_eng
