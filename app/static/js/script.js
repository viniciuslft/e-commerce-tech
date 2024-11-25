$(document).ready(function () { 
  console.log("oi")
  var campo = $("#CEP");
  campo.mask('00000-000', {reverse: true});
});


//script envolvendo as mensagens para o usuario

document.addEventListener('DOMContentLoaded', () =>{
  const flashedMessages = document.querySelectorAll('.flash-message');

  flashedMessages.forEach(message => {
    setTimeout(() => {
      message.classList.add('show');
    }, 100)
  })


  setTimeout(() => {
    flashedMessages.forEach(message => {
      message.classList.remove('show');
      message.classList.add('hide');
      setTimeout(() => message.remove(),1000);
    })
  }, 1300)

})



