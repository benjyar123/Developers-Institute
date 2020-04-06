// alert("Is this thing on?")

// // accessing in array

// let color = ["blue", "red", "green"]
// document.write (color[1])

// // array access element with index
// // object access element with key name
// // object is unordered
// // objects keys can be properties or methods

// let person = {
//   firstName: "John",
//   lastName: "Doe",
//    eat : function () {
//         document.write("I love chocolate")}
// };

// alert(person.firstName + " has " + person.eyeColor + " eyes.")


// person.eat()



// // document.write([person])

// // person.firstName = "Sarah"
// // person.eyeColor = "blue"

// // Exercise 1

let object = {
	username: "Popeye",
	password: "spinach",
}

// let database = [object]


// let newsfeed = [
//   {
//     username:"Alvin",
//     timeline:"example1"
//   },
//   {
//     username:"Simon",
//     timeline:"example1"
//   },
//   {
//     username:"Theodore",
//     timeline:"example1"
//   }
// ];

// console.log(database)
// console.log(newsfeed)

// console.log(newsfeed[1]["username"])

// exercise 2


// for (i = 0; i < 16; i++) {
// 	if (i % 2 == 0) {
// 	document.write(i + "is even. ");}
// 	else if (i % 2 != 0) {
// 	document.write(i + "is odd. ");}
// }


// for (let x in object) {
// 	alert(object[x])
// }


// for (let x in object) {
// 	alert(x)
// }

// let person = {
// fname:"John", 
// lname:"Doe", 
// age:25,
// friends:["Lea", "Joanna", "Mark"]};



// for (let i of person.friends) {
//    console.log(i); // logs blue, yellow, red
// }


// for (let x in person) {
// 	console.log(person[x])
// }

// while loops

// while (boolean condition)
// {
//    loop statements...
// }

// while loop

// let n = 0;
// while (n < 5) {
//   n++;
//   console.log(n)
// }

// // do while loop

// // do
// // {
// //     statements..
// // }
// // while (condition);

// let i = 0;
// do {
//   console.log("The number is " + i)
//   i++;
// }
// while (i < 10);

// KEY DIFFERENCE IS THAT DO WHILE LOOPS ARE EXECUTED AT LEAST ONCE REGARDLESS


// 


//  return str.charAt(index).toUpperCase() === str.charAt(index);
//     }
// console.log(isUpperCaseAt('Js STRING EXERCISES', 1));



let names = ["john", "sarah", 23, "Rudolf", 34]

for (let i = 0; i < names.length; i++) 

	if (isNaN(names[i])) {

	console.log(names[i])
}


// Exercise 3
// var names= ["john", "sarah", 23, "Rudolf",34]

// 1. Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.