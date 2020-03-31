

// Exercise 1

let topColors = ["blue", "black", "purple", "grey"];

for (i = 0; i < topColors.length; i++) {

  console.log("My number " + (i+1) + " colour is " + topColors[i]);

 
}

// Exercise 2

do {
   yourNumber = prompt("Give me a number that is smaller than 10...")
}
while (yourNumber > 10);

// Exercise 3

let people = ["Greg", "Mary", "Devon", "James"];

people.splice(0,1);

people.splice(2,1, "Jason");

people.push("Benjy")

for (let i = 0; i < people.length; i++) {

	console.log(people[i])
	if (people[i] === "Mary") { 
      break;
    }
}

let peopleCopy = people.slice(1, 3);

console.log(peopleCopy)

console.log(people.indexOf("Mary"));
console.log(peopleCopy.indexOf("Mary"));

last = people[people.length - 1];

console.log(last)

// Exercise 4

let age = [20,5,12,43,98,55];

let ageSum = age => age.reduce((a,b) => a + b, 0)

console.log(ageSum(age))













