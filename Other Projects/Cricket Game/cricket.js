function shotOutcome(shotChosen)
{
return shotChosen[Math.floor(Math.random()*shotChosen.length)];    
}


let runs = 0
let balls = 0
let Aggressive = [0,0,0,1,1,1,2,2,2,4,4,4,4,4,6,6,6,6,6,"W","W","W","W","W"];
let Attacking = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,4,4,4,4,6,6,"W","W","W"];
let Positive = [0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,3,3,4,4,4,"W","W"];
let Cautious = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,4,"W"];
let Defensive = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,4,"W"];


alert("Let's play cricket!! How many runs can you score?\n\nPlaying more aggressively will let you score more quickly, but there is a higher chance of you losing your wicket...")

nextShot()
function nextShot(){

let yourShot = prompt("Current score: " + runs + " (" + balls + ")\n\n" + "Select shot aggression level:\n\nDefensive (1)\nCautious (2)\nPositive (3)\nAttacking (4)\nAggressive (5)")

if (yourShot == "1") {
	let thisShot = (shotOutcome(Defensive));
	if (thisShot != "W") {
		runs = runs + thisShot;
		balls++;
		alert(thisShot + " runs!");
		nextShot();
	}
	else if (thisShot = "W") {
		balls++;
		alert("WICKET!!!\n\n Your final score is " + runs + " off of " + balls + " balls.")
	}


}

if (yourShot == "2") {
	let thisShot = (shotOutcome(Cautious));
	if (thisShot != "W") {
		runs = runs + thisShot;
		balls++;
		alert(thisShot + " runs!");
		nextShot();
	}
	else if (thisShot = "W") {
		balls++;
		alert("WICKET!!!\n\n Your final score is " + runs + " off of " + balls + " balls.")
	}


}
if (yourShot == "3") {
	let thisShot = (shotOutcome(Positive));
	if (thisShot != "W") {
		runs = runs + thisShot;
		balls++;
		alert(thisShot + " runs!");
		nextShot();
	}
	else if (thisShot = "W") {
		balls++;
		alert("WICKET!!!\n\n Your final score is " + runs + " off of " + balls + " balls.")
	}


}
if (yourShot == "4") {
	let thisShot = (shotOutcome(Attacking));
	if (thisShot != "W") {
		runs = runs + thisShot;
		balls++;
		alert(thisShot + " runs!");
		nextShot();
	}
	else if (thisShot = "W") {
		balls++;
		alert("WICKET!!!\n\n Your final score is " + runs + " off of " + balls + " balls.")
	}


}
if (yourShot == "5") {
	let thisShot = (shotOutcome(Aggressive));
	if (thisShot != "W") {
		runs = runs + thisShot;
		balls++;
		alert(thisShot + " runs!");
		nextShot();
	}
	else if (thisShot = "W") {
		balls++;
		alert("WICKET!!!\n\n Your final score is " + runs + " off of " + balls + " balls.")
	}


}


}
