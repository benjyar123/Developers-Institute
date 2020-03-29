let input1 = parseInt(prompt('Pick a number'));
let input2 = parseInt(prompt('Pick another number'));
let operator = prompt('Pick an operator: + , - , * , /');

let answer; 

if (operator=="+") {
	answer = input1 + input2;
}
else if (operator=="-") {
	answer = input1 - input2;
}
else if (operator=="*") {
	answer = input1 * input2;
}
else if (operator=="/") {
	answer = input1 / input2;
}
else {
	answer = "You have not selected an available option. Reload page."
}

alert(answer)

