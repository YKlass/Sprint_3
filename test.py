import time

import pytest
from locators import Locators as L
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestBurger:

    def test_registration(self, email, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(1)
        driver.find_element(*L.ACCOUNT_BUTTON).click()
        time.sleep(2)
        driver.find_element(*L.REGISTER_LINK).click()
        time.sleep(2)
        driver.find_element(*L.REGISTER_NAME).send_keys("HungryMan")
        driver.find_element(*L.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys("123456")
        time.sleep(2)
        driver.find_element(*L.REGISTER_BUTTON).click()
        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_password_error(self, email, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*L.REGISTER_NAME).send_keys("HungryMan")
        driver.find_element(*L.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys("123")
        time.sleep(2)
        driver.find_element(*L.REGISTER_BUTTON).click()
        time.sleep(3)
        error_text = driver.find_element(*L.INPUT_ERROR_CLASS).text
        assert error_text == "Некорректный пароль"

    def test_entrance_to_account(self, driver, valid_credentials):
        email, password = valid_credentials
        driver.get("https://stellarburgers.nomoreparties.site/")
        time.sleep(2)
        driver.find_element(*L.ACCOUNT_BUTTON).click()
        driver.find_element(*L.LOGIN_EMAIL).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(password)
        time.sleep(1)
        driver.find_element(*L.LOGIN_BUTTON).click()
        time.sleep(2)
        order_button = driver.find_element(*L.PLACE_ORDER_BUTTON)
        assert order_button is not None

    def test_entrance_personal_account(self, driver, valid_credentials):
        email, password = valid_credentials
        driver.get("https://stellarburgers.nomoreparties.site/")
        time.sleep(2)
        driver.find_element(*L.ACCOUNT_LINK).click()
        driver.find_element(*L.LOGIN_EMAIL).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(password)
        time.sleep(1)
        driver.find_element(*L.LOGIN_BUTTON).click()
        time.sleep(2)
        order_button = driver.find_element(*L.PLACE_ORDER_BUTTON)
        assert order_button is not None

    def test_entrance_registration_form(self, driver, valid_credentials):
        email, password = valid_credentials
        driver.get("https://stellarburgers.nomoreparties.site/")
        time.sleep(3)
        driver.find_element(*L.ACCOUNT_BUTTON).click()
        driver.find_element(*L.REGISTER_LINK).click()
        driver.find_element(*L.LOGIN_LINK).click()
        driver.find_element(*L.LOGIN_EMAIL).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(password)
        time.sleep(3)
        driver.find_element(*L.LOGIN_BUTTON).click()
        time.sleep(3)
        order_button = driver.find_element(*L.PLACE_ORDER_BUTTON)
        assert order_button is not None

    def test_entrance_forgot_password(self, driver, valid_credentials):
        email, password = valid_credentials
        driver.get("https://stellarburgers.nomoreparties.site/")
        time.sleep(5)
        driver.find_element(*L.ACCOUNT_BUTTON).click()
        driver.find_element(*L.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*L.LOGIN_LINK).click()
        time.sleep(5)
        driver.find_element(*L.LOGIN_EMAIL).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(password)
        time.sleep(3)
        driver.find_element(*L.LOGIN_BUTTON).click()
        time.sleep(3)
        order_button = driver.find_element(*L.PLACE_ORDER_BUTTON)
        assert order_button is not None

    def test_personal_account_opening(self, logged_in_driver):
        logged_in_driver.find_element(*L.ACCOUNT_LINK).click()
        time.sleep(2)
        assert logged_in_driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    @pytest.mark.parametrize('constructor_link', [
        L.BURGER_CONSTRUCTOR,
        L.LOGO_STELLAR
    ])
    def test_way_from_personal_account_to_constructor(self, logged_in_driver, constructor_link):
        logged_in_driver.find_element(*L.ACCOUNT_LINK).click()
        time.sleep(2)
        WebDriverWait(logged_in_driver, 3).until(EC.element_to_be_clickable(constructor_link)).click()
        time.sleep(3)
        assert logged_in_driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_exit(self, logged_in_driver):
        logged_in_driver.find_element(*L.ACCOUNT_LINK).click()
        time.sleep(2)
        logged_in_driver.find_element(*L.LOGOUT_BUTTON).click()
        time.sleep(1)
        assert logged_in_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_constructor_scroll_buns(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(L.BURGER_CONSTRUCTOR))
        element.click()
        driver.find_element(*L.SAUCES_BUTTON).click()
        buns = driver.find_element(*L.BUNS_HEADER)
        driver.find_element(*L.BUNS_BUTTON).click()
        assert buns.is_displayed()

    def test_constructor_scroll_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(L.FILLINGS_BUTTON)).click()
        fillings = driver.find_element(*L.FILLINGS_HEADER)
        assert fillings.is_displayed()

    def test_constructor_scroll_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(L.FILLINGS_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(L.SAUCES_BUTTON)).click()
        sauces = driver.find_element(*L.SAUCES_HEADER)
        assert sauces.is_displayed()
