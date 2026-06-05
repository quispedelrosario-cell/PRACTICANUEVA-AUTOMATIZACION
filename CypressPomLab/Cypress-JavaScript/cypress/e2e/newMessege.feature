Feature: Enviar un nuevo mensaje
  Como usuario registrado de Demoblaze
  Quiero enviar un mensaje a través del formulario de contacto
  Para poder comunicarme con el soporte de la tienda

 Background:
   Given que estoy en la pagina principal de Demoblaze
   

 Scenario: Enviar un mensaje a través del formulario de contacto
   When hago clic en el enlace "Contact"
   And completo el formulario con un email válido, un nombre y un mensaje
   And envio el mensaje al hacer clic en el botón "Send message"
   Then debo ver una alerta con el mensaje "Thanks for the message!!"