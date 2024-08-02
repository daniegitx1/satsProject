// script.js
window.onload = function() {
    setInterval(function() {
        const date = new Date();
        const displayDate = date.toLocaleDateString();
        const displayTime = date.toLocaleTimeString();
        document.getElementById('datetime').innerHTML = `${displayDate} ${displayTime}`;
    }, 1000); // 1000 milliseconds = 1 second
};
