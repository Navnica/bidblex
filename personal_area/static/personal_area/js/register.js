document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementsByTagName("form")[0]
    const passwordField = document.getElementById('id_password')
    const confirmPasswordField = document.getElementById('id_confirm_password')

    form.addEventListener('submit', function (event){
        if(passwordField.value !== confirmPasswordField.value){
            confirmPasswordField.setCustomValidity('Не совпадает с паролем')
            confirmPasswordField.reportValidity()
            event.preventDefault()
        }
    })

    passwordField.addEventListener("input", function() {
        passwordField.setCustomValidity("");
        confirmPasswordField.setCustomValidity("");
    });

    confirmPasswordField.addEventListener("input", function() {
        passwordField.setCustomValidity("");
        confirmPasswordField.setCustomValidity("");
    });

})