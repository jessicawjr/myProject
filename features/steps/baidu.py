from behave import *


@when('I go to baidu homepage')
def step_impl(context):
    context.bd.open_baidu()


@then('Baidu homepage is loaded')
def step_impl(conext):
    assert "www.baidu.com" in conext.bd.get_current_url()
