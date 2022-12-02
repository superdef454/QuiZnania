from behave import *
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# path = os получить путь до драйвера для разных компов но лень, поэтому:
# path = "C:/Users/Пользователь/Desktop/работа/git/QuiZnania/featuers/chromedriver.exe"
path = "C:/Users/user/Documents/учёба/git/QuiZnania/featuers/chromedriver.exe"


#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('Запущен сайт "{url}"')
def step(context, url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    context.browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    context.browser.maximize_window()
    context.browser.get(url)

@when('Пользователь нажимает на кнопку с названием "{name}"')
def step(context, name):
    element = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/a"))
    )
    element.click()

@then("Открывается страница с выбром раздела")
def step(context):
    element = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'text__third__screen'))
    )
    assert element
    context.browser.quit()

# bd.py

@given('Страница "{url}" с объектом "{object}"')
def step(context, url, object):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    context.browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    context.browser.maximize_window()
    context.browser.get(url)
    try:
        context.check = WebDriverWait(context.browser, 2).until(
            EC.presence_of_element_located((By.XPATH, object))
        )
    except Exception as e:
        context.check = False

@when('На странице бд "{url}" выключить отображение объекта "{checkbox}" и сохранить изменения "{submit}"')
def step(context, url, checkbox, submit):
    context.browser.get(url)
    element = WebDriverWait(context.browser, 10).until(
        # Как найти по тексту хз
        EC.element_to_be_clickable((By.XPATH, checkbox))
    ).click()
    element = WebDriverWait(context.browser, 10).until(
        # Как найти по тексту хз
        EC.element_to_be_clickable((By.XPATH, submit))
    ).click()

    
@then('На странице "{url}" пропадёт объект "{object}"')
def step(context, url, object):
    context.browser.get(url)
    try:
        element = WebDriverWait(context.browser, 2).until(
            EC.presence_of_element_located((By.XPATH, object))
        )
    except Exception as e:
        element = False
    context.browser.quit()
    assert element != context.check, "Объект не изменился"
    