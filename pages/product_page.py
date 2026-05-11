from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    """Product detail page — handles Add to Cart."""

    PRODUCT_TITLE   = (By.CSS_SELECTOR, "h1.product__title, h1.product-single__title, h1")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[name='add'], button[id='AddToCart'], "
                                         "button[class*='add-to-cart'], input[name='add']")
    CART_COUNT      = (By.CSS_SELECTOR, ".cart-count, .cart__count, span[class*='cart-count']")
    SUCCESS_MSG     = (By.CSS_SELECTOR, ".cart-notification, .ajaxcart__notify, "
                                         "[class*='cart-notification'], [class*='added']")
    CART_ICON       = (By.CSS_SELECTOR, "a[href='/cart'], .cart-link")

    def get_product_title(self) -> str:
        return self.get_text(self.PRODUCT_TITLE)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def is_cart_updated(self) -> bool:
        """Returns True if cart notification or count update is visible."""
        return (self.is_visible(self.SUCCESS_MSG) or
                self.is_visible(self.CART_COUNT))

    def go_to_cart(self):
        self.click(self.CART_ICON)
