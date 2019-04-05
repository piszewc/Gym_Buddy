$(document).ready(function () {
    $("#newsletter_button").click(function () {
        $("button").removeClass("btn-primary");
        $("span", this).text("Thanks!");
        $(this).addClass("btn-success");
    });

    $("#newsletter_button_final").click(function () {
        $("button").removeClass("btn-outline-primary");
        $(this).addClass("btn-outline-success");
        $("span", this).text("Thanks!");
    });

});

$(document).ready(function() {
    $('#exercise-list-html').DataTable({

        "scrollX": true,
       
    });
    
} );
var table = $('#exercise-list-html').DataTable({}) ;

table.on('page.dt', function() {
    $('html, body').animate({
      scrollTop: $(".dataTables_wrapper").offset().top
    }, 'slow');
  
    $('thead tr th:first-child').focus().blur();
  });