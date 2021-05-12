$("form[name=addGRForm]").submit(function (e) {
	var $form = $(this);
	var $error = $form.find("#addGroupHelp");
	var data = $form.serialize();

	$.ajax({
		url: "/addGroup",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/manageGroups";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("d-none");
		},
	});

	e.preventDefault();
});
$("#dlAllGroupBtn").click(function (e) {
	$.ajax({
		url: "/deleteAllGroups",
		success: function (resp) {
			window.location.href = "/manageGroups";
		},
	});
	e.preventDefault();
});

$("a[name=dlGroupBtn]").click(function (e) {
	$.ajax({
		url: $(this).attr("href"),
		success: function (resp) {
			window.location.href = "/manageGroups";
		},
	});
	e.preventDefault();
});
