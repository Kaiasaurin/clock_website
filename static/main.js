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
            // Construct timezone string here carefully
            var timezoneString = key;
            if (!['Etc-GMT', 'Etc-GMT+0', 'Etc-GMT-0'].includes(key)) {
                timezoneString = key.replace("-", "/");
            }
            $("#" + key).html(timezoneString + ": " + data[key]); 
        }   
    });
}

$(document).ready(function() {
    var deviceType = detectDevice();
    $("body").addClass(deviceType);
    setInterval(fetchTime, 1000);
});
