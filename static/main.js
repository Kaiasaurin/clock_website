function fetchTime() {  
    $.getJSON("/time", function(data){
        for (var key in data) {
            $("#" + key).html(data[key]);  // Use the key directly as the ID
        }   
    });
}

setInterval(fetchTime, 1000);
