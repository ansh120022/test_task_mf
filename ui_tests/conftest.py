from selenium import webdriver
import pytest
from query_page import QueryPage


class Browser:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_test_page(self, url):
        self.driver.get(url)


@pytest.fixture()
def bro():
    bro = Browser()
    bro.open_test_page(
        "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
    )
    bro.driver.find_element(*QueryPage.accept_choices).click()
    yield bro.driver
    bro.driver.close()
