import config
from pages.base import WebPage
from pages.elements import WebElement

class AuthPage(WebPage):

    def __init__(self, web_driver):
        url = config.url_base + config.url_reg
        super().__init__(web_driver, url)

    input_first_name_xpath = WebElement(xpath = '//input[@name="first_name"]')
    input_last_name_xpath = WebElement(xpath = '//input[@name="last_name"]')
    input_email_xpath = WebElement(xpath = '//input[@name="email"]')
    input_phone_xpath = WebElement(xpath = '//input[@name="phone"]')
    input_password_xpath = WebElement(xpath = '//input[@name="password"]')
    input_password_confirmation_xpath = WebElement(xpath = '//input[@name="password_confirmation"]')
    checkbox_xpath = WebElement(xpath = '//input[@type="checkbox"]')
    button_registration_xpath = WebElement(xpath = '//button')

    logo_xpath = WebElement(xpath = '//img')
    terms_of_service_xpath = WebElement(xpath = '//a[text() = "Условиями предоставления доступа"]')
    withdrawal_xpath = WebElement(xpath = '//a[text() = "Условиями вывода средств"]')
    already_registered_xpath = WebElement(xpath = '//form/div/a')

    warning_whoops_xpath = WebElement(xpath = '//div[@class="mb-4"]/div[text() = "Whoops! Something went wrong."]')
    warning_first_name_xpath = WebElement(xpath = '//ul/li[text() = "Поле Имя может содержать только латинские символы"]')
    warning_last_name_xpath = WebElement(xpath = '//ul/li[text() = "Поле Фамилия может содержать только латинские символы"]')
    warning_password_rus_xpath = WebElement(xpath = '//ul/li[text() = "Поле Пароль может содержать только латинские символы и цифры"]')
    warning_password_small_xpath = WebElement(xpath = '//ul/li[text() = "The Пароль must be at least 8 characters."]')
    warning_password_confirmation_xpath = WebElement(xpath = '//ul/li[text() = "Поле Пароль не совпадает с подтверждением."]')

    label_first_name_xpath = WebElement(xpath = '(//label[@class="block font-medium text-sm text-gray-700"])[1]')
    label_last_name_xpath = WebElement(xpath = '(//label[@class="block font-medium text-sm text-gray-700"])[2]')
