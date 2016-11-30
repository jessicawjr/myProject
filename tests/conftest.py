from unittest import mock
from selenium import webdriver
from baidu.tutorial import Baidu
import pytest


@pytest.fixture(scope="function")
def driver_mock():
    return mock.create_autospec(webdriver.Firefox)


@pytest.fixture(scope="function")
def bd(driver_mock):
    return Baidu(driver_mock)
