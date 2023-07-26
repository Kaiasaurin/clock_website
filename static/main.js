function fetchTime() {  
    $.getJSON("/time", function(data){
        for (var key in data) {
            $("#"+ key.replace("/", "-")).html(data[key]);
        }   
    });
}

setInterval(fetchTime, 1000);
