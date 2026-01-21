function Clock() {
    const now = new Date();
    let hours = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();
    if (minutes < 10) minutes = "0" + minutes;
    if (seconds < 10) seconds = "0" + seconds;
    document.getElementById("clock").textContent =
        hours + ":" + minutes + ":" + seconds;
    document.getElementById("date").textContent =
        now.toLocaleDateString("en-IN");
}

Clock();
setInterval(Clock, 1000);