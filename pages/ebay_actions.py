#  Library import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from prettytable import PrettyTable

#  File import
import utilities.constants as const
from utilities.ebay_filtration import EbayFiltration
from utilities.ebay_scrap import EbayScrap

"""
Run.py uses 'with' for context managing 
__exit__ magic function runs after executing code in 'with'
When teardown=False, then __exit__ function does nothing and browser stays open after executing commands
I still use options.add_experimental_option("detach", True) for proper working every time
"""


class Ebay(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = Options()
        options.add_experimental_option("detach", True)  # prevent from closing browser after executing code
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # disable Chrome dev logs and warnings
        super(Ebay, self).__init__(options=options)  # instantiate super class and include options
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):  # __exit__ is used for 'with' in run.py
        if self.teardown:
            self.quit()

    def open_first_page(self):
        self.get(const.EBAY_URL)

    def choose_category(self, category):
        category_filter = self.find_element(By.ID, 'gh-cat')
        category_filter.click()
        cat = self.find_element(By.XPATH, f'//select[@id="gh-cat"]/option[contains(text(), "{category}")]')
        cat.click()

    def type_query(self, query):
        search_box = self.find_element(By.ID, 'gh-ac')
        search_box.send_keys(query)
        search_box.submit()

    def filtration(self):
        filtration = EbayFiltration(driver=self)
        filtration.format('Hardcover', 'Paperback')  # define format, can be more than 2 parameters
        filtration.condition('Brand New', 'Good')   # define condition, can be more than 2 parameters

    def scrap_results(self, amount=10):
        scrap = EbayScrap(driver=self)
        table = PrettyTable(
            field_names=["Book name", "Price", "shipped from"]
        )
        table.add_rows(scrap.results(n=amount))  # define amount of results shown (from top to down)
        print(table)
        return table
