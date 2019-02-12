$(function () {
    $('input').on('keyup', function (e) {
        var current_val = $(this).val()
        if(current_val.length < 15){
            $('.tokainput').text(current_val*0.001);
        }
        else {
            window.alert("type less then 15 integers");
        }
    })
});

$(function () {
    $('input').on('keyup', function (e) {
        var current_val = $(this).val()
        if(current_val.length < 15){
            $('.gpainput').text(current_val*0.01);
        }
        else {
            window.alert("type less then 15 integers");
        }
    })
});

