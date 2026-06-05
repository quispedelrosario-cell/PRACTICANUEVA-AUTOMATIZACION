"""
Page Object para la tienda Demoblaze.
"""
import allure
from .base_page import BasePage


class DemoblazePage(BasePage):
    BASE_URL = "https://www.demoblaze.com"
    HOME_URL = f"{BASE_URL}/index.html"
    CART_URL = f"{BASE_URL}/cart.html"
    CATEGORY_LINK = "a#itemc"
    PRODUCT_LINK = "a[href*='prod.html?idp_=']"
    ADD_TO_CART_BUTTON = "a:has-text('Add to cart')"
    CART_ROWS = "tbody#tbodyid tr"
    CART_ROW_PRODUCT_NAME = "td:nth-child(2)"

    def __init__(self, page):
        super().__init__(page)
        self.last_alert_text = ""

    def open(self):
        """Navega a la página de inicio de Demoblaze."""
        with allure.step(f"Navegar a {self.HOME_URL}"):
            self.navigate_to(self.HOME_URL)
            self.page.wait_for_selector(self.CATEGORY_LINK, timeout=20000)
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
            self.page.wait_for_selector(self.ADD_TO_CART_BUTTON, timeout=20000)
            self.take_screenshot(f"Página del producto {product_name}")

    def add_to_cart(self):
        """Hace clic en Add to cart y guarda el texto de la alerta."""
        with allure.step("Agregar producto al carrito y aceptar la alerta"):
            self.page.wait_for_selector(self.ADD_TO_CART_BUTTON, timeout=10000)
            with self.page.expect_event("dialog") as dialog_info:
                self.page.locator(self.ADD_TO_CART_BUTTON).click()
            dialog = dialog_info.value
            self.last_alert_text = dialog.message
            dialog.accept()
            allure.attach(
                self.last_alert_text,
                name="Alerta Add to cart",
                attachment_type=allure.attachment_type.TEXT,
            )
            self.take_screenshot("Producto agregado al carrito")
            return self.last_alert_text

    def open_cart(self):
        """Abre la página del carrito."""
        with allure.step(f"Navegar a {self.CART_URL}"):
            self.navigate_to(self.CART_URL)
            self.page.wait_for_selector(self.CART_ROWS, timeout=20000)
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
