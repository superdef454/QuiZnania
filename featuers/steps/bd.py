from behave import *
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# path = os получить путь до драйвера для разных компов но лень, поэтому:
path = "C:/Users/Пользователь/Desktop/работа/git/QuiZnania/featuers/chromedriver.exe"

@given('Страница "{url}" с объектом "{object}"')
def step(context, url, object):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    context.browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    context.browser.maximize_window()
    context.browser.get(url)
    element = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, object))
    )
    assert element, "Элемент не найден!"

@when('На странице бд выключить отображение объекта "{checkbox}" и сохранить изменения "{submit}"')
def step(context, checkbox, submit):
    element = WebDriverWait(context.browser, 120).until(
        # Как найти по тексту хз
        EC.element_to_be_clickable((By.XPATH, checkbox))
    ).click()
    element = WebDriverWait(context.browser, 120).until(
        # Как найти по тексту хз
        EC.element_to_be_clickable((By.XPATH, submit))
    ).click()

    
@then('На странице "{url}" пропадёт объект "{object}"')
def step(context, url, object):
    context.browser.get(url)
    element = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, object))
    )
    assert not element, "Объект не убрался"
    context.browser.quit()