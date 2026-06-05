/**
 * Page Object: Product Detail Page
 * URL: https://sauce-demo.myshopify.com/collections/frontpage/products/:product
 */
class ProductPage {
  // Selectores
  get productTitle() {
    return cy.get('h1.product-title, h1')
  }

  get productPrice() {
    return cy.get('.product-price, .price')
  }

  get addToCartButton() {
    return cy.get('button[type="submit"], input[type="submit"][value*="ADD"], button').contains(/add to cart/i)
  }

  get cartCount() {
    return cy.get('a[href="/cart"]')
  }

  // Acciones
  addToCart() {
    cy.get('form[action="/cart/add"] button[type="submit"], form[action*="cart"] input[type="submit"]')
      .first()
      .click()
  }

  verifyProductTitle(title) {
    this.productTitle.should('contain.text', title)
  }

  verifyProductPrice(price) {
    this.productPrice.should('contain.text', price)
  }
}

module.exports = new ProductPage()
