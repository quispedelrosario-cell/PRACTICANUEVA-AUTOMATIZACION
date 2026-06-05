# Guía: Cómo crear un nuevo caso de prueba

Esta guía explica paso a paso cómo agregar un nuevo caso de prueba al proyecto, tanto en **JavaScript** como en **TypeScript**, usando el patrón **POM + BDD**.

El ejemplo que seguiremos es: **verificar que el título de la página del carrito es "My Cart"**.

---

## Estructura de archivos que vas a tocar

```
cypress/
 ├── e2e/
 │    ├── addToCart.feature          ← 1. Agrega el Scenario aquí
 │    └── step_definitions/
 │         └── addToCart.steps.js/ts ← 2. Implementa los steps aquí
 └── pages/
      └── CartPage.js/ts             ← 3. Agrega métodos al Page Object si hacen falta
```

---

## Paso 1 — Escribe el Scenario en el `.feature`

Abre `cypress/e2e/addToCart.feature` y agrega el nuevo scenario al final:

```gherkin
  Scenario: Verificar el título de la página del carrito
    When visito la página del carrito
    Then el título de la página debe ser "My Cart"
```

El archivo completo queda así:

```gherkin
Feature: Agregar artículo al carrito
  Como cliente de Sauce Demo
  Quiero agregar un artículo al carrito
  Para poder comprarlo

  Background:
    Given que estoy en la página del producto "Grey jacket"

  Scenario: Verificar título y precio del producto
    Then el título del producto debe ser "Grey jacket"
    And el precio del producto debe ser "£55.00"

  Scenario: Agregar un artículo al carrito y verificarlo
    When agrego el producto al carrito
    Then el producto "Grey jacket" debe aparecer en el carrito

  Scenario: Verificar el título de la página del carrito
    When visito la página del carrito
    Then el título de la página debe ser "My Cart"
```

> **Nota:** El `Background` se ejecuta antes de cada Scenario. Si tu nuevo caso no necesita estar en la página del producto, puedes moverlo a un `.feature` separado.

---

## Paso 2 — Implementa los steps

Abre el archivo de step definitions y agrega los nuevos steps al final.

### JavaScript → `cypress/e2e/step_definitions/addToCart.steps.js`

```javascript
When('visito la página del carrito', () => {
  cy.visit('https://sauce-demo.myshopify.com/cart')
})

Then('el título de la página debe ser {string}', (titulo) => {
  cy.get('h1').should('contain.text', titulo)
  // Evidencia: captura de pantalla al final del step
  cy.screenshot(`titulo-pagina-${titulo.toLowerCase().replace(/ /g, '-')}`, { overwrite: true })
})
```

### TypeScript → `cypress/e2e/step_definitions/addToCart.steps.ts`

```typescript
When('visito la página del carrito', () => {
  cy.visit('https://sauce-demo.myshopify.com/cart')
})

Then('el título de la página debe ser {string}', (titulo: string) => {
  cy.get('h1').should('contain.text', titulo)
  // Evidencia: captura de pantalla al final del step
  cy.screenshot(`titulo-pagina-${titulo.toLowerCase().replace(/ /g, '-')}`, { overwrite: true })
})
```

> **Regla importante:** cada frase del `.feature` debe tener exactamente un step que la implemente. Si la frase ya existe en otro step, no la dupliques — reutilízala.

---

## Paso 3 — Agrega métodos al Page Object (si hace falta)

Si la acción o verificación es compleja o se va a reutilizar en varios tests, agrégala al Page Object correspondiente en lugar de escribirla directamente en el step.

### JavaScript → `cypress/pages/CartPage.js`

```javascript
verifyCartTitle(title) {
  cy.get('h1').should('contain.text', title)
}
```

### TypeScript → `cypress/pages/CartPage.ts`

```typescript
verifyCartTitle(title: string): void {
  cy.get('h1').should('contain.text', title)
}
```

Y en el step definition lo usas así:

```javascript
// JS
Then('el título de la página debe ser {string}', (titulo) => {
  cartPage.verifyCartTitle(titulo)
  cy.screenshot(`titulo-pagina-${titulo.toLowerCase().replace(/ /g, '-')}`, { overwrite: true })
})
```

