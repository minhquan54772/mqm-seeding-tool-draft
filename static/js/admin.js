$("form[name=setADForm]").submit(function (e) {
	var $form = $(this);
	var $error = $form.find("#setADError");
	var data = $form.serialize();

	$.ajax({
		url: $(this).attr("action"),
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/setAdmin";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("d-none");
		},
	});

	e.preventDefault();
});

$("form[name=revokeADForm]").submit(function (e) {
	var $form = $(this);
	var $error = $form.find("#revokeADError");
	var data = $form.serialize();

	$.ajax({
		url: $(this).attr("action"),
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/setAdmin";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("d-none");
		},
	});

	e.preventDefault();
});
