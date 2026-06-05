Feature: Agregar un nuevo usuario
 Como usuario nuevo de Demoblaze
 Quiero registrarme en la tienda
 Para poder iniciar sesión y comprar productos

 Background:
   Given que estoy en la pagina principal de Demoblaze

 Scenario Outline: Registrar un nuevo usuario
   When hago clic en el botón de registro
   And ingreso un nombre de usuario "usuario" y una contraseña "password"
   And confirmo el registro
   Then debo ver la alerta "Sign up successful."
   Examples:
     | usuario   | password   |
     | uGR1     | pass123    |
     | BYF2     | pass456    |