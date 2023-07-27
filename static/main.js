function fetchTime() {  
    $.getJSON("/time", function(data){
        for (var key in data) {
            $("#" + key).html(key.replace("-", "/") + ": " + data[key]);  // Append the time zone name to the current time
        }   
    });
}
setInterval(fetchTime, 1000);
