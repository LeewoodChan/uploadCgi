// JavaScript source code
$(function () {
    //alert("start");
    var jsonName = "../../json/" + document.getElementById("myJson").getAttribute("rel");

    document.getElementById("myJson").innerHTML = "";
    $.each(myJson,function(i, field){
        if (field.length > 100) {
            $('#myJson').append("<li id=" + i + ">Filename: " + i + ".txt : too much </li>");
            //$('#myJson').append("<li id=" + i + ">Filename: " + i + ".txt : " + field + " </li>");
        } else {
        $('#myJson').append("<li id=" + i + ">Filename: " + i + ".txt : " + field + " </li>");
        }
    });

    //if there is an external json use this follow code to open a json file. "$.getJSON("filename",function (result){..})
/*
    $.getJSON(myJ, function (result) {
        $.each(result, function (i, field) {
            if (field.length > 100) {
                $('#myJson').append("<li id=" + i + ">Filename: " + i + ".txt : too much </li>");
                //$('#myJson').append("<li id=" + i + ">Filename: " + i + ".txt : " + field + " </li>");
            } else {
                $('#myJson').append("<li id=" + i + ">Filename: " + i + ".txt : " + field + " </li>");
            }
            //alert(field);
        });
    });
    */
});

//alert("done");
