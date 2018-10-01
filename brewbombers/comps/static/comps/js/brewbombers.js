// Javascript goes here for the BrewBombers site.

// Add judge modal form javascript.
// Get the form itself.
var modal_form = document.getElementById('add-judge-form');

// Get the button that opens the modal
var btn = document.getElementById("add-judge");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("add-judge-close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
    console.log('hit');
    modal_form.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal_form.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal_form) {
        modal_form.style.display = "none";
    }
}
