import time

from pages.auth_page import AuthPage
from pages.profile_page import ProfilePage


class TestAuthPage:
    # тексты ошибок
    wrong_password_error = "Не удаётся войти. Пожалуйста, проверьте правильность написания логина и пароля."
    wrong_password_error_eng = 'Wrong credentials. Please check your login and password.'

    no_such_user_error = "Пользователя с таким логином не существует"
    no_such_user_error_eng = 'User with this login is not registered'

    incorrect_email = 'E-mail введен некорректно'
    incorrect_email_eng = 'Please check the e-mail is correct'

    unregistered_email = 'Данный e-mail не зарегистрирован'
    unregistered_email_eng = 'User with this e-mail is not registered'

    password_mismatch = 'Пароли не совпадают'
    password_mismatch_eng = 'Password mismatch'

    existing_mail = 'Аккаунт с таким e-mail уже существует'
    existing_mail_eng = 'An account with the same e-mail already exists'

    password_not_match_requirements = 'Пароль не соответствует требованиям'
    password_not_match_requirements_eng = 'Password does not match requirements'

    incorrect_code = 'Код некорректен, осталась 2 попытки'
    incorrect_code_eng = 'Incorrect code, 2 attempt left'

    def test_sign_in_login(self, driver):  # 304
        profile_page = ProfilePage(driver)
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', '123123123')
        auth_page.open_my_profile()
        assert profile_page.get_login() == 'ktox', 'Неправильный логин в профиле'

    def test_sign_in_mail(self, driver):  # 305
        profile_page = ProfilePage(driver)
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktoxsyrovv@inbox.ru', '123123123')
        auth_page.open_my_profile()
        assert profile_page.get_login() == 'ktox', 'Неправильный логин в профиле'

    def test_sign_in_with_login_wrong_password(self, driver):  # 307
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', 'wrongpasswd')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.wrong_password_error
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.wrong_password_error_eng

    def test_sign_in_with_mail_wrong_password(self, driver):  # 307.2
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktoxsyrovv@inbox.ru', 'wrongpasswd')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.wrong_password_error
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.wrong_password_error_eng

    def test_sign_in_with_mail_incorrect(self, driver):  # 308
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktoxsyrovv@inbox', '123123123')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.wrong_password_error
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.wrong_password_error_eng

    def test_sign_in_no_such_user(self, driver):  # 383
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('nosuchuser', 'anypasswd')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.no_such_user_error
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.no_such_user_error_eng

    def test_reset_password_incorrect_mail(self, driver):  # 311
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

    def test_reset_password_unregistered_mail(self, driver):  # 312
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

    def test_register_password_mismatch(self, driver):  # 315
        auth_page = AuthPage(driver)
        auth_page.register_with_mail('ktoxsyrovv@inbox.ru', '123123123', '12312312')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.password_mismatch
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.password_mismatch_eng

    def test_register_incorrect_mail(self, driver):  # 316
        auth_page = AuthPage(driver)
        auth_page.register_with_mail('ktoxsyrovv@inboxru', '123123123', '123123123')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.incorrect_email
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.incorrect_email_eng

    def test_register_existing_mail(self, driver):  # 317
        auth_page = AuthPage(driver)
        auth_page.register_with_mail('ktoxsyrovv@inbox.ru', '123123123', '123123123')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.existing_mail
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.existing_mail_eng

    def test_register_password_not_match_requirement(self, driver):  # 318
        auth_page = AuthPage(driver)
        auth_page.register_with_mail('newnew@inbox.ru', '123', '123')
        # ошибка
        error = auth_page.get_reset_error_message()
        assert error == self.password_not_match_requirements
        # ошибка на англ
        auth_page.switch_lang_to_en()
        error_eng = auth_page.get_reset_error_message()
        assert error_eng == self.password_not_match_requirements_eng

    def test_sign_in_with_phone(self, driver):  # 320
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_phone('9689061499')
        auth_page.send_random_code()
        auth_page.submit()
        error = auth_page.get_register_error_message()
        assert error == self.incorrect_code
        time.sleep(10)




