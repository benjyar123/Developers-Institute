let innings = document.getElementById("innings");
let score = document.getElementById("score");
let inningsSoFar = innings.innerHTML;	
let balls = 0;

let Aggressive = [".",".",".",".",".",".",1,1,1,2,2,2,4,4,4,4,4,6,6,6,6,6,"W","W","W"];
let Attacking = [".",".",".",".",".",".",".",".",".",1,1,1,1,2,2,2,2,3,3,3,4,4,4,4,6,6,"W","W"];
let Positive = [".",".",".",".",".",".",".",".",".",".",1,1,1,1,1,1,1,2,2,2,2,2,3,3,4,4,4,"W","W"];
let Cautious = [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",1,1,1,1,1,1,1,2,2,2,4,"W"];
let Defensive = [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",1,1,1,1,1,2,4,"W"];

function shotOutcome(shotChosen) {
return shotChosen[Math.floor(Math.random()*shotChosen.length)];    
}

function delivery (event) {

	
	let shotChosen = event.target.innerHTML;
	inningsSoFar = innings.innerHTML;
	balls = (inningsSoFar.length / 2) + 1;

	if (shotChosen === "Aggressive") {
		let runs = shotOutcome(Aggressive);
		innings.innerText = inningsSoFar + " " + runs;
		if (runs === "W") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
			wicket ();
		} else if (runs === ".") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
		} else {
			score.innerHTML = (parseInt(score.innerHTML) + runs) + " (" + balls + ")";
		}
	} else if (shotChosen === "Attacking") {
		let runs = shotOutcome(Attacking);
		innings.innerText = inningsSoFar + " " + runs;
		if (runs === "W") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
			return wicket ();
		} else if (runs === ".") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
		} else {
			score.innerHTML = (parseInt(score.innerHTML) + runs) + " (" + balls + ")";
		}
	} else if (shotChosen === "Positive") {
		let runs = shotOutcome(Positive);
		innings.innerText = inningsSoFar + " " + runs;
		if (runs === "W") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
			return wicket ();
		} else if (runs === ".") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
		} else {
			score.innerHTML = (parseInt(score.innerHTML) + runs) + " (" + balls + ")";
		}
	} else if (shotChosen === "Cautious") {
		let runs = shotOutcome(Cautious);
		innings.innerText = inningsSoFar + " " + runs;
		if (runs === "W") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
			return wicket ();
		} else if (runs === ".") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
		} else {
			score.innerHTML = (parseInt(score.innerHTML) + runs) + " (" + balls + ")";
		}
	} else if (shotChosen === "Defensive") {
		let runs = shotOutcome(Defensive);
		innings.innerText = inningsSoFar + " " + runs;
		if (runs === "W") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
			return wicket ();
		} else if (runs === ".") {
			score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
		} else {
			score.innerHTML = (parseInt(score.innerHTML) + runs) + " (" + balls + ")";
		}
	}

	





}



function wicket () {

	alert("HOWZAAAAAAAT?!?!")

	let rand = Math.random();
	if (rand < 0.2) {
		alert("Not out!! Umpire says it's drifting down leg. Play on...");
		innings.innerText = inningsSoFar + " " + ".";
		score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
	} else if (rand < 0.4) {
		alert("Not out!! There's nothing on snicko. Play on...");
		innings.innerText = inningsSoFar + " " + ".";
		score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
	} else if (rand < 0.6) {
		alert("Not out!! Bowler's overstepped, no ball! Play on...");
		innings.innerText = inningsSoFar + " " + ".";
		score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
	} else {
	innings.innerText = inningsSoFar + " " + "W";
	score.innerHTML = parseInt(score.innerHTML) + " (" + (balls) + ")";
	alert("***WICKET*** Got him!!!\n\nYour final score is " + score.innerHTML);
	reset();
	}
}


function reset () {
	innings.innerText = "";
	score.innerHTML = "0 (0)";
}