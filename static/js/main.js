$(document).ready(function() {

    // AJAX GET
    // $('.get-more').click(function(){

    //     $.ajax({
    //         type: "GET",
    //         url: "/ajax/more/",
    //         success: function(data) {
    //         for(i = 0; i < data.length; i++){
    //             $('ul').append('<li>'+data[i]+'</li>');
    //         }
    //     }
    //     });

    // });

    // AJAX POST
    $('.add-todo1').click(function(e){
      console.log('sanity test');
      e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/ajax/add/",
            dataType: "json",
            data: { "item": $(".form-control1").val() },
            success: function(data) {
                alert(data.message);
            }
        });

    });

    $('.txt').click(function(){
        var $ctrl = $('<input/>').attr({ type: 'text', name:'text', value:'text'}).addClass("text");
        $(".holder").append($ctrl);
    });

    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 


});
