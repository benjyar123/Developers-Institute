function dragStart(event) {
event.dataTransfer.setData("text", event.target.id);
// let duplicate = document.createElement("div");
// duplicate.setAttribute("class", "letter");
// duplicate.innerText = "A";
// let location = document.getElementById("letterBox");
// location.appendChild(duplicate);
// // give letter elements a value
}

function allowDrop(event) {
event.preventDefault(); 
}

function dragDrop(event) {
let data = event.dataTransfer.getData("text");  
let chosenLetter = document.getElementById(data);
event.target.appendChild(chosenLetter);
let x = event.clientX;
let y = event.clientY;
// let shiftX = event.clientX - chosenLetter.getBoundingClientRect().left;
// let shiftY = event.clientY - chosenLetter.getBoundingClientRect().top;
chosenLetter.style.left = (x-31) + "px";
chosenLetter.style.top = (y-31) + "px";
chosenLetter.style.position = "absolute";
}

