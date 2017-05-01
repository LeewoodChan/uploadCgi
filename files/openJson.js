// JavaScript source code
$(function () {
    //alert("start");
    var jsonName = "../../json/" + document.getElementById("myJson").getAttribute("rel");

    document.getElementById("myJson").innerHTML = "";
    $.getJSON("jsonFile.json", function (result) {
        $.each(result, function (i, field) {
            if (field.length > 100) {
                $('#myJson').append("<li id=" + i + ">Filename: " + i + ".txt : Too much content  </li>");
                //$('#myJson').append("<li id=" + i + ">Filename: " + i + ".txt : " + field + " </li>");
            } else {
                $('#myJson').append("<li id=" + i + ">Filename: " + i + ".txt : " + field + " </li>");
            }
            //alert(field);
        });
    });
});

alert("done");
