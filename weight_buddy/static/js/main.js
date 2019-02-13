jQuery(function () {

	jQuery('#type, #major_muscule, #minior_muscule').select2();

	jQuery("#type").on("select2:select", function (e) {

		var input, filter, table, tr, td, i, txtValue;
		input = document.getElementById("type");
		filter = input.value.toUpperCase();
		table = document.getElementById("exercise-list-html");
		tr = table.getElementsByTagName("tr");

		// Loop through all table rows, and hide those who don't match the search query
		for (i = 0; i < tr.length; i++) {
			td = tr[i].getElementsByTagName("td")[2];
			if (td) {
				txtValue = td.textContent || td.innerText;
				if (txtValue.toUpperCase().indexOf(filter) > -1) {
					tr[i].style.display = "";
				} else {
					tr[i].style.display = "none";
				}
			}
		}
	});

	
	jQuery("#major_muscule").on("select2:select", function (e) {
		var input, filter, table, tr, td, i, txtValue;
		input = document.getElementById("major_muscule");
		filter = input.value.toUpperCase();
		table = document.getElementById("exercise-list-html");
		tr = table.getElementsByTagName("tr");

		// Loop through all table rows, and hide those who don't match the search query
		for (i = 0; i < tr.length; i++) {
			td = tr[i].getElementsByTagName("td")[3];
			if (td) {
				txtValue = td.textContent || td.innerText;
				if (txtValue.toUpperCase().indexOf(filter) > -1) {
					tr[i].style.display = "";
				} else {
					tr[i].style.display = "none";
				}
			}
		}
	});

	jQuery("#minior_muscule").on("select2:select", function (e) {
		var input, filter, table, tr, td, i, txtValue;
		input = document.getElementById("minior_muscule");
		filter = input.value.toUpperCase();
		table = document.getElementById("exercise-list-html");
		tr = table.getElementsByTagName("tr");

		// Loop through all table rows, and hide those who don't match the search query
		for (i = 0; i < tr.length; i++) {
			td = tr[i].getElementsByTagName("td")[4];
			if (td) {
				txtValue = td.textContent || td.innerText;
				if (txtValue.toUpperCase().indexOf(filter) > -1) {
					tr[i].style.display = "";
				} else {
					tr[i].style.display = "none";
				}
			}
		}
	});

});
