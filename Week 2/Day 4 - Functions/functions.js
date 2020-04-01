alert("Exercise 1")

function exercise1 (myAge) {
	let mumAge = myAge * 2
	let dadAge = mumAge * 1.2
	alert("Your age is " + myAge + ", your mum is " + mumAge + ", and your dad is " + dadAge)
}

let userAge = prompt ("what is your age?")

exercise1 (userAge)


alert("Exercise 2")

function exercise2 (myAge) {
	return myAge * 2
}


let mum = prompt ("what is your age?")


alert("Mum's age is " + exercise2(mum))




