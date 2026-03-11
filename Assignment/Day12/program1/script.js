let count = 0;
let fontSize = 20;

const message = document.getElementById("message");
const button = document.getElementById("btn");
const gifContainer = document.getElementById("gifContainer");

const colors = ["red", "blue", "green", "purple", "orange", "pink"];

button.addEventListener("click", function () {

    count++;

    if (count < 4) {

        // Increase font size
        fontSize += 20;
        message.style.fontSize = fontSize + "px";

        // Change color randomly
        let randomColor = colors[Math.floor(Math.random() * colors.length)];
        message.style.color = randomColor;

    } else {

        // Remove previous styles
        message.removeAttribute("style");

        // Remove previous content
        message.innerHTML = "🎉 Happy Birthday 🎉";

        // Add birthday class
        message.classList.add("birthday-style");

        // Show GIF
        gifContainer.style.display = "block";

        // Hide button after final message
        button.style.display = "none";
    }
});