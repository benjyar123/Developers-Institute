

// let Mercury = document.createElement("div");
// let Venus = document.createElement("div");
// let Earth = document.createElement("div");
// let Mars = document.createElement("div");
// let Jupiter = document.createElement("div");
// let Saturn = document.createElement("div");
// let Uranus = document.createElement("div");
// let Neptune = document.createElement("div");

let body = document.getElementsByTagName("body");

let planetList = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

for (planets of planetList) {
	let planet = document.createElement("div");
	planet.innerHTML = planets;
	body[0].appendChild(planet);
	planet.setAttribute("class", "planet");
	planet.setAttribute("id", planets);
}

document.getElementById("Mercury").style.backgroundColor = "red"
document.getElementById("Venus").style.backgroundColor = "white"
document.getElementById("Earth").style.backgroundColor = "blue"
document.getElementById("Mars").style.backgroundColor = "brown"
document.getElementById("Jupiter").style.backgroundColor = "orange"
document.getElementById("Saturn").style.backgroundColor = "yellow"
document.getElementById("Uranus").style.backgroundColor = "turquoise"
document.getElementById("Neptune").style.backgroundColor = "blue"






















