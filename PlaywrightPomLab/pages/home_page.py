"""
Page Object para la página principal de Demoblaze.
"""

import allure
from .base_page import BasePage


class HomePage(BasePage):
    HOME_URL = "https://www.demoblaze.com/index.html"
    CATEGORY_LINK = "a#itemc"

    def open(self):
        """Navega a la página principal de Demoblaze."""
        with allure.step(f"Navegar a {self.HOME_URL}"):
            self.navigate_to(self.HOME_URL)
            self.wait_for_selector(self.CATEGORY_LINK, timeout=20000)
            self.take_screenshot("Demoblaze - Inicio")

    def select_category(self, category_name: str):
        """Selecciona una categoría por su nombre visible."""
        with allure.step(f"Seleccionar categoría '{category_name}'"):
            locator = self.page.locator(self.CATEGORY_LINK, has_text=category_name).first
            locator.wait_for(state="visible", timeout=10000)
            locator.click()
            self.page.wait_for_timeout(1000)
            self.take_screenshot(f"Categoría {category_name} seleccionada")

    def select_product(self, product_name: str):
        """Selecciona un producto por su nombre visible."""
        with allure.step(f"Seleccionar producto '{product_name}'"):
            locator = self.page.locator("a", has_text=product_name).first
            locator.wait_for(state="visible", timeout=10000)
            locator.click()
            self.page.wait_for_selector("a:has-text('Add to cart')", timeout=20000)
            self.take_screenshot(f"Página del producto {product_name}")
