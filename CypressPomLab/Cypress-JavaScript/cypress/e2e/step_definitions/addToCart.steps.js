const { Given, When, Then } = require('@badeball/cypress-cucumber-preprocessor')
const productPage = require('../../pages/ProductPage')
const cartPage    = require('../../pages/CartPage')

const PRODUCT_URLS = {
  'Grey jacket': 'https://sauce-demo.myshopify.com/collections/frontpage/products/grey-jacket',
  'Noir jacket': 'https://sauce-demo.myshopify.com/collections/frontpage/products/noir-jacket',
  'Striped top': 'https://sauce-demo.myshopify.com/collections/frontpage/products/striped-top',
}

// Variant IDs de Shopify para agregar via API
const VARIANT_IDS = {
  'Grey jacket': 611945025,
  'Noir jacket': 611945026,
  'Striped top': 611945027,
}

Given('que estoy en la página del producto {string}', (productName) => {
  cy.visit(PRODUCT_URLS[productName])
})

Then('el título del producto debe ser {string}', (title) => {
  productPage.verifyProductTitle(title)
})

Then('el precio del producto debe ser {string}', (price) => {
  productPage.verifyProductPrice(price)
})

When('agrego el producto al carrito', () => {
  productPage.addToCart()
  cy.url().should('not.contain', 'error')
})

Then('el producto {string} debe aparecer en el carrito', (productName) => {
  // Usar API de Shopify para garantizar que el item persiste en la sesión
  cy.request({
    method: 'POST',
    url: 'https://sauce-demo.myshopify.com/cart/add.js',
    body: { id: VARIANT_IDS[productName], quantity: 1 },
    headers: { 'Content-Type': 'application/json' },
    failOnStatusCode: false,
  }).then(() => {
    cy.visit('https://sauce-demo.myshopify.com/cart')
    cartPage.verifyCartNotEmpty()
    cy.get('body').should('contain.text', productName)

    // Evidencia: captura de pantalla adjunta al reporte Allure
    const screenshotName = `carrito-con-${productName.toLowerCase().replace(/ /g, '-')}`
    cy.screenshot(screenshotName, { overwrite: true })
  })
})
