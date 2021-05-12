$("form[name=loginForm]").submit(function (e) {
	var $form = $(this);
	var $error = $form.find("#loginError");
	var data = $form.serialize();

	$.ajax({
		url: "/login",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/index";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("d-none");
		},
	});

	e.preventDefault();
});
