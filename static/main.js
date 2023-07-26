function fetchTime() {  
    $.getJSON("/time", function(data){
        for (var key in data) {
            $("#"+ key).html(data[key]);
        }   
    });
}

setInterval(fetchTime, 1000);
