var loadFile = function (event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
    image.style.width="170px"
    image.style.height="170px";
    image.style.display="block"
    image.style.borderRadius="50%"
};

$(document).ready(function () {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".input_fields_wrap"); //Fields wrapper
    var add_button = $(".add_field_button"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" class="box" name="skill"/><a href="#" class="remove_field">&nbsp;&nbsp;&nbsp;&nbsp;Remove&nbsp;&nbsp;</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});

$(document).ready(function () {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".input_fields_wrap2"); //Fields wrapper
    var add_button = $(".add_field_button2"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" class="box" name="hobby"/><a href="#" class="remove_field">&nbsp;&nbsp;&nbsp;&nbsp;Remove&nbsp;&nbsp;</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});


$(document).ready(function () {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".input_fields_wrap3"); //Fields wrapper
    var add_button = $(".add_field_button3"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" class="box" name="lang"/><a href="#" class="remove_field">&nbsp;&nbsp;&nbsp;&nbsp;Remove&nbsp;&nbsp;</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});

$(document).ready(function () {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".input_fields_wrap4"); //Fields wrapper
    var add_button = $(".add_field_button4"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" class="box" name="social_media"/><a href="#" class="remove_field">&nbsp;&nbsp;&nbsp;&nbsp;Remove&nbsp;&nbsp;</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});