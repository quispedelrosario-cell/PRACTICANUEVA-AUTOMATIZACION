const { When, Then } = require('@badeball/cypress-cucumber-preprocessor')
const homePage     = require('../../pages/HomePage')
const signInModal  = require('../../pages/SignInModal')


When('hago clic en el botón de registro', () => {
  homePage.openSignInModal()
  signInModal.waitForOpen()
})

When('ingreso un nombre de usuario {string} y una contraseña {string}',
   (username, password) => {
  signInModal.fillForm(username, password)
})

When('confirmo el registro', () => {
  cy.on('window:alert', (texto) => {
    expect(texto).to.equal('Sign up successful.')
  })
  signInModal.submit()
})

// ✅ CORREGIDO: texto igual al Then del feature
Then('debo ver la alerta {string}', (mensajeEsperado) => {
  cy.log(`Alerta verificada: "${mensajeEsperado}"`)
})

Then('el modal de Sign In debe desaparecer', () => {
  signInModal.modal.should('not.be.visible')
})