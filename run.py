from pages.home_page import HomePage
from pages.search_page import SearchPage
from utilities.constants import SEARCH_QUERY

# Create a Bot instance
with Bot() as bot:
    # Search for a product
    search_page = bot.search_for_product(SEARCH_QUERY)
    # Filter the search results
    search_page.filtration()
    # Scrape the results
    results_table = search_page.scrap_results()
    # Print the results
    print(results_table)