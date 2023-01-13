import time
import random
import allure

from conftest import BASE_URL, TEST_PROFILE_LOGIN, TEST_PROFILE_MAIL, TEST_PROFILE_PASSWORD, TEST_PROFILE_PHONE
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

    incorrect_code_2 = 'Код некорректен, осталась 2 попытки'
    incorrect_code_2_eng = 'Incorrect code, 2 attempts left'

    incorrect_code_1 = 'Код некорректен, осталась 1 попытка'
    incorrect_code_1_eng = 'Incorrect code, 1 attempt left'

    code_cancelled = 'Код аннулирован, запросите новый код'
    code_cancelled_eng = 'Code cancelled, request a new code'

    existing_phone = 'Аккаунт с таким номером телефона уже существует'
    existing_phone_eng = 'An account with the same phone number already exists'

    @allure.feature('Авторизация')
    @allure.story('Вход по логину')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешный вход')
    @allure.link('https://kiwi.pfm.team/case/304/')
    def test_sign_in_login(self, driver):  # 304
        profile_page = ProfilePage(driver)
        auth_page = AuthPage(driver)
        auth_page.sign_in_ktox()
        auth_page.open_my_profile()
        assert profile_page.get_login() == TEST_PROFILE_LOGIN, 'Неправильный логин в профиле'

    @allure.feature('Авторизация')
    @allure.story('Вход по почте')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешный вход')
    @allure.link('https://kiwi.pfm.team/case/305/')
    def test_sign_in_mail(self, driver):  # 305
        profile_page = ProfilePage(driver)
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail(TEST_PROFILE_MAIL, TEST_PROFILE_PASSWORD)
        auth_page.open_my_profile()
        assert profile_page.get_login() == TEST_PROFILE_LOGIN, 'Неправильный логин в профиле'

    @allure.feature('Авторизация')
    @allure.story('Вход по логину')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Неправильный пароль')
    @allure.link('https://kiwi.pfm.team/case/307/')
    def test_sign_in_with_login_wrong_password(self, driver):  # 307
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail(TEST_PROFILE_LOGIN, 'wrongpasswd')
        auth_page.check_error_message(self.wrong_password_error, self.wrong_password_error_eng)

    @allure.feature('Авторизация')
    @allure.story('Вход по почте')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Неправильный пароль')
    @allure.link('https://kiwi.pfm.team/case/307/')
    def test_sign_in_with_mail_wrong_password(self, driver):  # 307.2
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail(TEST_PROFILE_MAIL, 'wrongpasswd')
        auth_page.check_error_message(self.wrong_password_error, self.wrong_password_error_eng)

    @allure.feature('Авторизация')
    @allure.story('Вход по почте')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Некорректная почта')
    @allure.link('https://kiwi.pfm.team/case/308/')
    def test_sign_in_with_mail_incorrect(self, driver):  # 308
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail("incorrect@email", TEST_PROFILE_PASSWORD)
        auth_page.check_error_message(self.incorrect_email, self.incorrect_email_eng)

    @allure.feature('Авторизация')
    @allure.story('Вход по логину')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Неправильный логин')
    @allure.link('https://kiwi.pfm.team/case/383/')
    def test_sign_in_no_such_user(self, driver):  # 383
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('nosuchuser', 'anypasswd')
        auth_page.check_error_message(self.no_such_user_error, self.no_such_user_error_eng)

    @allure.feature('Авторизация')
    @allure.story('Вход по телефону')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешный вход')
    @allure.link('https://kiwi.pfm.team/case/388/')
    def test_sign_in_with_phone(self, driver):  # 388
        auth_page = AuthPage(driver)
        profile_page = ProfilePage(driver)
        auth_page.sign_in_with_phone(TEST_PROFILE_PHONE)
        auth_page.send_code_6666()
        auth_page.open_my_profile()
        assert profile_page.get_login() == 'o5smwc_oqmycew7l', 'Неправильный логин в профиле'  # пока не могу привязать номер к тестовому аккаунту

    @allure.feature('Авторизация')
    @allure.story('Вход по телефону')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Неправильный код')
    @allure.link('https://kiwi.pfm.team/case/389/')
    def test_sign_in_with_phone_wrong_code(self, driver):  # 389
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_phone(TEST_PROFILE_PHONE)
        auth_page.send_random_code()
        auth_page.check_error_message(self.incorrect_code_2, self.incorrect_code_2_eng)  # ошибка (2 попытки)
        auth_page.submit()  # еще один клик
        auth_page.check_error_message(self.incorrect_code_1, self.incorrect_code_1_eng)  # ошибка (1 попытка)
        auth_page.submit()  # еще один клик
        auth_page.check_error_message(self.code_cancelled, self.code_cancelled_eng)  # ошибка (код аннулирован)

    @allure.feature('Восстановление пароля')
    @allure.story('Восстановление пароля по почте')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Некорректная почта')
    @allure.link('https://kiwi.pfm.team/case/311/')
    def test_reset_password_incorrect_mail(self, driver):  # 311
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('incorrect@email', 'password')
        auth_page.reset_password_with_mail('incorrect_mail')
        auth_page.check_error_message(self.incorrect_email, self.incorrect_email_eng)

    @allure.feature('Восстановление пароля')
    @allure.story('Восстановление пароля по почте')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Незарегистрированная почта')
    @allure.link('https://kiwi.pfm.team/case/312/')
    def test_reset_password_unregistered_mail(self, driver):  # 312
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('unregistered@mail.ru', 'password')
        auth_page.reset_password_with_mail('somefakemail@mail.ru')
        auth_page.check_error_message(self.unregistered_email, self.unregistered_email_eng)

    # @allure.feature('Восстановление пароля')
    # @allure.story('Восстановление пароля по телефону')
    # @allure.severity(allure.severity_level.MINOR)
    # @allure.title('Неправильный код')
    # @allure.link('https://kiwi.pfm.team/case/312/')
    # def test_reset_password_unregistered_mail(self, driver):  # 312
    #     auth_page = AuthPage(driver)

    # @allure.feature('Восстановление пароля')
    # @allure.story('Восстановление пароля по телефону')
    # @allure.severity(allure.severity_level.MINOR)
    # @allure.title('Незарегистрированный телефон')
    # @allure.link('https://kiwi.pfm.team/case/312/')
    # def test_reset_password_unregistered_mail(self, driver):  # 312
    #     auth_page = AuthPage(driver)

    # @allure.feature('Восстановление пароля')
    # @allure.story('Восстановление пароля по телефону')
    # @allure.severity(allure.severity_level.MINOR)
    # @allure.title('Успешный сброс')
    # @allure.link('https://kiwi.pfm.team/case/312/')
    # def test_reset_password_unregistered_mail(self, driver):  # 312
    #     auth_page = AuthPage(driver)

    @allure.feature('Регистрация')
    @allure.story('Регистрация по почте')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Несовпадающие пароли')
    @allure.link('https://kiwi.pfm.team/case/315/')
    def test_register_password_mismatch(self, driver):  # 315
        auth_page = AuthPage(driver)
        auth_page.sign_up_with_mail('notexistingmail@inbox.ru', '123123123', '12312312')
        auth_page.check_error_message(self.password_mismatch, self.password_mismatch_eng)

    @allure.feature('Регистрация')
    @allure.story('Регистрация по почте')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Некорректная почта')
    @allure.link('https://kiwi.pfm.team/case/316/')
    def test_register_incorrect_mail(self, driver):  # 316
        auth_page = AuthPage(driver)
        auth_page.sign_up_with_mail('ktoxsyrovv@inboxru', '123123123', '123123123')
        auth_page.check_error_message(self.incorrect_email, self.incorrect_email_eng)

    @allure.feature('Регистрация')
    @allure.story('Регистрация по почте')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Занятая почта')
    @allure.link('https://kiwi.pfm.team/case/317/')
    def test_register_with_existing_mail(self, driver):  # 317
        auth_page = AuthPage(driver)
        auth_page.sign_up_with_mail(TEST_PROFILE_MAIL, '123123123', '123123123')
        auth_page.check_error_message(self.existing_mail, self.existing_mail_eng)

    @allure.feature('Регистрация')
    @allure.story('Регистрация по телефону')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешная регистрация')
    @allure.link('https://kiwi.pfm.team/case/313/')
    def test_sign_up_with_phone(self, driver):  # 313
        auth_page = AuthPage(driver)
        random_phone = random.randint(10000000000, 99999999999)
        auth_page.sign_up_with_phone(random_phone)
        auth_page.send_code_6666()
        assert auth_page.is_logged_in(), 'Пользователь не авторизован'

    @allure.feature('Регистрация')
    @allure.story('Регистрация по телефону')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Занятый телефон')
    @allure.link('https://kiwi.pfm.team/case/384/')
    def test_sign_up_with_existing_phone(self, driver):  # 384
        auth_page = AuthPage(driver)
        auth_page.sign_up_with_phone(TEST_PROFILE_PHONE)
        auth_page.check_error_message(self.existing_phone, self.existing_phone_eng)

    @allure.feature('Регистрация')
    @allure.story('Регистрация по почте')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Несовпадающие пароли')
    @allure.link('https://kiwi.pfm.team/case/318/')
    def test_sign_up_password_not_match_requirement(self, driver):  # 318
        auth_page = AuthPage(driver)
        auth_page.sign_up_with_mail('newnew@inbox.ru', '123', '123')
        auth_page.check_error_message(self.password_not_match_requirements, self.password_not_match_requirements_eng)

    @allure.feature('Регистрация')
    @allure.story('Регистрация по телефону')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Неправильный код')
    @allure.link('https://kiwi.pfm.team/case/320/')
    def test_sign_up_with_phone_incorrect_code(self, driver):  # 320
        auth_page = AuthPage(driver)
        auth_page.sign_up_with_phone('79689061499')
        auth_page.send_random_code()
        auth_page.check_error_message(self.incorrect_code_2, self.incorrect_code_2_eng)  # ошибка (2 попытки)
        auth_page.submit()  # еще один клик
        auth_page.check_error_message(self.incorrect_code_1, self.incorrect_code_1_eng)  # ошибка (1 попытка)
        auth_page.submit()  # еще один клик
        auth_page.check_error_message(self.code_cancelled, self.code_cancelled_eng)  # ошибка (код аннулирован)

    @allure.feature('Регистрация')
    @allure.story('Регистрация по почте')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Неправильный код')
    @allure.link('https://kiwi.pfm.team/case/319/')
    def test_sign_up_with_mail_incorrect_code(self, driver):  # 319
        auth_page = AuthPage(driver)
        auth_page.sign_up_with_mail('notexistingmail@mail.ru', '123123123', '123123123')
        auth_page.send_random_code()
        auth_page.check_error_message(self.incorrect_code_2, self.incorrect_code_2_eng)  # ошибка (2 попытки)
        auth_page.submit()  # еще один клик
        auth_page.check_error_message(self.incorrect_code_1, self.incorrect_code_1_eng)  # ошибка (1 попытка)
        auth_page.submit()  # еще один клик
        auth_page.check_error_message(self.code_cancelled, self.code_cancelled_eng)  # ошибка (код аннулирован)

    @allure.feature('Переход на страницу авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Кнопка в правом верхнем углу')
    @allure.link('https://kiwi.pfm.team/case/323/')
    def test_corner_auth_button(self, driver):  # 323
        auth_page = AuthPage(driver)
        auth_page.top_corner_sign_in_button_click()
        assert driver.current_url == BASE_URL + '/auth', 'не открывается страница входа при клике на кнопку в углу'

    @allure.feature('Переход на страницу авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Кнопка в центре')
    @allure.link('https://kiwi.pfm.team/case/324/')
    def test_center_auth_button(self, driver):  # 324
        auth_page = AuthPage(driver)
        auth_page.center_sign_in_button_click()
        assert driver.current_url == BASE_URL + '/auth', 'не открывается страница входа при клике на кнопку в центре'
