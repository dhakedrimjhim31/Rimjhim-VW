function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({
        behavior: "smooth"
    });
}

function submitForm(event) {
    event.preventDefault();
    alert("Thank you for your order! We will contact you soon 🌸🎂");
}