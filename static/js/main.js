$(document).ready(function fnHandler() {
    alert('Hi!');
    prompt('What can I do for you?','make a Sandwich');
});
/*
jQuery(function () {

    jQuery('#course, #location').select2();

    jQuery("#course").on("select2:select", function (e) {
        var course = jQuery("#course").val();
        jQuery('#events-table tr .hidden-course').removeClass('hidden-course');
        jQuery('#events-table tr:not(".' + course + '-event")').addClass('hidden-course');
        if (course == 'all') {
            jQuery('#events-table tr').removeClass('hidden-course');
        }
    });

    jQuery("#location").on("select2:select", function (e) {
        var loc = $('#location').val();
        jQuery('#events-table tr .hidden-location').removeClass('hidden-location');
        jQuery('#events-table tr:not(".' + loc + '")').addClass('hidden-location');
        if (loc == 'all') {
            jQuery('#events-table tr').removeClass('hidden-location');
        }
    });
});



*/ 