// Exercise 1

// Ask a number to the user, and save it to a variable.
// Check if the variable is an even number
// If yes, display: “x is an even number’. Where x is the actual number of the user
// If no, display “x is not an even number’. Where x is the actual number of the user

let userNum = prompt("Please enter an integer.")

if (userNum == 0) {
	alert("That's the number 0 - which is neither odd nor even.")
}

else if (userNum % 2 == 0) {
	alert("That's an even integer.")
}

else if (userNum % 2 == 1) {
	alert("That's an odd integer.")
}

else alert("That's not an integer.")

// Exercise 2

// Create 2 variables, x and y =. Each of them has a different numeric value
// Write an if/else statement that display the bigger number

let x = prompt("Give me a number to set as variable x...")
let y = prompt("Give me a number to set as variable y...")


if (isNaN(x)||isNaN(y)) {
  alert("At least one of the variables you inputed is not a number.")
}
else if (x === y) {
	alert("x and y are equal numbers")
}
else if (x > y) {
	alert(x + " is the bigger number")
}
else if (y > x)
	alert(y + " is the bigger number")
else alert("If this alert is displayed then my IF and ELSE IF statements have not covered every eventuality.")

// Exercise 2

// Ask the user which language he speaks
// Create a few conditions :
// If he speaks French : display “Bonjour”
// If he speaks English : display “Hello”
// If he speaks Hebrew : display “Shalom”
// If he doesn’t speak none of these 3 languages: display ‘:)’

let userLang = prompt("What language do you speak?")

switch (userLang) {
  case 'French':
    alert('"Bonjour"');
    break;
  case 'English':
    alert('"Hello"');
    break;
  case 'Hebrew':
    alert('"Shalom"');
    break;
  default:
    alert(':)');
}

// Exercise 4 : The Grade Assigner

// Ask the user for his grade
// If the score is bigger than 90, console.log ‘A’
// If the score is between 80 and 90, console.log ‘B’
// If the score is between 70 and 80, console.log ‘C’
// If the score is lower than 70, console.log ‘D’

let grade = prompt("How many marks out of 100 did you get on your exam?")

switch (true) {
  case (grade >= 90):
    alert('"A"');
    break;
  case (grade >= 80):
    alert('"B"');
    break;
  case (grade >= 70):
    alert('"C"');
    break;
  case (grade >= 0):
    alert('"D"');
    break;
  
  default:
    alert("That isn't a mark out of 100!");
}