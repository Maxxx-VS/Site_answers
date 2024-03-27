
document.addEventListener("DOMContentLoaded", function() {
    function submit() {
        var inputs = document.querySelectorAll("input[type='text']");


        for (var i = 0; i < inputs.length; i++) {
            var inputValue = inputs[i].value;
            alert(inputValue);








            inputs[i].value = "";
        }
    }
    var button = document.getElementById("submitBtn");
    button.addEventListener("click", function(event) {
        event.preventDefault();
        submit();
    });
});





