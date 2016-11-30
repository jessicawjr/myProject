from baidu.tutorial import Baidu
from selenium import webdriver


def get_driver(context):
    return webdriver.Firefox()


def before_all(context):
    context.driver = get_driver(context)
    context.bd = Baidu(context.driver)
