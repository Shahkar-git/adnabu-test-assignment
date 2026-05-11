from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    """Search results page — handles product listing."""

    PRODUCT_TITLES    = (By.CSS_SELECTOR, ".product-item__title, .card__heading, h3.h4")
    FIRST_PRODUCT     = (By.CSS_SELECTOR, ".product-item a, .card__heading a, .product-card a")
    NO_RESULTS_MSG    = (By.CSS_SELECTOR, ".search-no-results, .empty-page-content, p.search__no-results")

    def get_all_product_titles(self) -> list:
        """Return list of all product title texts on results page."""
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        return [el.text.strip() for el in elements if el.text.strip()]

    def click_first_product(self):
        """Click on the first product in search results."""
        self.click(self.FIRST_PRODUCT)

    def no_results_shown(self) -> bool:
        """Returns True if no results message is displayed."""
        return self.is_visible(self.NO_RESULTS_MSG)

    def results_count(self) -> int:
        """Return number of products shown in results."""
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        return len(elements)
