const { defineConfig } = require("cypress");
const { allureCypress } = require("allure-cypress/reporter");
const createBundler = require("@bahmutov/cypress-esbuild-preprocessor");
const { addCucumberPreprocessorPlugin } = require("@badeball/cypress-cucumber-preprocessor");
const { createEsbuildPlugin } = require("@badeball/cypress-cucumber-preprocessor/esbuild");
const fs = require("fs");
const path = require("path");

module.exports = defineConfig({
  e2e: {
    specPattern: "cypress/e2e/**/*.{cy.js,feature}",
    screenshotsFolder: "cypress/screenshots",
    async setupNodeEvents(on, config) {
      // Allure reporter
      allureCypress(on, config, { resultsDir: "allure-results" });

      // Adjuntar screenshots manuales a Allure automáticamente
      on("after:screenshot", (details) => {
        const allureResultsDir = path.join(process.cwd(), "allure-results");
        if (!fs.existsSync(allureResultsDir)) return details;

        const imgBuffer = fs.readFileSync(details.path);
        const attachmentName = path.basename(details.path, ".png") + "-attachment.png";
        const attachmentPath = path.join(allureResultsDir, attachmentName);
        fs.writeFileSync(attachmentPath, imgBuffer);
        return details;
      });

      // Cucumber BDD preprocessor
      await addCucumberPreprocessorPlugin(on, config);
      on(
        "file:preprocessor",
        createBundler({ plugins: [createEsbuildPlugin(config)] })
      );

      return config;
    },
  },
});
