import pytest
from selenium import webdriver
from faker import Faker
from locators import Locators as L
import time

faker = Faker()

@pytest.fixture
def email():
    return faker.email()


# параметризованная фикстура автозакрывающегося драйвера, тест запустится на обоих браузерах
# https://roman.pt/posts/parametrizing-pytest-fixtures/
@pytest.fixture(params=[webdriver.Chrome, webdriver.Firefox])
def driver(request):
    driver = request.param()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def valid_credentials():
    return "HM@gmail.com", "123456"


@pytest.fixture
def logged_in_driver(driver, valid_credentials):
    email, password = valid_credentials
    driver.get("https://stellarburgers.nomoreparties.site")
    time.sleep(2)
    driver.find_element(*L.ACCOUNT_BUTTON).click()
    time.sleep(1)
    driver.find_element(*L.LOGIN_EMAIL).send_keys(email)
    driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(password)
    time.sleep(1)
    driver.find_element(*L.LOGIN_BUTTON).click()
    return driver

# driver.get("https://stellarburgers.nomoreparties.site/")


