from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utilities.constants import EBAY_URL


class Bot:
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def open_home_page(self):
        self.driver.get(EBAY_URL)
        return HomePage(self.driver)

    def search_for_product(self, query):
        home_page = self.open_home_page()
        home_page.type_query(query)
        return SearchPage(self.driver)

    def choose_category(self, category):
        home_page = self.open_home_page()
        home_page.choose_category(category)
        return SearchPage(self.driver)

    def filter_search_results(self):
        search_page = SearchPage(self.driver)
        search_page.filtration()

    def scrape_results(self, amount=10):
        search_results_page = SearchPage(self.driver)
        return search_results_page.scrap_results(amount)