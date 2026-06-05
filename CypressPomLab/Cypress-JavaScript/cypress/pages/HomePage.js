/**
 * Page Object: Home Page
 * URL: https://www.demoblaze.com/index.html
 */
class HomePage {
 //Nuevo: Registro
 get signInButton() {
    return cy.get('#signin2')
  }

  //Nuevo Mensaje
  get contactLink() {
    return cy.get('a.nav-link').contains('Contact')
  }
  // Selectores
  get productCards() {
    return cy.get('.product-card, .grid-item, .product')
  }

  get cartLink() {
    return cy.get('a[href="/cart"]')
  }

  // Acciones
  visit() {
    cy.visit('https://www.demoblaze.com/index.html')
  }
 // VISITAR 
  openSignInModal() {
    this.signInButton.click()
  }
  openMessageModal() {
    this.contactLink.click()
  }
  
  clickProduct(productName) {
    cy.contains(productName).click()
  }
}

module.exports = new HomePage()
