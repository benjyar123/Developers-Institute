// DECLARATIONS

function verse (bottles, take, itThem) {
	console.log(bottles + " bottles of beer on the wall,");
	console.log(bottles + " bottles of beer....");
	console.log("Take " + take + " down, pass " + itThem + " around,");
	console.log((bottles-take) + " bottles of beer on the wall!");
	console.log("*************************");
}

function endSong () {
	console.log("We seem to have run out of beers.....pub?")
}

function song () {

	let bottles = prompt("How many bottles?");
	let take = 1
	let itThem = "it"

	for (let i = 0; true; i++) {

		if (bottles == 0) {
		endSong();
		break;
		}

		if (take == 1) {
			itThem = "it";
		} else {itThem = "them"};

		if ((bottles - take) < 1) {
			take = bottles;
		}

		verse(bottles, take, itThem);

		bottles = bottles - take;
		take = take + 1;
	}
}

// EXECUTIONS

song()