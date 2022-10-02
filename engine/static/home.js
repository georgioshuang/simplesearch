

"use strict"

$(document).ready(function(){
    $(".site").change (function () {  
        var selectedsite = $(this).children("option:selected").val();  
    })

    var jobinput = document.getElementById("job");
    var locationinput = document.getElementById("location");
    var siteinput = document.getElementById("site");
    function search() {

        var selectedsite = $('#dropdown').val();
        
        if (selectedsite != "" && jobinput.length != 0 && locationinput.length != 0 ){
            
            window.location.href = selectedsite + "?job=" + $('#job').val() + "&location=" + $('#location').val(); 
        }
    }


    var btn = document.querySelector('#btn');
    btn.addEventListener('click',search)


    
    jobinput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("btn").click();
    }
    });


    
    locationinput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("btn").click();
    }
    });

    jobinput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("btn").click();
        }
        });
        
    siteinput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("btn").click();
    }
    });

    
})




