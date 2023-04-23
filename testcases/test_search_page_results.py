import pytest
from ddt import ddt, data, file_data, unpack

from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchPageResults:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)

    @pytest.mark.parametrize("test_category,test_query,test_amount", [
        ("Books", "fantasy book", 10)])
    #@file_data("../testdata/test_data_json.json")
    def test_search_page_results(self, test_category, test_query, test_amount):
        self.hp = HomePage(self.driver)
        search_click_result = self.hp.input_cat_and_query(cat=test_category, this_query=test_query)

        search_click_result.filtration()
        search_click_result.scrap_results(amount=test_amount)
