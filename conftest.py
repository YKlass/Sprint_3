import pytest
from selenium import webdriver
from locators import Locators as L
from helper import ValidCredentials, Urls


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.MAIN)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    driver.find_element(*L.ACCOUNT_BUTTON).click()
    driver.find_element(*L.LOGIN_EMAIL).send_keys(ValidCredentials.email)
    driver.find_element(*L.PASSWORD_INPUT_NAME).send_keys(ValidCredentials.password)
    driver.find_element(*L.LOGIN_BUTTON).click()
    return driver
