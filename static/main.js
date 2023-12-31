function detectDevice() {
    if (/iPad|iPhone|iPod/.test(navigator.userAgent) || (/iPad|iPhone|iPod/.test(navigator.platform)) || (navigator.maxTouchPoints && navigator.maxTouchPoints > 2 && /MacIntel/.test(navigator.platform))) {
        return "ios";
    } else if (window.matchMedia("(max-width: 767px)").matches) {
        return "mobile";
    } else {
        return "desktop";
    }
}

function fetchTime() {  
    $.getJSON("/time", function(data){
        for (var key in data) {
            // Replace "/" with "-" to match HTML IDs
            var timezoneHTMLID = key.replace("/", "-");
            $("#" + timezoneHTMLID ).html(key + ": " + data[key]); 
        }   
    });
}


$(document).ready(function() {
    var deviceType = detectDevice();
    $("body").addClass(deviceType);
    setInterval(fetchTime, 1000);
});
