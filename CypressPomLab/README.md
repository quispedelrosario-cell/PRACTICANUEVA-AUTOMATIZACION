# Demo Cypress – JavaScript y TypeScript con POM y BDD

Este laboratorio muestra cómo instalar y ejecutar **Cypress de forma local**, usando **JavaScript** y **TypeScript**, con los patrones **Page Object Model (POM)** y **BDD con Cucumber**, orientado a un curso práctico de automatización Front-End.

El repositorio contiene **dos proyectos independientes**:

```
Cypress-lab/
 ├── Cypress-JavaScript/   ← proyecto con JavaScript
 └── Cypress-TypeScript/   ← proyecto con TypeScript
```

Cada uno tiene su propia instalación de dependencias.

---

## 1️⃣ Requisitos Previos

### Node.js (LTS recomendado)

Descarga desde: https://nodejs.org

```bash
node -v
npm -v
```

> Se recomienda Node.js 18 o superior. Cypress 15.x requiere Node.js >= 18.

### Git (opcional, para clonar el repo)

```bash
git --version
```

### Allure CLI (para reportes)

```bash
npm install -g allure-commandline
allure --version
```

### Navegador Chrome (o Chromium)

Cypress lo usa por defecto en modo interactivo.

---

## 2️⃣ Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd Cypress-lab
```

---

## 3️⃣ Proyecto JavaScript

### 📁 Ubicación

```
Cypress-lab/Cypress-JavaScript/
```

### 📦 Instalación

#### Si clonaste este repositorio

```bash
cd Cypress-JavaScript
npm install
```

#### Si partes desde cero

**1. Inicializa el proyecto:**

```bash
mkdir Cypress-JavaScript
cd Cypress-JavaScript
npm init -y
```

**2. Instala Cypress:**

```bash
npm install cypress --save-dev
```

**3. Instala Allure y BDD (Cucumber):**

```bash
npm install allure-cypress --save-dev
npm install @badeball/cypress-cucumber-preprocessor @bahmutov/cypress-esbuild-preprocessor esbuild --save-dev
```

**4. Abre Cypress por primera vez** para generar la estructura de carpetas:

```bash
npx cypress open
```

**5. Agrega los scripts al `package.json`:**

```json
"scripts": {
  "cy:open": "cypress open",
  "cy:run": "cypress run",
  "allure:generate": "allure generate allure-results --clean -o allure-report",
  "allure:open": "allure open allure-report",
  "allure:report": "npm run cy:run && npm run allure:generate && npm run allure:open"
}
```

**6. Agrega la configuración de Cucumber al `package.json`:**

```json
"cypress-cucumber-preprocessor": {
  "nonGlobalStepDefinitions": false,
  "stepDefinitions": "cypress/e2e/step_definitions/**/*.steps.js"
}
```

### 🚀 Ejecutar las pruebas

#### Modo headless (terminal, sin navegador)

```bash
npm run cy:run
```

#### Modo interactivo — ver la ejecución en el navegador

```bash
npm run cy:open
```

Al abrirse la UI de Cypress:
1. Selecciona **E2E Testing**
2. Elige el navegador (**Chrome** recomendado)
3. Haz clic en el spec que quieres ejecutar (`addToCart.cy.js` o `addToCart.feature`)
4. Se abre Chrome y puedes ver cada paso en tiempo real

#### Modo headed — navegador visible pero desde terminal

```bash
npx cypress run --headed --browser chrome
```

> Útil para ver la ejecución sin abrir la UI completa de Cypress.

#### Ejecutar solo el `.feature` BDD

```bash
npx cypress run --spec "cypress/e2e/addToCart.feature"
npx cypress run --spec "cypress/e2e/addToCart.feature" --headed --browser chrome
```

### 📄 Estructura del proyecto

```
Cypress-JavaScript/
 │    ├── e2e/
 │    │    ├── addToCart.cy.js            ← tests POM
 │    │    ├── addToCart.feature          ← escenarios BDD (Gherkin)
 │    │    └── step_definitions/
 │    │         └── addToCart.steps.js   ← implementación de los steps
 │    ├── fixtures/
 │    │    └── products.json             ← datos de los productos
 │    ├── pages/
 │    │    ├── HomePage.js               ← Page Object: home
 │    │    ├── ProductPage.js            ← Page Object: detalle de producto
 │    │    └── CartPage.js               ← Page Object: carrito
 │    └── support/
 │         ├── commands.js
 │         └── e2e.js
 ├── cypress.config.js
 └── package.json
