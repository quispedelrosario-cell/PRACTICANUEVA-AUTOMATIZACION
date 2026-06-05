"""
Step definitions para agregar productos al carrito en Demoblaze.
"""
import pytest
import allure
from pytest_bdd import scenarios, given, when, then, parsers

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage


scenarios("../features/add_product.feature")


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
def select_demoblaze_category(home_page: HomePage, category_name: str):
    home_page.select_category(category_name)


@when(parsers.parse('selecciono el producto "{product_name}"'))
def select_demoblaze_product(home_page: HomePage, product_name: str):
    home_page.select_product(product_name)


@when("agrego el producto al carrito")
def add_demoblaze_product_to_cart(product_page: ProductPage):
    product_page.add_to_cart()


@when("vuelvo a la página principal")
def return_to_demoblaze_home(home_page: HomePage):
    home_page.open()


@when(parsers.parse('debe mostrarse la alerta "{expected_alert}" para el producto "{product_name}"'))
@then(parsers.parse('debe mostrarse la alerta "{expected_alert}" para el producto "{product_name}"'))
def verify_demoblaze_alert_for_product(
    product_page: ProductPage,
    expected_alert: str,
    product_name: str,
):
    actual_alert = product_page.last_alert_text
    allure.attach(
        f"Producto: {product_name}\nEsperado: {expected_alert}\nObtenido: {actual_alert}",
        name="Verificación de alerta de producto",
        attachment_type=allure.attachment_type.TEXT,
    )
    assert actual_alert == expected_alert, (
        f"Texto de alerta esperado '{expected_alert}' para '{product_name}', pero se obtuvo '{actual_alert}'"
    )


@then(parsers.parse('ambos productos "{first_product}" y "{second_product}" deben aparecer en el carrito'))
def verify_two_products_in_demoblaze_cart(
    cart_page: CartPage,
    first_product: str,
    second_product: str,
):
    cart_page.open()
    missing_products = []
    for product_name in (first_product, second_product):
        if not cart_page.is_product_in_cart(product_name):
            missing_products.append(product_name)

    assert not missing_products, (
        f"Los productos {missing_products} no se encontraron en el carrito."
    )


@then(parsers.parse('debe mostrarse la alerta "{expected_alert}"'))
def verify_demoblaze_alert(product_page: ProductPage, expected_alert: str):
    actual_alert = product_page.last_alert_text
    allure.attach(
        f"Esperado: {expected_alert}\nObtenido: {actual_alert}",
        name="Verificación de alerta",
        attachment_type=allure.attachment_type.TEXT,
    )
    assert actual_alert == expected_alert, (
        f"Texto de alerta esperado '{expected_alert}', pero se obtuvo '{actual_alert}'"
    )


@then(parsers.parse('el producto "{product_name}" debe aparecer en el carrito'))
def verify_product_in_demoblaze_cart(cart_page: CartPage, product_name: str):
    cart_page.open()
    assert cart_page.is_product_in_cart(product_name), (
        f"El producto '{product_name}' no se encontró en el carrito."
    )
