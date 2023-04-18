from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from prettytable import PrettyTable

from utilities.ebay_filtration import EbayFiltration
from utilities.ebay_scrap import EbayScrap


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def filtration(self):
        filtration = EbayFiltration(driver=self.driver)
        filtration.format('Hardcover', 'Paperback')  # define format, can be more than 2 parameters
        filtration.condition('Brand New', 'Good')  # define condition, can be more than 2 parameters

    def scrap_results(self, amount=10):
        scrap = EbayScrap(driver=self.driver)
        table = PrettyTable(
            field_names=["Book name", "Price", "shipped from"]
        )
        table.add_rows(scrap.results(n=amount))  # define amount of results shown (from top to down)
        print(table)
        return table
