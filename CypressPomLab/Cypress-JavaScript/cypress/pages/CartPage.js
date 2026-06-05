/**
 * Page Object: Cart Page
 * URL: https://sauce-demo.myshopify.com/cart
 */
class CartPage {
  // Selectores
  get cartTitle() {
    return cy.get('h1, .cart-title')
  }

  get cartItems() {
    // Shopify theme: filas de la tabla del carrito o contenedor genérico
    return cy.get('table tr, .cart-item, .cart__row, form[action="/cart"] tr')
  }

  get checkoutButton() {
    return cy.get('input[name="checkout"], button[name="checkout"]')
  }

  // Acciones
  visit() {
    cy.visit('https://sauce-demo.myshopify.com/cart')
  }

  verifyItemInCart(productName) {
    // Verificar que el nombre del producto aparece en algún lugar de la página del carrito
    cy.contains(productName).should('be.visible')
  }

  verifyCartNotEmpty() {
    // El carrito no está vacío si no aparece el mensaje de carrito vacío
    cy.get('body').should('not.contain.text', 'cart is currently empty')
  }
}

module.exports = new CartPage()
