const{ When, Then } = require('@badeball/cypress-cucumber-preprocessor')
const homePage     = require('../../pages/HomePage')
const messageModal  = require('../../pages/MessageModal')




When ('hago clic en el enlace "Contact"', () => {
  homePage.contactLink.click()
  messageModal.waitForOpen()
})

When('completo el formulario con un email válido, un nombre y un mensaje', () => {
  messageModal.fillForm('Juan', 'juan@test.com', 'Hola necesito ayuda')
})

When('envio el mensaje al hacer clic en el botón "Send message"', () => {
  cy.on('window:alert', (texto) => {
    expect(texto).to.equal('Thanks for the message!!')
  })
  messageModal.submit()
})

Then('debo ver una alerta con el mensaje "Thanks for the message!!"', () => {
  cy.log('Alerta verificada')
})
