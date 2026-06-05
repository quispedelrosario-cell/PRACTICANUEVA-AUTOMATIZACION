
Feature: Agregar artículo al carrito en Demoblaze
  Como cliente quiero agregar un producto al carrito
  Para poder verificar la compra en el sitio demoblaze.com

  Scenario: Agregar Iphone 6 32gb al carrito
    Given que estoy en la página principal de Demoblaze
    When selecciono la categoría "Phones"
    And selecciono el producto "Iphone 6 32gb"
    And agrego el producto al carrito
    Then debe mostrarse la alerta "Product added"
    And el producto "Iphone 6 32gb" debe aparecer en el carrito


  Scenario: Agregar Sony vaio i5 al carrito
    Given que estoy en la página principal de Demoblaze
    When selecciono la categoría "Laptops"
    And selecciono el producto "Sony vaio i5"
    And agrego el producto al carrito
    Then debe mostrarse la alerta "Product added"
    And el producto "Sony vaio i5" debe aparecer en el carrito 


    # Seleccionar mas de un producto y verificar que ambos estén en el carrito
  Scenario: Agregar varios productos al carrito
    Given que estoy en la página principal de Demoblaze
    When selecciono la categoría "Phones" 
    And selecciono el producto "Iphone 6 32gb"
    And agrego el producto al carrito   
    And debe mostrarse la alerta "Product added" para el producto "Iphone 6 32gb"
    And vuelvo a la página principal
    And selecciono la categoría "Laptops"
    And selecciono el producto "Sony vaio i5" 
    And agrego el producto al carrito
    Then debe mostrarse la alerta "Product added" para el producto "Sony vaio i5"
    And ambos productos "Iphone 6 32gb" y "Sony vaio i5" deben aparecer en el carrito
    