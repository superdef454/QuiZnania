from behave import *
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# path = os получить путь до драйвера для разных компов но лень, поэтому:
path = "C:/Users/Пользователь/Desktop/работа/git/QuiZnania/featuers/requirements.txt"

#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@step('Запущен сайт "{url}"')
def step(context, url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    context.browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    context.browser.maximize_window()
    context.browser.get(url)

@step("Пользователь выбирает первый раздел, первую тему, первый раунд и прокликивает до конца")
def step(context):
    pass

@step("Пользователь выбирает первый раздел, первую тему, первый раунд и прокликивает до конца")
def step(context):
    context.browser.quit()

# # найдём и нажмём на кнопку
# @When("push button with div '{text}'")
# def step(context, text):
#     element = WebDriverWait(context.browser, 120).until(
#         EC.element_to_be_clickable((By.CLASS_NAME, text))
#     )
#     element.click()

# #Проверим, что мы на странице с результатами поиска, есть некоторый искомый див
# @then("page include div '{text}'")
# def step(context, text):
#     element = WebDriverWait(context.browser, 120).until(
#         EC.presence_of_element_located((By.CLASS_NAME, text))
#     )
#     # assert element
#     context.browser.quit()