$("form[name=regForm]").submit(function (e) {
	var $form = $(this);
	var $error = $form.find("#regError");
	var data = $form.serialize();

	$.ajax({
		url: "/register",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/register";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("d-none");
		},
	});

	e.preventDefault();
});
