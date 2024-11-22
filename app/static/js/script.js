$(document).ready(function () { 
  console.log("oi")
  var campo = $("#CEP");
  campo.mask('00000-000', {reverse: true});
});