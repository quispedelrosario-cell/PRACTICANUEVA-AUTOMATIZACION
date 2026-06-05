 /**
 * Page Object: Sign in Page
 * URL: https://www.demoblaze.com/index.html
 */

 class messageModal {
   // Selectores
   
   get messageModal() {
     return cy.get('#exampleModal')
   }
    get emailInput() {
        return cy.get('#recipient-email')
    }
    get nameInput() {
        return cy.get('#recipient-name')
    }   
    get messageInput() {
        return cy.get('#message-text')
    }

   get sendButton() {
    return cy.get('#exampleModal .btn-primary').contains('Send message')
  }

    // Acciones
    waitForOpen() {
        this.messageModal.should('be.visible')
    }
    fillForm(name, email, message) {
        this.nameInput.type(name)
        this.emailInput.type(email)
        this.messageInput.type(message)
    }   
    submit() {
        this.sendButton.click()
    }
    
    }
    module.exports = new messageModal()