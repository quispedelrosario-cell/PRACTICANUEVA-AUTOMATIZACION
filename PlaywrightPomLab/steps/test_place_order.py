"""
Step definitions para agregar productos al carrito en Demoblaze.
"""
import pytest
import allure
from pytest_bdd import scenarios, given, when, then, parsers

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

scenarios("../features/place_order.feature")

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.fixture(scope="function")
def product_page(page):
    return ProductPage(page)

@pytest.fixture(scope="function")
def cart_page(page):
    return CartPage(page)

@given("que estoy en la página principal de Demoblaze")
def open_demoblaze_home(home_page: HomePage):
    home_page.open()

@when(parsers.parse('selecciono la categoría "{category_name}"'))
@then(parsers.parse('selecciono la categoría "{category_name}"'))
def select_demoblaze_category(home_page: HomePage, category_name: str):
    home_page.select_category(category_name)

@when(parsers.parse('selecciono el producto "{product_name}"'))
@then(parsers.parse('selecciono el producto "{product_name}"'))
def select_demoblaze_product(home_page: HomePage, product_name: str):
    home_page.select_product(product_name)

@when("agrego el producto al carrito")
@then("agrego el producto al carrito")
def add_demoblaze_product_to_cart(product_page: ProductPage):
    product_page.add_to_cart()

@when(parsers.parse('debe mostrarse la alerta "{expected_alert}"'))
@then(parsers.parse('debe mostrarse la alerta "{expected_alert}"'))
def verify_demoblaze_alert(product_page: ProductPage, expected_alert: str):
    actual_alert = product_page.last_alert_text
    assert expected_alert in actual_alert, (
        f"Expected alert to contain '{expected_alert}', but got '{actual_alert}'"
    )

@given("el carrito tiene productos")
def ensure_cart_has_products(home_page: HomePage, product_page: ProductPage, cart_page: CartPage):
    home_page.open()
    home_page.select_category("Phones")
    home_page.select_product("Iphone 6 32gb")
    product_page.add_to_cart()
    cart_page.open()
    assert cart_page.get_cart_product_names(), "El carrito debe tener al menos un producto después de agregarlo."

@when("vuelvo a la página principal")
@then("vuelvo a la página principal")
def return_to_demoblaze_home(home_page: HomePage):
    home_page.open()

@when(parsers.parse('el producto "{product_name}" debe aparecer en el carrito'))
@then(parsers.parse('el producto "{product_name}" debe aparecer en el carrito'))
def verify_product_in_cart(cart_page: CartPage, product_name: str):
    cart_page.open()
    assert cart_page.is_product_in_cart(product_name), (
        f"Expected product '{product_name}' to be in the cart, but it was not found."
    )

@when(parsers.parse('selecciono el boton "{button_name}"'))
@then(parsers.parse('selecciono el boton "{button_name}"'))
def select_cart_button(cart_page: CartPage, button_name: str):
    if button_name.lower() == "place order":
        cart_page.place_order()
    else:
        raise ValueError(f"Botón '{button_name}' no está soportado.")

@then("se debe abrir el formulario de place order")
def verify_place_order_form_open(cart_page: CartPage):
    cart_page.page.wait_for_selector("input#name", timeout=10000)
    assert cart_page.page.locator("input#name").is_visible(), (
        "El formulario de Place Order no se abrió correctamente."
    )

@when(parsers.re(r'^completo el formulario de place order con los siguientes datos:\n(?P<data_table>[\s\S]+)$'))
@then(parsers.re(r'^completo el formulario de place order con los siguientes datos:\n(?P<data_table>[\s\S]+)$'))
def fill_place_order_form(cart_page: CartPage, data_table: str):
    lines = data_table.strip().split("\n")
    headers = [header.strip() for header in lines[0].split("|") if header.strip()]
    values = [value.strip() for value in lines[1].split("|") if value.strip()]
    data = dict(zip(headers, values))

    cart_page.fill_place_order_form(
        name=data.get("nombre", ""),
        country=data.get("pais", ""),
        city=data.get("ciudad", ""),
        card=data.get("tarjeta", ""),
        month=data.get("mes", ""),
        year=data.get("año", "")
    )

@when(parsers.parse('confirmo seleccionar "{button_name}"'))
@then(parsers.parse('confirmo seleccionar "{button_name}"'))
def confirm_button_click(cart_page: CartPage, button_name: str):
    if button_name.lower() == "purchase":
        cart_page.confirm_purchase()
    else:
        raise ValueError(f"Button '{button_name}' is not recognized for confirmation.")

@then("se debe mostrar el mensaje de confirmación de compra")
def verify_purchase_confirmation(cart_page: CartPage):
    expected_message = "Thank you for your purchase!"
    actual_message = cart_page.get_confirmation_message()
    assert expected_message in actual_message, (
        f"Expected confirmation message to contain '{expected_message}', but got '{actual_message}'"
    )
