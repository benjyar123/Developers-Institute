let numArray = [];
let store1 = 0;
let store2 = 0;
let operation = "op";
let numbers = []
let operations = []

function my_f(n) {
	numArray.push(n);
	console.log(numArray.join(''));
}

function add() {
	numbers.push(parseInt(numArray.join('')));
	operations.push("add");
}

function sub() {
	store1 = parseInt(numArray.join(''));
	operation = "sub";
	numArray = [];	
	console.log(operation);
}

function mul() {
	store1 = parseInt(numArray.join(''));
	operation = "mul";
	numArray = [];	
}

function div() {
	store1 = parseInt(numArray.join(''));
	operation = "div";
	numArray = [];	
}


// function equals() {

// 	store2 = parseInt(numArray.join(''));

// 	if (operation == "add") {
// 		console.log(store1 + store2);
// 	} else if (operation == "sub") {
// 		console.log(store1 - store2);
// 	} else if (operation == "mul") {
// 		console.log(store1 * store2);
// 	} else if (operation == "div") {
// 		console.log(store1 / store2);
// 	} else if (operation == "op") {
// 		console.log(store1);
// 	}

// 	clr ()

// }

function clr() {
	console.log("**CLEAR**");
	let numArray = [];
	let store1 = 0;
	let store2 = 0;
	let operation = "op";
}


function hello () {
	console.log("checking");
	console.log(numbers);
	console.log(operations);

}









function newequals() {

	let carry = 0;

	






	for (let i = 0; i < numbers.length; i++) {
		let num1 = numbers[i];
		let num2 = numbers[i+1];

		if (operations[i] == "add") {
			carry = (num1 + num2);
			console.log(num1);
		} else if (operations[i] == "sub") {
			carry = (num1 - num2);
		} else if (operations[i] == "mul") {
			carry = (num1 * num2);
		} else if (operations[i] == "div") {
			carry = (num1 / num2);
		} 
	}
	

	

}