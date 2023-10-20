
console.log(1);
function animate_stars(star_element, div) {
    const stars = div.children;
    for (let i = 0; i < stars.length; i++) {
        stars[i].classList.remove("bi-star")
        stars[i].classList.add("bi-star-fill");
        if (stars[i] == star_element) {
            break;
        }
    }
} 

function hide_animation(div) {
    const stars = div.children;
    for (let i = 0; i < stars.length; i++) {
        stars[i].classList.remove("bi-star-fill");
        stars[i].classList.add("bi-star");
    }
}