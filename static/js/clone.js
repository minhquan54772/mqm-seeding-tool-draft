$("form[name=addCloneFrom]").submit(function (e) {
	var $form = $(this);
	var $error = $form.find("#addCloneError");
	var data = $form.serialize();

	$.ajax({
		url: "/addUser",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/manageCloneAccount";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("d-none");
		},
	});

	e.preventDefault();
});

$("form[name=editCloneForm]").submit(function (e) {
	var $form = $(this);
	var data = $form.serialize();

	$.ajax({
		url: $(this).attr("action"),
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/manageCloneAccount";
		},
	});

	e.preventDefault();
});

$("#dlAllCloneBtn").click(function (e) {
	$.ajax({
		url: "/deleteAllUsers",
		success: function (resp) {
			window.location.href = "/manageCloneAccount";
		},
	});
	e.preventDefault();
});

$("a[name=deleteCloneBtn]").click(function (e) {
	$.ajax({
		url: $(this).attr("href"),
		success: function (resp) {
			window.location.href = "/manageCloneAccount";
		},
	});
	e.preventDefault();
});
