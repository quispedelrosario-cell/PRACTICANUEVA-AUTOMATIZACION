pipeline {
    agent any

    environment {
        PW_DIR                 = 'PlaywrightPomLab'
        CY_DIR                 = 'CypressPomLab/Cypress-JavaScript'
        ALLURE_RESULTS_PW      = 'reports/allure-results-playwright'
        ALLURE_RESULTS_CYPRESS = 'reports/allure-results-cypress'
        ALLURE_RESULTS_ALL     = 'reports/allure-results-all'
        ALLURE_REPORT          = 'reports/allure-report'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {
        stage('Stage 1: Playwright + pytest-bdd') {
            steps {
                echo '=== Instalando dependencias Python ==='
                bat '''
                    cd %PW_DIR%
                    python -m venv .venv
                    call .venv\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install pytest pytest-bdd playwright pytest-playwright allure-pytest
                    playwright install chromium
                '''
                echo '=== Ejecutando pruebas BDD ==='
                bat '''
                    cd %PW_DIR%
                    call .venv\\Scripts\\activate.bat
                    pytest -v steps/ --alluredir=..\\%ALLURE_RESULTS_PW% --tb=short
                '''
            }
            post {
                always {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'reports/allure-results-playwright']]
                    ])
                }
                success { echo '✅ Stage 1 completado exitosamente' }
                failure { echo '❌ Stage 1 falló — revisa el reporte Allure' }
            }
        }

        stage('Stage 2: Cypress') {
            steps {
                echo '=== Instalando dependencias Node ==='
                bat '''
                    cd %CY_DIR%
                    npm ci
                    npm install --save-dev @shelex/cypress-allure-plugin
                '''
                echo '=== Ejecutando pruebas Cypress ==='
                bat '''
                    cd %CY_DIR%
                    npx cypress run --env allure=true,allureResultsPath=..\\..\\..\\%ALLURE_RESULTS_CYPRESS%
                '''
            }
            post {
                always {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'reports/allure-results-cypress']]
                    ])
                }
                success { echo '✅ Stage 2 completado exitosamente' }
                failure { echo '❌ Stage 2 falló — revisa el reporte Allure' }
            }
        }

        stage('Stage 3: Reporte Allure Unificado') {
            steps {
                echo '=== Combinando resultados ==='
                bat '''
                    if not exist %ALLURE_RESULTS_ALL% mkdir %ALLURE_RESULTS_ALL%
                    xcopy /E /Y %ALLURE_RESULTS_PW%\\*      %ALLURE_RESULTS_ALL%\\
                    xcopy /E /Y %ALLURE_RESULTS_CYPRESS%\\* %ALLURE_RESULTS_ALL%\\
                '''
                echo '=== Generando reporte HTML unificado ==='
                bat 'allure generate %ALLURE_RESULTS_ALL% --clean -o %ALLURE_REPORT%'
            }
            post {
                always {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'reports/allure-results-all']]
                    ])
                }
                success { echo '✅ Reporte unificado generado' }
                failure { echo '❌ Error al generar reporte unificado' }
            }
        }
    }

    post {
        always {
            echo '=== Pipeline finalizado ==='
            cleanWs()
        }
        success { echo '🎉 Todos los stages pasaron' }
        failure { echo '🔴 El pipeline tuvo fallos' }
    }
}
