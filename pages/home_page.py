from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.constants as const


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(const.EBAY_URL)

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
