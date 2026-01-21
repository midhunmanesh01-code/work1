let secret = Math.floor(Math.random() * 10) + 1;
let attempts = 3;

function checkGuess() {
    let guess = parseInt(document.getElementById("guess").value);
    if (isNaN(guess)) {
        document.getElementById("result").innerText = "Please enter a number!";
        return;
    }

    if (attempts <= 0) {
        document.getElementById("result").innerText = "Game Over!";
        return;
    }

    attempts--;

    if (guess === secret) {
        document.getElementById("result").innerText = "Win!";
    }
    else if (guess > secret) {
        document.getElementById("result").innerText = "Too High!";
    }
    else {
        document.getElementById("result").innerText = "Too Low!";
    }

    if (attempts === 0 && guess !== secret) {
        document.getElementById("result").innerText = "Game Over!";
    }
}

function restartGame() {
    secret = Math.floor(Math.random() * 10) + 1;
    attempts = 3;
    document.getElementById("guess").value = "";
    document.getElementById("result").innerText = "";

}