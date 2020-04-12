// PROBLEMS THAT STILL NEED FIXING

// -- Clicking again within set interval time messes everything up.
// -- New Game doesn't actually clear all divs from grid to start again.
// -- Need to add timer and turns counter

let emojis = ["A", "B", "C", "D", "E", "F", "G", "H", "1", "2", "3", "4", "5", "6", "7", "8"]
let letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
let numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]

let click = document.getElementById("click"); 
let ding = document.getElementById("ding"); 
let win = document.getElementById("win"); 
let newGame = document.getElementById("new"); 
let grid = document.getElementById("theGrid");
let turnsTaken = document.getElementById("turns");

let matchedPairs = 0;
let turns = 0;
let card1 = "X";
let card2 = "Y";

turnsTaken.innerText = "Turns taken: " + turns;


function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

 function reveal (event) {

 	if (card1 === "X") { 	
 	click.play();
 	card1 = event.target.id;
 	let string = card1 + ".jpg";
 	document.getElementById(card1).style.backgroundSize = "cover";
 	document.getElementById(card1).style.backgroundImage = "url('" + string + "')"; 

 	} else {
	card2 = event.target.id;
 	let string = card2 + ".jpg";
 	document.getElementById(card2).style.backgroundSize = "cover";
 	document.getElementById(card2).style.backgroundImage = "url('" + string + "')";
 	let index1 = letters.indexOf(card1) + numbers.indexOf(card1);
 	let index2 = letters.indexOf(card2) + numbers.indexOf(card2);
 	if (index1 != index2) {
 		click.play();
 		turns = turns + 1;
 		turnsTaken.innerText = "Turns taken: " + turns;
 		let turn1 = document.getElementById(card1)
 		let turn2 = document.getElementById(card2)
 		card1 = "X";
 		card2 = "Y";
 		function turnOver () {
 			turn1.style.backgroundImage = "none";
 			turn2.style.backgroundImage = "none";
  		}
  		setTimeout(turnOver, 1500);

 	} else if (index1 == index2) {
 		ding.play();
 		turns = turns + 1;
  		turnsTaken.innerText = "Turns taken: " + turns;
 		matchedPairs = matchedPairs +1;
 		card1 = "X";
 		card2 = "Y";
 		if (matchedPairs == 8) {
 			win.play();
 		}
 	}
 	}
 }

function deal () {

	turnsTaken.innerText = "Turns taken: " + turns;
	win.pause();
	win.currentTime = 0;
	newGame.play();

	let cardNumber = (grid.childElementCount);
	if (cardNumber == 0) {

	shuffle(emojis);

	for (let i = 0; i < 16; i++) {

		let card = document.createElement("div");
		card.classList.add("grid-item");
		card.id = emojis[i];
		card.onclick = function() { reveal(event); };
		grid.appendChild(card);

	}
	} else if (cardNumber > 0) {
		matchedPairs = 0;
		turns = 0;
		removeCards ();
		deal ();
	}

}

function turnOver() {
  document.getElementById(card1).style.backgroundImage = null;
  document.getElementById(card2).style.backgroundImage = null;
}


function removeCards () {
	let grid = document.getElementById("theGrid");
	for (let i = 0; i < 17; i++) {
	grid.removeChild(grid.childNodes[0]);	
	}
	

}













