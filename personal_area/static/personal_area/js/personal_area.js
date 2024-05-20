document.addEventListener("DOMContentLoaded", function() {
    const sideMenuButtons = document.querySelectorAll("#side-menu ul li");
    const pages = {}
    document.querySelectorAll("#page-block .page").forEach(page => {
        pages[page.id] = page;
    });

    sideMenuButtons.forEach(button => {
        button.addEventListener("click", function() {
            for (let pageKey in pages) {
                if(pageKey !== button.id){
                    pages[pageKey].classList.add("hidden")
                }
                else{
                    pages[pageKey].classList.remove("hidden")
                }
            }
        })
    })
})