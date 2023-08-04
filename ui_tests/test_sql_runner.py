import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger("test sql executor")


class Browser:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options)
        logging.info("Running Chrome")

    def open_test_page(self, url):
        self.driver.get(url)


@pytest.fixture()
def bro():
    bro = Browser()
    bro.open_test_page(
        "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
    )
    bro.driver.find_element(By.ID, "accept-choices").click()
    yield bro.driver
    bro.driver.close()


query_1 = """
            SELECT address
            FROM customers
            WHERE ContactName = 'Giovanni Rovelli'
        """
query_2 = """
            SELECT count(*)
            FROM customers
            WHERE city='London'
        """


class QueryPage:
    def __init__(self, bro):
        self.bro = bro

    def fill_query_field(self, query):
        self.bro.find_element(By.CSS_SELECTOR, '.cm-m-sql:nth-child(4)').click()
        code_input = self.bro.find_element(By.CSS_SELECTOR, "textarea:nth-child(1)")
        actions = ActionChains(self.bro)
        actions.move_to_element(code_input).double_click().click_and_hold().send_keys(
            Keys.CLEAR
        ).send_keys(query).perform()


@pytest.mark.parametrize(
    "query, expected_result", [(query_1, "Via Ludovico il Moro 22"), (query_2, "6")]
)
def test_execute_query(bro, query, expected_result):
    QueryPage(bro).fill_query_field(query)
    bro.find_element(By.CSS_SELECTOR, ".ws-btn").click()
    logging.info(f"Running query: {query}")
    expected_result = By.XPATH, f"//tr/td[.='{expected_result}']"
    assert WebDriverWait(bro, 10).until(
        EC.presence_of_element_located(expected_result)
    ), f"Expected result {expected_result} not found "
