const { Given } = require('@badeball/cypress-cucumber-preprocessor')
const homePage = require('../../pages/HomePage')

Given('que estoy en la pagina principal de Demoblaze', () => {
  homePage.visit()
})