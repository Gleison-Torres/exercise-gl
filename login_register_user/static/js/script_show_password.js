var pass = $('#password');
var eye = $(".input-password i");

eye.mousedown(function() {
    pass.attr("type", "text");
});

eye.mouseup(function() {
    pass.attr("type", "password");
});

$( ".input-password i" ).mouseout(function() {
    $("#passwoord").attr("type", "password");
});