function fetchTime() {  
    $.getJSON("/time", function(data){
        for (var key in data) {
            $("#" + key).html(key.replace("-", "/") + ": " + data[key]);  // Append the time zone name to the current time
        }   
    });
}
setInterval(fetchTime, 1000);

function detectDevice() {
    if (/iPad|iPhone|iPod/.test(navigator.userAgent) || /iPad|iPhone|iPod/.test(navigator.platform)) {
        return "ios";
    } else if (window.matchMedia("(max-width: 767px)").matches) {
        return "mobile";
    } else {
        return "desktop";
    }
}

$(document).ready(function() {
    var deviceType = detectDevice();
    $("body").addClass(deviceType);
});
