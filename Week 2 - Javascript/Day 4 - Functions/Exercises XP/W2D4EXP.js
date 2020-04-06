// // Exercise 1

function checkDriverAge(age) {

	if (age < 18) {
	alert("Sorry, you are too yound to drive this car. Powering off");
	} else if (age > 18) {
	alert("Powering On. Enjoy the ride!");
	} else if (age === 18) {
	alert("Congratulations on your first year of driving. Enjoy the ride!");
	}

}

checkDriverAge(5)

checkDriverAge(18)

checkDriverAge(92)


// Exercise 2

amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}


function checkBasket(item) {

	if (item in amazonBasket) {
	alert("You have " + amazonBasket[item] + " " + item + " in your basket.");
	} else {
	alert("You do not have any " + item + " in your basket.");
	}
}

checkBasket("glasses")
checkBasket("books")
checkBasket("floss")
checkBasket("cars")

// or could put a user input instead to search for specific items

// Exercise 3

let shoppingList = ["banana", "orange", "apple", "banana", "orange", "apple", "pear", "pear", "blueberry"]

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5, 
    "blueberry":10
} 

console.log("Stock BEFORE myBill function")
console.log(stock)  

function myBill () {

let listLength = shoppingList.length;
let unavailable = []
let total = 0

alert("Your shopping list is...\n\n" + shoppingList)

for (let i = 0; i < listLength; i++) {
	if (stock[shoppingList[i]] > 0) {
    total = total + prices[shoppingList[i]];
    stock[shoppingList[i]]--;}
    else if (stock[shoppingList[i]] == 0) {
    unavailable.push(shoppingList[i]);
    shoppingList.splice(i, 1);
}
}
alert("The following items were unavailable;\n\n" + unavailable)
alert("You have bought;\n\n" + shoppingList)
alert("That will be " + total + " shekels please!")
}

myBill()

console.log("Stock AFTER myBill function")
console.log(stock)   

// Exercise 4


hotel_cost = (nights) => {
  return nights * 140;
}

rental_car_cost = (days) => {
  return days * 40;
}

function plane_ride_cost (city) {

	if (city == "London") {
		return 183;
	}
	else if (city == "Paris") {
		return 220;
	}
	else {
		return 300;
	}
	
}

total_holiday_cost = (hotel, flight, car) => {
  return hotel_cost(hotel) + plane_ride_cost(flight) + rental_car_cost(car);
}

userHotelNights = prompt("How many nights do you want to stay in a hotel?")
userCity = prompt("Where do you want to go?")
userCarDays = prompt("How many days do you want to rent a car for?")

alert("Hotel will cost: " + hotel_cost(userHotelNights))
alert("Flight will cost: " + plane_ride_cost(userCity))
alert("Car will cost: " + rental_car_cost(userCarDays))

Total = total_holiday_cost(userHotelNights, userCity, userCarDays)

alert("Your total holiday cost will be: " + Total)
