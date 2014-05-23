BuildRateChange();
HideWarningAlert();


function BuildRateChange() {
    $('button#down, button#up').click(function (data) {
        var action = $(this).data('value');
        var build_id = $(this).parent().attr('id');
        var csrftoken = $(this).parent().find("[name='csrfmiddlewaretoken']");
        var alert_box = $('div#' + build_id + '.alert')
        var rating_box = $('span#' + build_id + '.rating')
        $.ajax({
            url: '/vote/',
            type: "POST",
            data: "id=" + build_id + "&action=" + action + "&csrfmiddlewaretoken=" + csrftoken.val(),
            success: function (data) {
                if (data.status.toLowerCase() === "success") {
                    rating_box.html(data.data.rating);
                }
                else if (data.status.toLowerCase() === "fail") {
                    alert_box.show()
                }
            },
            error: function (data) {
                console.log('server error');
            },
            dataType: "json"
        });
    });
};

function HideWarningAlert() {
    $("[data-hide]").on("click", function () {
        $(this).closest("." + $(this).attr("data-hide")).hide();
    });
}
