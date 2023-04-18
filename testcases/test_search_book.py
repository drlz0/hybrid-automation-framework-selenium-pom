from base.bot import Bot


def test_ebay():
    with Bot() as bot:
        bot.open_home_page()
        bot.choose_category('Books')
        bot.search_for_product('fantasy book')
        bot.filter_search_results()
        bot.scrape_results(amount=5)