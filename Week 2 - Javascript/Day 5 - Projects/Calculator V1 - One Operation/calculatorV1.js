// THIS ONLY WORKS FOR OPERATIONS FITTING THIS STRUCTURE;

// MULTIPLE DIGIT NUMBER ---- OPERATOR ---- MULTIPLE DIGIT NUMBER --- EQUALS


let numArray = [];
let store1 = 0;
let store2 = 0;
let operation = "op";

function my_f(n) {
	numArray.push(n);
	console.log(numArray.join(''));
}

function add() {
	store1 = parseInt(numArray.join(''));
	operation = "add";
	numArray = [];	
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


function equals() {

	store2 = parseInt(numArray.join(''));

	if (operation == "add") {
		console.log(store1 + store2);
	} else if (operation == "sub") {
		console.log(store1 - store2);
	} else if (operation == "mul") {
		console.log(store1 * store2);
	} else if (operation == "div") {
		console.log(store1 / store2);
	} else if (operation == "op") {
		console.log(store1);
	}

	clr ()

}

function clr() {
	console.log("**CLEAR**");
	let numArray = [];
	let store1 = 0;
	let store2 = 0;
	let operation = "op";
}







