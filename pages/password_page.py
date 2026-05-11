from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PasswordPage(BasePage):
    """Handles the Shopify store password entry page."""

    PASSWORD_INPUT = (By.ID, "password")
    ENTER_BUTTON   = (By.CSS_SELECTOR, "button[type='submit']")

    STORE_URL  = "https://adnabu-store-assignment1.myshopify.com"
    PASSWORD   = "AdNabuQA"

    def open(self):
        self.driver.get(self.STORE_URL)

    def enter_store(self):
        """Open store and enter password if password page is shown."""
        self.open()
        if "password" in self.driver.current_url:
            self.type(self.PASSWORD_INPUT, self.PASSWORD)
            self.click(self.ENTER_BUTTON)
