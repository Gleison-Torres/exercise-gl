
/* Mascara */
$(document).ready(function(){
    $('#id_postal_code').mask('00000-000');
});

/* API CEP jquery */

$(document).ready(function() {

    function limpa_formulário_cep() {
        $("#id_street_address").val("");
        $("#id_neighborhood").val("");
        $("#id_city").val("");
        $("#id_state").val("");
    }

    $("#id_postal_code").blur(function() {

        var cep = $(this).val().replace(/\D/g, '');

        if (cep != "") {

            var validacep = /^[0-9]{8}$/;

            if(validacep.test(cep)) {

                $("#id_street_address").val("...");
                $("#id_neighborhood").val("...");
                $("#id_city").val("...");
                $("#id_state").val("...");

                //Consulta o webservice viacep.com.br/

                $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                    if (!("erro" in dados)) {
                        //Atualiza os campos com os valores da consulta.
                        $("#id_street_address").val(dados.logradouro);
                        $("#id_neighborhood").val(dados.bairro);
                        $("#id_city").val(dados.localidade);
                        $("#id_state").val(dados.uf);
                    }
                    else {
                        //CEP pesquisado não foi encontrado.
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            }
            else {
                //cep é inválido.
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        }
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    });
});
