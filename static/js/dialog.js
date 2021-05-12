$("form[name=addMSGForm]").submit(function (e) {
	var $form = $(this);
	var data = $form.serialize();

	$.ajax({
		url: "/addContent",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/manageScenario";
		},
	});

	e.preventDefault();
});

$("form[name=editMSGForm]").submit(function (e) {
	var $form = $(this);
	var data = $form.serialize();

	$.ajax({
		url: $(this).attr("action"),
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/manageScenario";
		},
	});

	e.preventDefault();
});

$("#dlAllContentBtn").click(function (e) {
	$.ajax({
		url: "/deleteAllContent",
		success: function (resp) {
			window.location.href = "/manageScenario";
		},
	});
	e.preventDefault();
});

$("a[name=dlMessage]").click(function (e) {
	$.ajax({
		url: $(this).attr("href"),
		success: function (resp) {
			window.location.href = "/manageScenario";
		},
	});
});
