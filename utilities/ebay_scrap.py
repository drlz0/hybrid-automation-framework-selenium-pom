# Separate file for class with instance methods
# That will be responsible for scrapping data of offers

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class EbayScrap:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def results(self, n):
        collection = []
        for x in range(2, n + 2):  # n - how many results to show
            parent_element = self.driver.find_element(
                By.XPATH, f'//*[@id="srp-river-results"]/ul/li[{x}]')  # get parent element with li tag
                                                                       # and iterate over it
            heading = parent_element.find_element(
                By.XPATH, './/span[@role="heading"]')  # find by xpath the lowest element with heading
            head_text = heading.text  # get text from this element, in this situation the span with role="..."

            price = parent_element.find_element(
                By.XPATH, './/span[@class="s-item__price"]')
            price_text = price.text

            shipped_from = parent_element.find_element(
                By.XPATH, './/span[@class="s-item__location s-item__itemLocation"]')
            shipped_from_text = shipped_from.text

            collection.append([head_text, price_text, shipped_from_text])  # append to main list
                                                                           # and then use PrettyTable
        return collection

