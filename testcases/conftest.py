import pytest
from pages.ebay_actions import Ebay


@pytest.fixture(scope='module')
def ebay():
    ebay = Ebay()
    yield ebay
    ebay.quit()
