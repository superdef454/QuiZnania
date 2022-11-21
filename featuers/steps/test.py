from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('website "{url}"')
def step(context, url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    context.browser = webdriver.Chrome(executable_path="C:/Users/user/Documents/учёба/Работы/QuiZ/featuers/chromedriver.exe", chrome_options=chrome_options)
    context.browser.maximize_window()
    context.browser.get(url)

# найдём и нажмём на кнопку
@When("push button with div '{text}'")
def step(context, text):
    element = WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.CLASS_NAME, text))
    )
    element.click()

#Проверим, что мы на странице с результатами поиска, есть некоторый искомый див
@then("page include div '{text}'")
def step(context, text):
    element = WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.CLASS_NAME, text))
    )
    # assert element
    context.browser.quit()