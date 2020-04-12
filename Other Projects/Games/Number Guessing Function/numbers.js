let myNum = (Math.floor(Math.random() * 101));   
let guesses = 1

let yourGuess = prompt ("I'm thinking of a number between 0 and 100. Can you guess what it is?")

if (yourGuess == myNum) {
	alert("Congratulations you guessed my number in " + guesses + " guesses!")}
	
else if (yourGuess > myNum) {
	alert ("No that's too high.")
	newGuess()}

else if (yourGuess < myNum) {
	alert ("No that's too low.")
	newGuess()}


function newGuess () {
	let yourGuess = prompt ("Have another guess...")

	if (yourGuess == myNum) {
	alert("Congratulations you guessed my number in " + (guesses + 1) + " guesses!")}

	else if (yourGuess > myNum) {
	alert ("No that's too high.")
	guesses++;
	newGuess()}

		else if (yourGuess < myNum) {
	alert ("No that's too low.")
	guesses++;
	newGuess()}
}

