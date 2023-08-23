from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger("test sql executor")


class QueryPage:
    def __init__(self, bro):
        self.bro = bro

    update_result = (
        By.XPATH,
        "//div[.='You have made changes to the database. Rows affected: 1']",
    )
    code_area = (By.CSS_SELECTOR, ".cm-m-sql:nth-child(4)")
    code_input = (By.CSS_SELECTOR, "textarea:nth-child(1)")
    run_button = (By.CSS_SELECTOR, ".ws-btn")
    accept_choices = (By.ID, "accept-choices")

    def send_query(self, query):
        self.bro.find_element(*self.code_area).click()
        code_input = self.bro.find_element(*self.code_input)
        actions = ActionChains(self.bro)
        actions.move_to_element(code_input).double_click().click_and_hold().send_keys(
            Keys.CLEAR
        ).send_keys(query).perform()
        self.bro.find_element(*self.run_button).click()
        logging.info(f"Running query: {query}")

    def wait_for_expected_result(self, expected_result):
        expected_result = By.XPATH, f"//tr/td[.='{expected_result}']"
        try:
            WebDriverWait(self.bro, 10).until(
                EC.presence_of_element_located(expected_result)
            )
            return "Found"
        except:
            TimeoutError

    def check_update_status(self):
        try:
            WebDriverWait(self.bro, 10).until(
                EC.presence_of_element_located(self.update_result)
            )
            return "Found"
        except:
            TimeoutError
