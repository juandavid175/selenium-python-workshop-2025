from behave import given,when, then
from selenium.webdriver import chrome
from selenium import webdriver
from pages.mercadoLibre_page1 import Page1
import time

@given('estoy en la pagina de inicio de mercado libre')
def step_given_mercadoLibre1(context):
    chrome.driver = webdriver.Chrome()
    context.driver.get("https://www.mercadolibre.com.co/")
    context.login_page = Page1(context.driver)

@when('el usuario ingresa bien los datos')
def step_when_mercadoLibre1(context):
    context.login_page.find("iphone 13")
    time.sleep(2) 

@then('el usuario es redirigido a la pagina de interes')
def step_then_mercadoLibre1(context):
    expected_url = "https://listado.mercadolibre.com.co/iphone-13"
    assert expected_url in context.driver.current_url, f"No redirigió correctamente. URL actual: {context.driver.current_url}"
    context.driver.quit()