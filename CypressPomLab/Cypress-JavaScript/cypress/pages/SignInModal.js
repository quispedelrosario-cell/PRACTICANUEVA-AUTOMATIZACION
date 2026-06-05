 /**
 * Page Object: Sign in Page
 * URL: https://www.demoblaze.com/index.html
 */

 class SignInModal {
   // Selectores
   get signInModal() {
     return cy.get('#signInModal')
   }

   get usernameInput() {
     return cy.get('#sign-username')
   }
    get passwordInput() {  
        return cy.get('#sign-password')
    }

   get signUpButton() {
    return cy.get('#signInModal').contains('button', 'Sign up')
  }

  get closeButton() {
    return cy.get('#signInModal').find('button.btn-secondary')
  }
   
    // Acciones
    waitForOpen() {
        this.signInModal.should('be.visible')
    } 
    fillForm(username, password) {
        this.usernameInput.type(username)
        this.passwordInput.type(password)
    } 
    submit() {
        this.signUpButton.click()
    }
    close() {
        this.closeButton.click()
    } 
  }
  module.exports = new SignInModal()