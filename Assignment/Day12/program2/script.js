const bulbImage = document.getElementById("bulbImage");
const onButton = document.getElementById("onButton");
const offButton = document.getElementById("offButton");

onButton.addEventListener("click", function () {

    bulbImage.src = "https://www.w3schools.com/js/pic_bulbon.gif";
    bulbImage.classList.add("glow");

});

offButton.addEventListener("click", function () {

    bulbImage.src = "https://www.w3schools.com/js/pic_bulboff.gif";
    bulbImage.classList.remove("glow");

});