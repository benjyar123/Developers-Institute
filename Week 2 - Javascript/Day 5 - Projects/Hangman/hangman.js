// Declarations

let word = prompt("Choose a secret word for your partner to guess...");
let display = "*".repeat(word.length);

function guess (word, display, turns) {

let letter = prompt(turns + " turns left!!!\n\nGuess a letter...\n\n" + display);

	for (let i = 0; i < word.length; i++) {
		if (letter == word.charAt(i)) {
			let str1 = display.slice(0, i);
			let str2 = display.slice(i+1);
			display = str1 + letter + str2;
		} 
	}

	if (display == word) {
		alert("CONGRATULATIONS!!!\n\nYou guessed that the word was...\n\n" + word + "!!!!");
	} else if (turns == 1) {
		alert("You have 0 turns left and you have lost the game :-(\n\n" + display + "\n\n" + word);
	} else {
		guess (word, display, (turns-1));
	}
}


// EXECUTIONS


guess (word, display, 10)





