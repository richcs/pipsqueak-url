$(document).ready(function(e) {
    $("#back").click(function() {
      if ($(".message").hasClass("login")) {
        $(".message").css("transform", "translateX(100%)");
        $(".message").removeClass("login");
        $(".message").addClass("signup");
      }
      else if ($(".message").hasClass("signup")) {
          $(".message").css("transform", "translateX(0)");
          $(".message").removeClass("signup");
          $(".message").addClass("login");
      }
    });
});