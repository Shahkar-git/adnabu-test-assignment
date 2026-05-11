from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class HomePage(BasePage):
    """Home page — handles search functionality."""

    SEARCH_ICON    = (By.CSS_SELECTOR, "a[href='/search'], button[aria-label='Search']")
    SEARCH_INPUT   = (By.CSS_SELECTOR, "input[type='search'], input[name='q']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".product-item, .grid__item, .product-card")

    def search_for(self, product_name: str):
        """Click search icon, type product name and submit."""
        self.click(self.SEARCH_ICON)
        self.type(self.SEARCH_INPUT, product_name)
        self.find(self.SEARCH_INPUT).send_keys(Keys.RETURN)

    def get_search_input(self):
        return self.find(self.SEARCH_INPUT)
