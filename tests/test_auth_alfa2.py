#python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe

import config
from pages.auth_page import AuthPage

def test_positive_reg(web_browser):
    page = AuthPage(web_browser)
    page.input_first_name_xpath = config.positive_first_name
    page.input_last_name_xpath = config.positive_last_name
    page.input_email_xpath = config.positive_email
    page.input_phone_xpath = config.positive_phone
    page.input_password_xpath = config.positive_password
    page.input_password_confirmation_xpath = config.positive_password_confirmation
    page.checkbox_xpath.click()
    page.button_registration_xpath.click()
    assert page.get_relative_link() == config.url_reg, 'ERROR positive_reg'

def test_clicking_logo(web_browser):
    page = AuthPage(web_browser)
    page.logo_xpath.click()
    assert page.get_relative_link() == config.url_login, 'ERROR clicking logo'

def test_clicking_terms_of_service(web_browser):
    page = AuthPage(web_browser)
    page.terms_of_service_xpath.click()
    page.switch_new()
    assert page.get_relative_link() == config.url_terms_of_service, 'ERROR clicking terms of service'

def test_clicking_withdrawal(web_browser):
    page = AuthPage(web_browser)
    page.withdrawal_xpath.click()
    page.switch_new()
    assert page.get_relative_link() == config.url_withdrawal, 'ERROR clicking withdrawal'

def test_clicking_already_registered(web_browser):
    page = AuthPage(web_browser)
    page.already_registered_xpath.click()
    assert page.get_relative_link() == config.url_login, 'ERROR clicking already registered'

def test_warning_first_name(web_browser):
    page = AuthPage(web_browser)
    page.input_first_name_xpath = config.negative_first_name

    page.input_last_name_xpath = config.positive_last_name
    page.input_email_xpath = config.positive_email
    page.input_phone_xpath = config.positive_phone
    page.input_password_xpath = config.positive_password
    page.input_password_confirmation_xpath = config.positive_password_confirmation
    page.checkbox_xpath.click()
    page.button_registration_xpath.click()

    assert page.warning_whoops_xpath.is_visible() and page.warning_first_name_xpath.is_visible(), 'Not found warning_first_name'

def test_warning_last_name(web_browser):
    page = AuthPage(web_browser)
    page.input_last_name_xpath = config.negative_last_name

    page.input_first_name_xpath = config.positive_first_name
    page.input_email_xpath = config.positive_email
    page.input_phone_xpath = config.positive_phone
    page.input_password_xpath = config.positive_password
    page.input_password_confirmation_xpath = config.positive_password_confirmation
    page.checkbox_xpath.click()
    page.button_registration_xpath.click()

    assert page.warning_whoops_xpath.is_visible() and page.warning_last_name_xpath.is_visible(), 'Not found warning_last_name'

def test_warning_password_rus(web_browser):
    page = AuthPage(web_browser)
    page.input_password_xpath = config.negative_password_rus
    page.input_password_confirmation_xpath = config.negative_password_rus

    page.input_first_name_xpath = config.positive_first_name
    page.input_last_name_xpath = config.positive_last_name
    page.input_email_xpath = config.positive_email
    page.input_phone_xpath = config.positive_phone
    page.checkbox_xpath.click()
    page.button_registration_xpath.click()
    
    assert page.warning_whoops_xpath.is_visible() and page.warning_password_rus_xpath.is_visible(), 'Not found warning_password_rus'

def test_warning_password_small(web_browser):
    page = AuthPage(web_browser)
    page.input_password_xpath = config.negative_password_small
    page.input_password_confirmation_xpath = config.negative_password_small

    page.input_first_name_xpath = config.positive_first_name
    page.input_last_name_xpath = config.positive_last_name
    page.input_email_xpath = config.positive_email
    page.input_phone_xpath = config.positive_phone
    page.checkbox_xpath.click()
    page.button_registration_xpath.click()

    assert page.warning_whoops_xpath.is_visible() and page.warning_password_small_xpath.is_visible(), 'Not found warning_password_small'

def test_warning_password_confirmation(web_browser):
    page = AuthPage(web_browser)
    page.input_password_xpath = config.positive_password
    page.input_password_confirmation_xpath = config.negative_password_confirmation

    page.input_first_name_xpath = config.positive_first_name
    page.input_last_name_xpath = config.positive_last_name
    page.input_email_xpath = config.positive_email
    page.input_phone_xpath = config.positive_phone
    page.checkbox_xpath.click()
    page.button_registration_xpath.click()

    assert page.warning_whoops_xpath.is_visible() and page.warning_password_confirmation_xpath.is_visible(), 'Not found warning_password_confirmation'
    
def test_label_first_name(web_browser):
    page = AuthPage(web_browser)
    assert page.label_first_name_xpath.is_visible(), 'Not found label_first_name'
    
def test_label_last_name(web_browser):
    page = AuthPage(web_browser)
    assert page.label_last_name_xpath.is_visible(), 'Not found label_last_name'
