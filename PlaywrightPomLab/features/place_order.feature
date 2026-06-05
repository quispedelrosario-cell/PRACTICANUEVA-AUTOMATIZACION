# language: es
Feature: Agregar productos al carrito en Demoblaze


  Scenario: Comprar varios productos y completar Place Order
    Given que estoy en la página principal de Demoblaze
    When selecciono la categoría "Phones"
    And selecciono el producto "Iphone 6 32gb"
    And agrego el producto al carrito
    Then debe mostrarse la alerta "Product added"
    And vuelvo a la página principal
    And selecciono la categoría "Laptops"
    And selecciono el producto "Sony vaio i5"
    And agrego el producto al carrito
    Then debe mostrarse la alerta "Product added"
    And vuelvo a la página principal
    And selecciono la categoría "Monitors"
    And selecciono el producto "Apple monitor 24"
    And agrego el producto al carrito
    Then debe mostrarse la alerta "Product added"
    And el producto "Iphone 6 32gb" debe aparecer en el carrito
    And el producto "Sony vaio i5" debe aparecer en el carrito
    And el producto "Apple monitor 24" debe aparecer en el carrito
    When selecciono el boton "Place Order"
    Then se debe abrir el formulario de place order
    And completo el formulario de place order con los siguientes datos:
      | nombre              | pais    | ciudad | tarjeta  | mes  | año  |
      | Marcia | BOLIVIA | LA PAZ | 99923    | MAYO | 2026 |
    And confirmo seleccionar "Purchase"
    Then se debe mostrar el mensaje de confirmación de compra

  