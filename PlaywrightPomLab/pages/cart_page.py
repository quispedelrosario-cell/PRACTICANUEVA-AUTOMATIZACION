"""
Page Object para la página del carrito de Demoblaze.
"""

import allure
from .base_page import BasePage


class CartPage(BasePage):
    CART_URL = "https://www.demoblaze.com/cart.html"
    CART_ROWS = "tbody#tbodyid tr"
    CART_ROW_PRODUCT_NAME = "td:nth-child(2)"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        """Abre la página del carrito."""
        with allure.step(f"Navegar a {self.CART_URL}"):
            self.navigate_to(self.CART_URL)
            self.wait_for_selector(self.CART_ROWS, timeout=20000)
            self.take_screenshot("Demoblaze - Carrito")

    def get_cart_product_names(self) -> list[str]:
        """Retorna los nombres de producto actualmente en el carrito."""
        with allure.step("Obtener nombres de productos en el carrito"):
            rows = self.page.locator(self.CART_ROWS)
            if rows.count() == 0:
                allure.attach(
                    "No hay artículos en el carrito.",
                    name="Carrito vacío",
                    attachment_type=allure.attachment_type.TEXT,
                )
                return []

            names = []
            for row in rows.all():
                cell = row.locator(self.CART_ROW_PRODUCT_NAME)
                names.append(cell.inner_text().strip())

            allure.attach(
                "\n".join(names),
                name="Productos en carrito",
                attachment_type=allure.attachment_type.TEXT,
            )
            return names

    def is_product_in_cart(self, product_name: str) -> bool:
        """Verifica si un producto aparece en el carrito."""
        with allure.step(f"Verificar presencia del producto '{product_name}' en el carrito"):
            names = self.get_cart_product_names()
            found = any(product_name.lower() in name.lower() for name in names)
            self.take_screenshot(
                "Producto encontrado en carrito" if found else "Producto no encontrado en carrito"
            )
            return found
        
# Accion de Place order
    def place_order(self):
        """Hace clic en el botón 'Place Order'."""
        with allure.step("Hacer clic en 'Place Order'"):
            self.page.wait_for_selector("button[data-target='#orderModal']", timeout=10000)
            self.page.locator("button[data-target='#orderModal']").click()
            self.take_screenshot("Formulario de Place Order abierto")

    def fill_place_order_form(self, name: str, country: str, city: str, card: str, month: str, year: str):
        """Completa el formulario de Place Order con los datos proporcionados."""
        with allure.step("Completar el formulario de Place Order"):
            self.page.wait_for_selector("input#name", timeout=10000)
            self.page.locator("input#name").fill(name)
            self.page.locator("input#country").fill(country)
            self.page.locator("input#city").fill(city)
            self.page.locator("input#card").fill(card)
            self.page.locator("input#month").fill(month)
            self.page.locator("input#year").fill(year)
            self.take_screenshot("Formulario de Place Order completado")

    def confirm_purchase(self):
        """Hace clic en el botón 'Purchase' para confirmar la compra."""
        with allure.step("Confirmar la compra haciendo clic en 'Purchase'"):
            self.page.wait_for_selector("button[onclick='purchaseOrder()']", timeout=10000)
            self.page.locator("button[onclick='purchaseOrder()']").click()
            self.take_screenshot("Compra confirmada")   

    def get_confirmation_message(self) -> str:
        """Obtiene el mensaje de confirmación después de realizar la compra."""
        with allure.step("Obtener el mensaje de confirmación de compra"):
            self.page.wait_for_selector("div.sweet-alert h2", timeout=10000)
            message = self.page.locator("div.sweet-alert h2").inner_text().strip()
            allure.attach(
                message,
                name="Mensaje de confirmación",
                attachment_type=allure.attachment_type.TEXT,
            )
            return message
