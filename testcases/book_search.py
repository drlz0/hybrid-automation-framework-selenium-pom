# This is test case for ebay search and filter

def test_ebay_search_results(ebay):
    ebay.open_first_page()
    ebay.choose_category('Books')
    ebay.type_query('Python')
    ebay.filtration()
    results_table = ebay.scrap_results(amount=5)

    assert len(results_table._rows) == 5

    for row in results_table._rows:
        assert 'python' in row[0].lower()
        assert '$' in row[1]
        assert row[2] != ''
