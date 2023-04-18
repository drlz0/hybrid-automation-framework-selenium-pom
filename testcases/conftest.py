import pytest
from base.bot import Bot


@pytest.fixture(scope='module')
def ebay():
    ebay = Bot()
    yield ebay
