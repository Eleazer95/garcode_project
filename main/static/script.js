const hamburger=document.querySelector('.hamburger');
const navLinks=document.querySelector('.nav-links');

hamburger.addEventListener('click',()=>{
    navLinks.classList.toggle('active');;
});


// script.js

// Show the back-to-top button when scrolling down
window.onscroll = function() {
    var backToTopButton = document.getElementById("back-to-top");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        backToTopButton.style.display = "block";
    } else {
        backToTopButton.style.display = "none";
    }
};

// Scroll to the top when the back-to-top button is clicked
document.getElementById("back-to-top").onclick = function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};