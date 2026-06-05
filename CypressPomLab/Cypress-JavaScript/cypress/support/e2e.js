// ***********************************************************
// This example support/e2e.js is processed and
// loaded automatically before your test files.
//
// This is a great place to put global configuration and
// behavior that modifies Cypress.
//
// You can change the location of this file or turn off
// automatically serving support files with the
// 'supportFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

// Import commands.js using ES2015 syntax:
import './commands'
import 'allure-cypress'

// Ignorar excepciones no capturadas del código de la aplicación
// El sitio sauce-demo.myshopify.com tiene un bug en jquery.theme.js
// que se dispara al agregar al carrito
Cypress.on('uncaught:exception', () => false)