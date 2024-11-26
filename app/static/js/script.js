$(document).ready(function () {
  var campoCEP = $("#CEP");
  campoCEP.mask('00000-000', {reverse: true});

  function corSelectCategoria() {
    $('#categoriaProduto').change(function() {
     var selecaoCategoria = $(this).val()
     if(selecaoCategoria === "0") {
       $(this).addClass('text-muted');
     } else {
       $(this).removeClass('text-muted');
     }
   })
   if($('#categoriaProduto').val() === "0") {
     $('#categoriaProduto').addClass('text-muted');
   }

  }
  corSelectCategoria();


  const dropArea = $(".drag-area");
  const botaoDrag = dropArea.find(".file-input-button");
  const input = dropArea.find(".file-input");

  botaoDrag.on("click", () => input.click());
  input.on("change", (e) => processaArquivo(e.target.files[0]));

  dropArea.on("dragover", (e) => {
    e.preventDefault();
    dropArea.addClass("active");
  });

  dropArea.on("dragleave", () => dropArea.removeClass("active"));

  dropArea.on("drop", (e) => {
    e.preventDefault();
    dropArea.removeClass("active");
    processaArquivo(e.originalEvent.dataTransfer.files[0]);
  });

  const processaArquivo = (file) => {
    const allowedTypes = ["image/png", "image/jpg", "image/jpeg"];
    const sizeInMB = (file.size / (1024 * 1024)).toFixed(2);

    if (!allowedTypes.includes(file.type)) {
      alert("Por favor, envie uma imagem (jpg, jpeg ou png).");
      return;
    }
    if (sizeInMB > 5) {
      alert("O arquivo deve ter no máximo 5MB.");
      return;
    }

    console.log(`Arquivo: ${file.name} (${sizeInMB} MB) - Tipo: ${file.type}`);
  };



  $('#precoProduto').on('keypress', function(e) {
    const charCode = e.which ? e.which : e.keyCode;
    
    if (charCode < 48 || charCode > 57) {
      e.preventDefault();
    }
  });

  $('#clearInputs').click(function() {
    $('#nomeProduto').val('');
    $('#descricaoProduto').val('');
    $('#precoProduto').val('');
    $('#quantidadeProduto').val('');
    $('#categoriaProduto').val('');
    
    // window.location.reload();
  })
  
  const maxCaracteres = 120;

  $('#descricaoProduto').on('input', function(event) {
    event.preventDefault()
    const caracteresDigitados = $(this).val().length;
    const caracteresRestantes = maxCaracteres - caracteresDigitados;

    $('#contagemCaracteres strong').text(caracteresRestantes); // Atualiza o contador
  });

  $('#precoProduto').on('focus', function() {
    $('#inputGroupFocus').addClass('focus');
  })
  $('#precoProduto').on('blur', function() {
    $('#inputGroupFocus').removeClass('focus');
  })

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



