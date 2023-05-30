$(document).ready(function(e) {
    $('form').submit(false);

    $("#post").click(function() {
        sendLongUrl();
        if ($(".message").hasClass("long")) {
            $(".message").css("transform", "translateX(0)");
            $(".message").removeClass("long");
            $(".message").addClass("short");
        }

        $("#back").show();
    });

    $("#back").click(function() {
        if ($(".message").hasClass("short")) {
            $(".message").css("transform", "translateX(100%)");
            $(".message").removeClass("short");
            $(".message").addClass("long");
        }

        $("#back").hide();
    });
});

function sendLongUrl() {
    $.ajax({
        type : "POST",
        url : "/api/v1/pipsqueak?" + $.param({url: $("#longurl").val()}),
        dataType: "text",
        success: function (data) {
            console.log(data);
            $("#shorturl").val(data)
        }
    });
}