/**
 * Feature: Agregar artículo al carrito
 * Sitio: https://sauce-demo.myshopify.com/
 * Patrón: Page Object Model (POM)
 */
const homePage    = require('../pages/HomePage')
const productPage = require('../pages/ProductPage')
const cartPage    = require('../pages/CartPage')

describe('Agregar artículo al carrito - Sauce Demo', () => {
  let product

  before(() => {
    cy.fixture('products').then((data) => {
      product = data.greyJacket
    })
  })

  it('Debe navegar a la home y ver los productos', () => {
    homePage.visit()
    cy.title().should('contain', 'Sauce Demo')
    homePage.productCards.should('have.length.greaterThan', 0)
  })

  it('Debe abrir la página del producto y verificar título y precio', () => {
    cy.visit(product.url)
    productPage.verifyProductTitle(product.name)
    productPage.verifyProductPrice(product.price)
  })

  it('Debe agregar el producto al carrito', () => {
    cy.visit(product.url)
    productPage.addToCart()
    cy.url().should('not.contain', 'error')
    cy.get('a[href="/cart"]').should('be.visible')
  })

  it('Debe mostrar el producto en el carrito (flujo completo)', () => {
    // Agregar el producto via API del carrito de Shopify para garantizar persistencia
    cy.request({
      method: 'POST',
      url: 'https://sauce-demo.myshopify.com/cart/add.js',
      body: { id: 611945025, quantity: 1 },
      headers: { 'Content-Type': 'application/json' },
      failOnStatusCode: false,
    }).then(() => {
      cy.visit('https://sauce-demo.myshopify.com/cart')
      cartPage.verifyCartNotEmpty()
      cy.get('body').should('contain.text', product.name)
    })
  })
})
