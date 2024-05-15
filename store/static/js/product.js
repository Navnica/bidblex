document.addEventListener('DOMContentLoaded', function() {
    const productImages = document.querySelectorAll('.image-list ul li img');
    const selectedImageContainer = document.querySelector(".selected-image img")
    const priceInput = document.getElementById("price-input")
    const priceOfferButtons = document.querySelectorAll('.price-offer-button');
    const offerButton = document.getElementById("offer-button")

    productImages[0].classList.add('selected')
    selectedImageContainer.src = productImages[0].src

    productImages.forEach(function(img) {
        img.addEventListener('click', function(event) {
            productImages.forEach(function(img) {
                img.classList.remove('selected');
            });

            this.classList.add('selected');
            selectedImageContainer.src = this.src
        });
    });

    offerButton.addEventListener("click", function (){handleButtonPress(offerButton)})

    priceInput.addEventListener("input", function () {
        if(priceInput.value < 1){
            priceInput.value = 1
        }
    })

    priceOfferButtons.forEach(function (button){
        button.addEventListener("click", function () {handleButtonPress(button)})

        if(button.value === "+"){
            button.addEventListener("click", function (){
                priceInput.value = parseFloat(priceInput.value) + 100
            })
        }
        else if(button.value === "-"){
            button.addEventListener("click", function (){
                priceInput.value = parseFloat(priceInput.value) - 100
                if(parseFloat(priceInput.value) - 100 < 1){
                    priceInput.value = 1
                }
            })
        }
    })

    function handleButtonPress(button) {
        button.addEventListener("mousedown", function() {
            button.classList.add("pressed");
        });

        button.addEventListener("mouseup", function() {
            button.classList.remove("pressed");
        });

        button.addEventListener("mouseleave", function() {
            button.classList.remove("pressed");
        });
    }
});
