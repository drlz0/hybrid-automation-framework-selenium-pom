from base.bot import Bot

bot = Bot()
bot.choose_category('Books')
bot.search_for_product('Python')
bot.filter_search_results()
bot.scrape_results(amount=5)
bot.__exit__(None, None, None)