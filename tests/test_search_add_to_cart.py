"""
Test: Search for a product and add it to cart — AdNabu Test Store
Author: Mohammad Shahkar Alam
Tool: Python + Selenium + Pytest
"""

import pytest
from pages.password_page import PasswordPage
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

SEARCH_PRODUCT = "T-Shirt"  # Change to any product available in the store


class TestSearchAndAddToCart:
    """
    Automates: Search for a product → click first result → Add to Cart → verify in cart
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Enter the password-protected store before each test."""
        self.driver = driver
        password_page = PasswordPage(driver)
        password_page.enter_store()

    def test_search_and_add_to_cart(self):
        """
        Scenario: Search for a product and add it to the cart successfully.
        Steps:
            1. Open the store and enter password
            2. Search for a product
            3. Click the first result
            4. Click Add to Cart
            5. Navigate to cart and verify product is present
        """
        # Step 1: Search for product
        home = HomePage(self.driver)
        home.search_for(SEARCH_PRODUCT)

        # Step 2: Verify results page and click first product
        results = SearchResultsPage(self.driver)
        assert results.results_count() > 0, \
            f"No results found for '{SEARCH_PRODUCT}' — check product name"

        titles = results.get_all_product_titles()
        print(f"\n✅ Found {len(titles)} results for '{SEARCH_PRODUCT}'")
        print(f"   First product: {titles[0] if titles else 'N/A'}")

        results.click_first_product()

        # Step 3: Get product name and add to cart
        product = ProductPage(self.driver)
        product_name = product.get_product_title()
        print(f"   Product page opened: {product_name}")

        product.click_add_to_cart()
        print(f"   Clicked Add to Cart")

        # Step 4: Navigate to cart and verify
        cart = CartPage(self.driver)
        cart.open()

        assert not cart.is_cart_empty(), "Cart is empty — Add to Cart may have failed"

        cart_items = cart.get_cart_item_names()
        print(f"   Cart items: {cart_items}")

        assert cart.get_item_count() > 0, "No items found in cart"
        print(f"✅ Test PASSED — Product successfully added to cart!")
