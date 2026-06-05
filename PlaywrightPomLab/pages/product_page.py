"""
Page Object para la página de detalle de producto en Demoblaze.
"""
import allure
from .base_page import BasePage


class ProductPage(BasePage):
    """
    Representa la página de detalle de un producto en Demoblaze.
    URL base: https://www.demoblaze.com
    """

    # ── Selectores ──────────────────────────────────────────────────────────
    PRODUCT_TITLE = "h2#tbodyld"
    PRODUCT_PRICE = "h3"
    ADD_TO_CART_BUTTON = "a:has-text('Add to cart')"
    CART_COUNT = "span.badge"

    def __init__(self, page):
        super().__init__(page)
        self.last_alert_text = None

    # ── Acciones ─────────────────────────────────────────────────────────────

    def get_product_title(self) -> str:
        """Retorna el título del producto visible en la página."""
        with allure.step("Obtener el título del producto"):
            self.wait_for_selector(self.PRODUCT_TITLE)
            title = self.page.locator(self.PRODUCT_TITLE).first.inner_text().strip()
            allure.attach(
                title,
                name="Título obtenido",
                attachment_type=allure.attachment_type.TEXT,
            )
            return title

    def get_product_price(self) -> str:
        """Retorna el precio del producto visible en la página."""
        with allure.step("Obtener el precio del producto"):
            price_locators = self.page.locator(self.PRODUCT_PRICE)
            # El precio está en el primer h3 que contiene un número
            for i in range(price_locators.count()):
                text = price_locators.nth(i).inner_text().strip()
                if text and text[0].isdigit():
                    allure.attach(
                        text,
                        name="Precio obtenido",
                        attachment_type=allure.attachment_type.TEXT,
                    )
                    return text
            return ""

    def add_to_cart(self):
        """Hace clic en el botón 'Add to cart' y captura la alerta."""
        with allure.step("Hacer clic en 'Add to cart'"):
            # Configurar listener para capturar alertas JavaScript
            def handle_dialog(dialog):
                self.last_alert_text = dialog.message
                dialog.accept()
            
            # Configurar el listener ANTES de interactuar con la página
            self.page.on("dialog", handle_dialog)
            
            # Esperar a que el botón sea visible
            self.page.locator(self.ADD_TO_CART_BUTTON).first.wait_for(state="visible", timeout=20000)
            self.take_screenshot("Antes de agregar al carrito")
            self.page.locator(self.ADD_TO_CART_BUTTON).first.click()
            
            # Esperar a que se capture la alerta
            self.page.wait_for_timeout(2000)
            self.take_screenshot("Después de agregar al carrito")

    def get_cart_count(self) -> int:
        """Retorna la cantidad de artículos en el carrito."""
        try:
            count_text = self.page.locator(self.CART_COUNT).first.inner_text().strip()
            return int(count_text) if count_text.isdigit() else 0
        except Exception:
            return 0