```

---

## 4️⃣ Proyecto TypeScript

### 📁 Ubicación

```
Cypress-lab/Cypress-TypeScript/
```

### 📦 Instalación

#### Si clonaste este repositorio

```bash
cd Cypress-TypeScript
npm install
```

#### Si partes desde cero

**1. Inicializa el proyecto:**

```bash
mkdir Cypress-TypeScript
cd Cypress-TypeScript
npm init -y
```

**2. Instala Cypress y TypeScript:**

```bash
npm install cypress --save-dev
npm install typescript @types/node --save-dev
```

**3. Instala Allure y BDD (Cucumber):**

```bash
npm install allure-cypress --save-dev
npm install @badeball/cypress-cucumber-preprocessor @bahmutov/cypress-esbuild-preprocessor esbuild --save-dev
```

**4. Abre Cypress por primera vez** para generar la estructura de carpetas:

```bash
npx cypress open
```

**5. Crea el archivo `tsconfig.json`** en la raíz del proyecto:

```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["es5", "dom"],
    "types": ["cypress", "node"],
    "strict": false,
    "skipLibCheck": true,
    "moduleResolution": "node"
  },
  "include": ["cypress/**/*.ts"]
}
```

> `"types": ["cypress", "node"]` permite que el editor reconozca los comandos `cy.*`. No se necesita instalar `@types/cypress` por separado.

**6. Agrega los scripts al `package.json`:**

```json
"scripts": {
  "cy:open": "cypress open",
  "cy:run": "cypress run",
  "allure:generate": "allure generate allure-results --clean -o allure-report",
  "allure:open": "allure open allure-report",
  "allure:report": "npm run cy:run && npm run allure:generate && npm run allure:open"
}
```

**7. Agrega la configuración de Cucumber al `package.json`:**

```json
"cypress-cucumber-preprocessor": {
  "nonGlobalStepDefinitions": false,
  "stepDefinitions": "cypress/e2e/step_definitions/**/*.steps.ts"
}
```

### 🚀 Ejecutar las pruebas

#### Modo headless (terminal, sin navegador)

```bash
npm run cy:run
```

#### Modo interactivo — ver la ejecución en el navegador

```bash
npm run cy:open
```

Al abrirse la UI de Cypress:
1. Selecciona **E2E Testing**
2. Elige el navegador (**Chrome** recomendado)
3. Haz clic en el spec que quieres ejecutar (`addToCart.cy.ts` o `addToCart.feature`)
4. Se abre Chrome y puedes ver cada paso en tiempo real

#### Modo headed — navegador visible pero desde terminal

```bash
npx cypress run --headed --browser chrome
```

> Útil para ver la ejecución sin abrir la UI completa de Cypress.

#### Ejecutar solo el `.feature` BDD

```bash
npx cypress run --spec "cypress/e2e/addToCart.feature"
npx cypress run --spec "cypress/e2e/addToCart.feature" --headed --browser chrome
```

### 📄 Estructura del proyecto
 ├── cypress/
 │    ├── e2e/
 │    │    ├── addToCart.cy.ts            ← tests POM
 │    │    ├── addToCart.feature          ← escenarios BDD (Gherkin)
 │    │    └── step_definitions/
 │    │         └── addToCart.steps.ts   ← implementación de los steps
 │    ├── fixtures/
 │    │    └── products.json             ← datos de los productos
 │    ├── pages/
 │    │    ├── HomePage.ts               ← Page Object: home
 │    │    ├── ProductPage.ts            ← Page Object: detalle de producto
 │    │    └── CartPage.ts               ← Page Object: carrito
 │    └── support/
 │         ├── commands.js
 │         └── e2e.js
 ├── cypress.config.js
 ├── tsconfig.json
 └── package.json
```

---

## 5️⃣ Feature: Agregar artículo al carrito

