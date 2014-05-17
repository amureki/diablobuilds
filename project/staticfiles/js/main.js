BuildRateChange();
HideWarningAlert();


function BuildRateChange() {
    $('button#down, button#up').click(function (data) {
        var action = $(this).data('value');
        var build_id = window.location.pathname.replace(/[^\d.]/g, '');
        var csrftoken = $(this).parent().find("[name='csrfmiddlewaretoken']");
//        alert(window.location.pathname);
        $.ajax({
            url: '/vote/',
            type: "POST",
            data: "id=" + build_id + "&action=" + action + "&csrfmiddlewaretoken=" + csrftoken.val(),
            success: function (data) {
                if (data.status.toLowerCase() === "success") {
                    $('span#rating').html(data.data.rating);
                }
                else if (data.status.toLowerCase() === "fail") {
                    $(".alert").show()
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
