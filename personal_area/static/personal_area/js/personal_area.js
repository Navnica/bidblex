document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById("contact-data-add-button");
    const form = document.getElementById("contact-data-form");

    button.addEventListener("click", function (){
        form.classList.remove("hidden")
        button.classList.add("hidden")
    })

})