Sitio de prueba: [sauce-demo.myshopify.com](https://sauce-demo.myshopify.com/)

### 🗺️ Outline del flujo

```
Product Page  →  Add to Cart  →  Cart Page
```

| Paso | Acción                            | Verificación                      |
|------|-----------------------------------|-----------------------------------|
| 1    | Navegar al producto (Grey jacket) | Título y precio correctos         |
| 2    | Hacer clic en "Add to Cart"       | Sin errores en la URL             |
| 3    | Ir al carrito                     | El producto aparece en el carrito |

---

## 6️⃣ Patrón POM (Page Object Model)

El **Page Object Model** separa la lógica de los tests de los selectores y acciones de cada página:

- **Page Object** — encapsula selectores y métodos de una página
- **Test** — usa los Page Objects sin conocer los selectores directamente
- **Fixture** — provee los datos de prueba (nombres, precios, URLs)

### 📄 Page Object (JavaScript)

```javascript
// cypress/pages/ProductPage.js
class ProductPage {
  get productTitle() {
    return cy.get('h1')
  }

  addToCart() {
    cy.get('form[action="/cart/add"] button[type="submit"]')
      .first()
      .click()
  }

  verifyProductTitle(title) {
    this.productTitle.should('contain.text', title)
  }
}

module.exports = new ProductPage()
```

### 📄 Page Object (TypeScript)

```typescript
// cypress/pages/ProductPage.ts
export class ProductPage {
  get productTitle(): Cypress.Chainable {
    return cy.get('h1')
  }

  addToCart(): void {
    cy.get('form[action="/cart/add"] button[type="submit"]')
      .first()
      .click()
  }

  verifyProductTitle(title: string): void {
    this.productTitle.should('contain.text', title)
  }
}

export default new ProductPage()
```

### 📄 Test POM

```javascript
// cypress/e2e/addToCart.cy.js
const productPage = require('../pages/ProductPage')
const cartPage    = require('../pages/CartPage')

describe('Agregar artículo al carrito', () => {
  it('Debe agregar el producto y mostrarlo en el carrito', () => {
    cy.visit('https://sauce-demo.myshopify.com/collections/frontpage/products/grey-jacket')
    productPage.verifyProductTitle('Grey jacket')
    productPage.addToCart()
    cy.visit('https://sauce-demo.myshopify.com/cart')
    cartPage.verifyCartNotEmpty()
  })
})
```

> En TypeScript usa `import productPage from '../pages/ProductPage'` y extensión `.cy.ts`.

---

## 7️⃣ BDD con Cucumber (Gherkin)

Los tests BDD usan archivos `.feature` con sintaxis Gherkin y step definitions que implementan cada paso usando los Page Objects.

### 📄 Archivo `.feature`

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
```

### 📄 Step Definitions (JavaScript)

```javascript
// cypress/e2e/step_definitions/addToCart.steps.js
const { Given, When, Then } = require('@badeball/cypress-cucumber-preprocessor')
const productPage = require('../../pages/ProductPage')
const cartPage    = require('../../pages/CartPage')

Given('que estoy en la página del producto {string}', (productName) => {
  cy.visit(`https://sauce-demo.myshopify.com/collections/frontpage/products/${productName.toLowerCase().replace(' ', '-')}`)
})

Then('el título del producto debe ser {string}', (title) => {
  productPage.verifyProductTitle(title)
})

When('agrego el producto al carrito', () => {
  productPage.addToCart()
})

Then('el producto {string} debe aparecer en el carrito', (productName) => {
  cy.visit('https://sauce-demo.myshopify.com/cart')
  cartPage.verifyCartNotEmpty()
  cy.get('body').should('contain.text', productName)
})
```

> En TypeScript usa `import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor'` y extensión `.steps.ts`.

### ⚙️ Configuración en `cypress.config.js`

```javascript
const { defineConfig } = require("cypress");
const { allureCypress } = require("allure-cypress/reporter");
const createBundler = require("@bahmutov/cypress-esbuild-preprocessor");
const { addCucumberPreprocessorPlugin } = require("@badeball/cypress-cucumber-preprocessor");
const { createEsbuildPlugin } = require("@badeball/cypress-cucumber-preprocessor/esbuild");

module.exports = defineConfig({
  e2e: {
    specPattern: "cypress/e2e/**/*.{cy.js,feature}",  // o cy.ts para TypeScript
    async setupNodeEvents(on, config) {
      allureCypress(on, config, { resultsDir: "allure-results" });
      await addCucumberPreprocessorPlugin(on, config);
      on("file:preprocessor", createBundler({
        plugins: [createEsbuildPlugin(config)]
      }));
      return config;
    },
  },
});
```

---

## 8️⃣ Evidencia y Reportes con Allure

Este proyecto usa [allure-cypress](https://www.npmjs.com/package/allure-cypress) para generar reportes visuales con evidencia (screenshots) embebida.

### 📸 Cómo funciona la evidencia

Al final del último step BDD se toma un screenshot con `cy.screenshot()`. El hook `after:screenshot` en `cypress.config.js` copia automáticamente la imagen a `allure-results/`, donde Allure la incluye como attachment del test.

```javascript
// En el step definition — último Then
cy.screenshot(`carrito-con-${productName.toLowerCase().replace(/ /g, '-')}`, { overwrite: true })
```

```javascript
// En cypress.config.js — copia automática a allure-results/
on("after:screenshot", (details) => {
  const imgBuffer = fs.readFileSync(details.path)
  const attachmentPath = path.join(allureResultsDir, path.basename(details.path))
  fs.writeFileSync(attachmentPath, imgBuffer)
  return details
})
```

### 🚀 Generar el reporte

```bash
npm run cy:run           # ejecuta los tests → genera allure-results/
npm run allure:generate  # convierte resultados en HTML → genera allure-report/
npm run allure:open      # abre el reporte en el navegador
```

O en un solo comando:

```bash
npm run allure:report
```

### 📊 Scripts y modos de ejecución

| Comando                                                        | Descripción                                      |
|----------------------------------------------------------------|--------------------------------------------------|
| `npm run cy:open`                                              | Abre la UI — selecciona spec y ves la ejecución  |
| `npm run cy:run`                                               | Headless — sin navegador visible                 |
| `npx cypress run --headed --browser chrome`                    | Headed — navegador visible desde terminal        |
| `npx cypress run --spec "cypress/e2e/addToCart.feature"`       | Solo el `.feature` BDD, headless                 |
| `npx cypress run --spec "cypress/e2e/addToCart.feature" --headed --browser chrome` | Solo el `.feature`, con navegador visible |
| `npm run allure:generate`                                      | Convierte los resultados en reporte HTML         |
| `npm run allure:open`                                          | Abre el reporte en el navegador                  |
| `npm run allure:report`                                        | Ejecuta cy:run + genera + abre el reporte        |

### 📁 Carpetas generadas (agregar al `.gitignore`)

```
allure-results/   ← datos crudos + screenshots copiados automáticamente
allure-report/    ← reporte HTML final con evidencia embebida
cypress/screenshots/  ← screenshots originales de Cypress
```

> Si quieres ver solo los scenarios BDD en el reporte, ejecuta únicamente el `.feature`:
> ```bash
> npx cypress run --spec "cypress/e2e/addToCart.feature"
> ```

---

## 9️⃣ Puntos clave para explicar en clase

- Cypress **no necesita waits manuales** — tiene esperas automáticas integradas
- El patrón **POM** hace los tests más mantenibles y reutilizables
- Los archivos **`.feature`** permiten escribir tests en lenguaje natural (Gherkin)
- Los **step definitions** conectan el Gherkin con los Page Objects
- **Fixtures** centralizan los datos de prueba
- La extensión del archivo (`.cy.js` vs `.cy.ts`) determina el lenguaje usado

---

## 🔟 Buenas prácticas

- No usar `cy.wait(5000)` — usar `should()` para sincronización
- Separar tests por feature o módulo
- Usar `fixtures` para datos de prueba
- Usar `cy.intercept()` para mockear llamadas de red
- Nombrar los scenarios BDD en lenguaje de negocio, no técnico
- Agregar `allure-results/` y `allure-report/` al `.gitignore`

---

🚀 Este demo está listo para evolucionar a:
- Mocks con `cy.intercept`
- CI/CD con GitHub Actions
- Scenarios con `Scenario Outline` y `Examples` en Gherkin

---

## 📖 Documentación adicional

- [GUIA-NUEVO-CASO.md](./GUIA-NUEVO-CASO.md) — Paso a paso para crear un nuevo caso de prueba en JS o TS
