// Essa função retorna todos os anos possíveis referentes a contratos.



// Essa função recebe url e tipo de contrato, vem pelo campo, e retora um json
// Contendo ano, mês, valor somado, e nome do

function get_event_totals(url, contract_type){
    $.ajax({
        url:url,
        type: 'GET',
        dataType : 'json',
        cache: false,
        data:{
            contract_type:contract_type,
        },
        success: function(callback){
            return callback
        },
        error: function(xhr){
            console.error(xhr)
        }
    
    })
}

function get_contract_totals(url){
    $.ajax({
        url:url,
        type: 'GET',
        dataType : 'json',
        cache: false,
        data:{
            contract_type:contract_type,
        },
        success: function(callback){
            return callback
        },
        error: function(xhr){
            console.error(xhr)
        }
    
    })
    }