```typescript
// TS
Then('el título de la página debe ser {string}', (titulo: string) => {
  cartPage.verifyCartTitle(titulo)
  cy.screenshot(`titulo-pagina-${titulo.toLowerCase().replace(/ /g, '-')}`, { overwrite: true })
})
```

---

## Paso 4 — Ejecuta y verifica el nuevo scenario

### Opción A — Modo interactivo (ver la ejecución en Chrome)

```bash
npm run cy:open
```

Al abrirse la UI de Cypress:
1. Selecciona **E2E Testing**
2. Elige **Chrome** como navegador
3. Haz clic en `addToCart.feature`
4. Se abre Chrome y puedes ver cada step ejecutándose en tiempo real

### Opción B — Modo headed desde terminal (navegador visible sin UI)

```bash
npx cypress run --spec "cypress/e2e/addToCart.feature" --headed --browser chrome
```

Útil para ver la ejecución completa desde la terminal sin abrir la UI de Cypress.

### Opción C — Modo headless (solo terminal, sin navegador)

```bash
npx cypress run --spec "cypress/e2e/addToCart.feature"
```

Más rápido, ideal para CI/CD o cuando no necesitas ver el navegador.

### Comparativa de modos

| Modo        | Comando                                      | Navegador visible | UI Cypress |
|-------------|----------------------------------------------|-------------------|------------|
| Interactivo | `npm run cy:open`                            | ✅ Sí             | ✅ Sí      |
| Headed      | `npx cypress run --headed --browser chrome`  | ✅ Sí             | ❌ No      |
| Headless    | `npm run cy:run`                             | ❌ No             | ❌ No      |

---

## Paso 5 — Ejecuta todos los tests y genera el reporte

```bash
npm run allure:report
```

Esto ejecuta todos los tests, genera el reporte HTML y lo abre en el navegador. El screenshot tomado en el último step aparece como attachment en el scenario correspondiente.

---

## Resumen del flujo completo

```
1. .feature     → escribe el Scenario en Gherkin
       ↓
2. steps.js/ts  → implementa cada Given / When / Then
       ↓
3. pages/*.js/ts → agrega métodos al Page Object si se reutilizan
       ↓
4. cy:run        → ejecuta y genera allure-results/
       ↓
5. allure:report → genera y abre el reporte con evidencia
```

---

## Referencia rápida de keywords Gherkin

| Keyword    | Uso                                              |
|------------|--------------------------------------------------|
| `Feature`  | Nombre del feature (una vez por archivo)         |
| `Scenario` | Un caso de prueba                                |
| `Background` | Pasos que se ejecutan antes de cada Scenario   |
| `Given`    | Precondición / estado inicial                    |
| `When`     | Acción que ejecuta el usuario                    |
| `Then`     | Verificación del resultado esperado              |
| `And`      | Continúa el paso anterior (Given/When/Then)      |
| `But`      | Excepción o caso negativo                        |

---

## Referencia rápida de comandos Cypress útiles

```javascript
cy.visit(url)                          // navegar a una URL
cy.get(selector)                       // obtener un elemento
cy.contains(texto)                     // buscar por texto
cy.get(selector).click()               // hacer clic
cy.get(selector).type('texto')         // escribir en un input
cy.get(selector).should('be.visible')  // verificar visibilidad
cy.get(selector).should('contain.text', 'texto')  // verificar texto
cy.url().should('include', '/cart')    // verificar URL
cy.screenshot('nombre')               // tomar evidencia
cy.request({ method, url, body })      // llamada HTTP directa
```

---

## Diferencias JS vs TS en los archivos

| Aspecto           | JavaScript                          | TypeScript                              |
|-------------------|-------------------------------------|-----------------------------------------|
| Extensión test    | `.cy.js`                            | `.cy.ts`                                |
| Extensión steps   | `.steps.js`                         | `.steps.ts`                             |
| Extensión pages   | `.js`                               | `.ts`                                   |
| Import steps      | `require(...)`                      | `import { ... } from '...'`             |
| Import pages      | `require(...)`                      | `import ... from '...'`                 |
| Tipos             | No aplica                           | `: string`, `: void`, `Cypress.Chainable` |
| Export pages      | `module.exports = new Clase()`      | `export default new Clase()`            |
