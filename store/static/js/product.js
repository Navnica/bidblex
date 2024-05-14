document.addEventListener('DOMContentLoaded', function() {
    const productImages = document.querySelectorAll('.image-list ul li img');
    const selectedImageContainer = document.querySelector(".selected-image img")
    const priceInput = document.getElementById("price-input");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");
    const offerButton = document.getElementById("offer")

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

    priceInput.addEventListener("input", function () {
        if(priceInput.value < 1){
            priceInput.value = 1
        }
    })

    prevButton.addEventListener("click", function() {
        if(priceInput.value - 100 < 1){
            priceInput.value = 1
        }
        else{
            priceInput.value = parseInt(priceInput.value) - 100
        }

    });

    nextButton.addEventListener("click", function() {
        priceInput.value = parseInt(priceInput.value) + 100;
    });

    prevButton.addEventListener("click", function (){
        handleButtonPress(prevButton)
    })

    nextButton.addEventListener("click", function (){
        handleButtonPress(nextButton)
    })

    offerButton.addEventListener("click", function (){
        handleButtonPress(offerButton)
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
