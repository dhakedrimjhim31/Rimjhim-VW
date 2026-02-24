const car = document.getElementById("car");
const moveBtn = document.getElementById("moveBtn");

let position = 0;

moveBtn.addEventListener("click", function () {

    position += 80;  // move 80px per click

    if (position > window.innerWidth - 300) {
        position = 0;  // reset when reaching end
    }

    car.style.left = position + "px";
});