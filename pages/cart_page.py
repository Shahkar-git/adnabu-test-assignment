from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Cart page — verifies item was added successfully."""

    CART_ITEMS      = (By.CSS_SELECTOR, ".cart__item, .cart-item, tr.cart__row")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, ".cart__item-name, .cart-item__name, "
                                         ".cart__product-title, a.cart__item-name")
    EMPTY_CART_MSG  = (By.CSS_SELECTOR, ".cart--empty, .empty-page-content, p.cart__empty-text")

    CART_URL = "https://adnabu-store-assignment1.myshopify.com/cart"

    def open(self):
        self.driver.get(self.CART_URL)

    def get_cart_item_names(self) -> list:
        elements = self.driver.find_elements(*self.CART_ITEM_TITLE)
        return [el.text.strip() for el in elements if el.text.strip()]

    def is_cart_empty(self) -> bool:
        return self.is_visible(self.EMPTY_CART_MSG)

    def get_item_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEMS))
