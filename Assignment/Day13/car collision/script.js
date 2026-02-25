let car1 = document.getElementById("car1");
let car2 = document.getElementById("car2");
let explosion = document.getElementById("explosion");
let message = document.getElementById("message");

let car1Pos = 0;
let car2Pos = 0;

let car1Interval = null;
let car2Interval = null;

let crashed = false;

// -------- START BUTTONS --------

function startCar1(){
    if(!car1Interval){
        car1Interval = setInterval(moveCar1, 20);
    }
}

function startCar2(){
    if(!car2Interval){
        car2Interval = setInterval(moveCar2, 20);
    }
}

// -------- CAR MOVEMENT --------

function moveCar1(){
    if(crashed) return;
    car1Pos += 4;
    car1.style.left = car1Pos + "px";
    checkCrash();
}

function moveCar2(){
    if(crashed) return;
    car2Pos += 4;
    car2.style.right = car2Pos + "px";
    checkCrash();
}

// -------- COLLISION DETECTION --------

function checkCrash(){

    let rect1 = car1.getBoundingClientRect();
    let rect2 = car2.getBoundingClientRect();

    if(rect1.right >= rect2.left){

        crashed = true;

        clearInterval(car1Interval);
        clearInterval(car2Interval);

        crashEffect(rect1, rect2);
    }
}

// -------- CRASH EFFECT --------

function crashEffect(rect1, rect2){

    // Slight bounce
    car1.style.left = (car1Pos - 8) + "px";
    car2.style.right = (car2Pos - 8) + "px";

    // Calculate exact collision center
    let roadRect = document.getElementById("road").getBoundingClientRect();

    let collisionX = (rect1.right + rect2.left) / 2 - roadRect.left;
    let collisionY = (rect1.top + rect1.bottom) / 2 - roadRect.top;

    explosion.style.display = "block";
    explosion.style.left = (collisionX - 35) + "px";
    explosion.style.top = (collisionY - 35) + "px";

    // Flash effect
    document.getElementById("road").style.background = "red";
    setTimeout(()=>{
        document.getElementById("road").style.background =
        "linear-gradient(#87CEEB 50%, #333 50%)";
    },200);

    // Rotate cars
    car1.style.transform = "rotate(15deg)";
    car2.style.transform = "rotate(-15deg)";

    setTimeout(fallCars, 800);
}

// -------- FALL EFFECT --------

function fallCars(){

    let fallTop = 120;

    let fallInterval = setInterval(()=>{

        if(fallTop >= 210){
            clearInterval(fallInterval);
            showMessage();
            return;
        }

        fallTop += 4;

        car1.style.top = fallTop + "px";
        car2.style.top = fallTop + "px";

        // Move explosion down with cars
        explosion.style.top =
            (parseInt(explosion.style.top) + 4) + "px";

    },20);
}

// -------- MESSAGE --------

function showMessage(){

    message.innerHTML =
    "⚠ Accident happened. Protect your future. Take Insurance.";
    message.style.color = "red";
    message.style.fontSize = "22px";
}