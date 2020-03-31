// EXERCISE 1

let family = {
	name: "Simpsons",
	members: 5,
	town: "Springfield",
	pets: 1
};

for (let x in family) {
  console.log(x);
}

for (let x in family) {
  console.log(family[x]); 
}

// EXERCISE 2

let building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}

console.log(building.number_levels) 
// Display 4
console.log(building.number_of_apt_by_level["1"]) 
// Display 3
console.log(building.number_of_apt_by_level["3"])
// Display 9


for (let x in building.number_of_apt_by_level) {


  if (x == ("1"||"3") ) {

  	console.log(building.number_of_apt_by_level[x])}

}

// Stuck on this one. Tried just console-logging first before attempted summing, but can't even get that to work.



console.log("Second tennant is " + building.name_of_tenants[1] + " and he has " + building.number_of_rooms_and_rent.Dan[0] + " rooms in his apartment.")

// Displays Second tennant is Dan and he has 4 rooms in his apartment.



let SarahRent = building.number_of_rooms_and_rent.Sarah[1]
let DavidRent = (building.number_of_rooms_and_rent.David[1])
let DanRent = (building.number_of_rooms_and_rent.Dan[1])

alert("Dan's rent at the beginning of this exercise is " + DanRent)

if ((SarahRent + DavidRent) > DanRent) {
	alert("Dan is being undercharged!! Dan's rent will be increased by the difference between his current rent and the sum of Sarah and David's rent. Life is tough sometimes.")
	DanRent = DavidRent + SarahRent
	building.number_of_rooms_and_rent.Dan[1] = DanRent
	alert("Dan's rent has now been changed inside the building database.")
}

// EXERCISE 3


let hero1 = {
  fullName: "Spiderman",
  mass: 75,
  height: 1.75,
  BodyMassIndex: function() {
     alert(this.mass / (Math.pow(this.height, 2)));
  }
};

let hero2 = {
  fullName: "Batman",
  mass: 90,
  height: 1.85,
  BodyMassIndex: function() {
     alert(this.mass / (Math.pow(this.height, 2)));
  }
};



hero1.BodyMassIndex()
hero2.BodyMassIndex()


