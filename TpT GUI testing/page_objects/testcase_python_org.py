__author__ = 'Roysten'


from selenium import webdriver
import pytest
import page

class search_keyword():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_text_search (self):
        main_page = page.Main_page(self.driver)
        assert main_page.is_title_matches(), "Tilte doesn't matches"
        main_page.search_text = "pycon"
        main_page.go_back()
        search_results = page.search_results_page(self.driver)
        assert search_results.is_search_text_found(), "Search text not found"

    def tear_down(self):
        self.driver.close()
if __name__ == "__main__":
    pytest.main()


