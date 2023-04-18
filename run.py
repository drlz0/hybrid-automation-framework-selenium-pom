from pages.ebay_actions import Ebay


with Ebay(teardown=True) as bot:
    bot.open_first_page()
    bot.choose_category(category='Books')
    bot.type_query(query='fantasy book')
    bot.filtration()  # Defining specific filters in filtration() function in ebay_main.py
    bot.scrap_results(amount=10)  # Define specific amount of displayed results
                                  # in scrap_results() function in ebay_main.py

