from base.bot import Bot


with Bot(teardown=True) as bot:
    bot.open_home_page()
    bot.search_for_product(query='fantasy book')
    bot.filter_search_results()  # Defining specific filters in filtration() function in ebay_main.py
    bot.scrape_results(amount=10)  # Define specific amount of displayed results
                                   # in scrap_results() function in ebay_main.py

