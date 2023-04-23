from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.search_page import SearchPage
from utilities.logs_and_data import LogsAndData


class HomePage(BasePage):
    logs = LogsAndData.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def choose_category(self, category):
        category_filter = self.driver.find_element(By.ID, 'gh-cat')
        category_filter.click()
        cat = self.driver.find_element(By.XPATH, f'//select[@id="gh-cat"]/option[contains(text(), "{category}")]')
        cat.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'gh-cat')))

    def type_query(self, query):
        search_box = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'gh-ac')))
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

    def input_cat_and_query(self, cat, this_query):
        self.choose_category(category=cat)
        self.type_query(query=this_query)
        self.logs.debug("inputted query: " + this_query)
        search_click_result = SearchPage(self.driver)
        return search_click_result  # Making connection between pages
