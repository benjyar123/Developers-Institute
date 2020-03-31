

// Exercice 3 : Verbing
// Create a string
// If the length of this string is at least 3, it should add ‘ing’ to its end, unless it already ends in ‘ing’, in which case it should add ‘ly’ instead.
// If the string length is less than 3, it should leave it unchanged.
// Example:

//   The string is : 'swim' , your program should console.log : 'swimming'
//   The string is : ‘swimming', your program should console.log : 'swimmingly'
//   The string is : 'go' your program should console.log : 'go'

alert("Let's play VERBING!")

let string = prompt("Type in a word, and we'll make it into a verb - unless it already is one, in which case we will make it an adverb. If it's less than three letters we will do nothing to it...");

if (string.endsWith("ing")) {
	alert (string + "ly")
} else if ((string.length) >= 3) {
	alert (string + "ing")
} else alert(string)

