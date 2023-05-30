import pytest
from locators import Locators as L
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from helper import Urls, ValidCredentials as VC

faker = Faker()


class TestBurger:

    def test_registration(self, driver):
        driver.find_element(*L.ACCOUNT_BUTTON).click()
        driver.find_element(*L.REGISTER_LINK).click()
        driver.find_element(*L.REGISTER_NAME).send_keys("HungryMan")
        driver.find_element(*L.REGISTER_EMAIL).send_keys(faker.email())
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys("123456")
        driver.find_element(*L.REGISTER_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_changes(Urls.REGISTER))
        assert driver.current_url == Urls.LOGIN, "Нет редиректа на страницу логина после регистрации"

    def test_password_error(self, driver):
        driver.get(Urls.REGISTER)
        driver.find_element(*L.REGISTER_NAME).send_keys("HungryMan")
        driver.find_element(*L.REGISTER_EMAIL).send_keys(faker.email())
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys("123")
        driver.find_element(*L.REGISTER_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.INPUT_ERROR_CLASS))
        error_text = driver.find_element(*L.INPUT_ERROR_CLASS).text
        assert error_text == "Некорректный пароль"

    def test_entrance_to_account(self, driver):
        driver.find_element(*L.ACCOUNT_BUTTON).click()
        driver.find_element(*L.LOGIN_EMAIL).send_keys(VC.email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(VC.password)
        driver.find_element(*L.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.PLACE_ORDER_BUTTON))
        order_button = driver.find_element(*L.PLACE_ORDER_BUTTON)
        assert order_button is not None

    def test_entrance_personal_account(self, driver):
        driver.find_element(*L.ACCOUNT_LINK).click()
        driver.find_element(*L.LOGIN_EMAIL).send_keys(VC.email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(VC.password)
        driver.find_element(*L.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.PLACE_ORDER_BUTTON))
        order_button = driver.find_element(*L.PLACE_ORDER_BUTTON)
        assert order_button is not None

    def test_entrance_registration_form(self, driver):
        driver.find_element(*L.ACCOUNT_BUTTON).click()
        driver.find_element(*L.REGISTER_LINK).click()
        driver.find_element(*L.LOGIN_LINK).click()
        driver.find_element(*L.LOGIN_EMAIL).send_keys(VC.email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(VC.password)
        driver.find_element(*L.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.PLACE_ORDER_BUTTON))
        order_button = driver.find_element(*L.PLACE_ORDER_BUTTON)
        assert order_button is not None

    def test_entrance_forgot_password(self, driver):
        driver.find_element(*L.ACCOUNT_BUTTON).click()
        driver.find_element(*L.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*L.LOGIN_LINK).click()
        driver.find_element(*L.LOGIN_EMAIL).send_keys(VC.email)
        driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(VC.password)
        driver.find_element(*L.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(L.PLACE_ORDER_BUTTON))
        order_button = driver.find_element(*L.PLACE_ORDER_BUTTON)
        assert order_button is not None

    def test_personal_account_opening(self, logged_in_driver):
        logged_in_driver.find_element(*L.ACCOUNT_LINK).click()
        WebDriverWait(logged_in_driver, 2).until(EC.url_changes(Urls.ACCOUNT))
        assert logged_in_driver.current_url == Urls.PROFILE

    @pytest.mark.parametrize('constructor_link', [L.BURGER_CONSTRUCTOR, L.LOGO_STELLAR])
    def test_way_from_personal_account_to_constructor(self, logged_in_driver, constructor_link):
        logged_in_driver.find_element(*L.ACCOUNT_LINK).click()
        WebDriverWait(logged_in_driver, 3).until(EC.element_to_be_clickable(constructor_link)).click()
        assert logged_in_driver.current_url == Urls.MAIN

    def test_exit(self, logged_in_driver):
        logged_in_driver.find_element(*L.ACCOUNT_LINK).click()
        WebDriverWait(logged_in_driver, 3).until(EC.element_to_be_clickable(L.LOGOUT_BUTTON)).click()
        WebDriverWait(logged_in_driver, 2).until(EC.url_changes(Urls.PROFILE))
        assert logged_in_driver.current_url == Urls.LOGIN

    def test_constructor_scroll_buns(self, driver):
        element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(L.BURGER_CONSTRUCTOR))
        element.click()
        driver.find_element(*L.SAUCES_BUTTON).click()
        buns = driver.find_element(*L.BUNS_HEADER)
        driver.find_element(*L.BUNS_BUTTON).click()
        assert buns.is_displayed()

    def test_constructor_scroll_fillings(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(L.FILLINGS_BUTTON)).click()
        fillings = driver.find_element(*L.FILLINGS_HEADER)
        assert fillings.is_displayed()

    def test_constructor_scroll_sauces(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(L.FILLINGS_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(L.SAUCES_BUTTON)).click()
        sauces = driver.find_element(*L.SAUCES_HEADER)
        assert sauces.is_displayed()
