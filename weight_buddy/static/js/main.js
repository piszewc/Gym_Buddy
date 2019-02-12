jQuery(function () {

	jQuery('#type, #major_muscule, #minior_muscule').select2();

	jQuery("#type").on("select2:select", function (e) {
		var type = jQuery('#type').val();
		jQuery('#exercise-list-html tr.hidden-type').removeClass('hidden-type');
		jQuery('#exercise-list-html tr:not(".' +type+'-type")').addClass('hidden-type');
		if (type == 'all') {
			jQuery('#exercise-list-html tr').removeClass('hidden-type');
		}
	});

	jQuery("#major_muscule").on("select2:select", function (e) {
		var major_muscule = $('#major_muscule').val();
		jQuery('#exercise-list-html tr.hidden-major_muscule').removeClass('hidden-major_muscule');
		jQuery('#exercise-list-html tr:not(".' + major_muscule + '-major_muscule")').addClass('hidden-major_muscule');
		if (major_muscule == 'all') {
			jQuery('#exercise-list-html tr').removeClass('hidden-major_muscule');
		}
	});
	jQuery("#minior_muscule").on("select2:select", function (e) {
		var minior_muscule = $('#minior_muscule').val();
		jQuery('#exercise-list-html tr.hidden-minior_muscule').removeClass('hidden-minior_muscule');
		jQuery('#exercise-list-html tr:not(".' + minior_muscule + '-minior_muscule")').addClass('hidden-minior_muscule');
		if (minior_muscule == 'all') {
			jQuery('#exercise-list-html tr').removeClass('hidden-minior_muscule');
		}
	});
});