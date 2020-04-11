let drumKeys = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
let drumNames = ["boom", "clap", "hihat", "kick", "openhat", "ride", "snare", "tink", "tom"]

function click (event) {
	let i = drumKeys.indexOf(event.target.id);
	let drumName = document.getElementById(drumNames[i]);
	let drumSound = document.getElementById(drumName);
	drumName.play();
} 

for (let i = 0; i < drumKeys.length; i++) {
	let key = document.createElement("div");
	key.setAttribute("id", drumKeys[i]);
	key.innerHTML = drumKeys[i];
	key.onclick = function() { click(event); };
	document.body.appendChild(key);
}


for (let i = 0; i < drumKeys.length; i++) {
let keySound = document.createElement("audio");
	keySound.setAttribute("id", drumNames[i]);
	keySound.setAttribute("src", (drumNames[i] + ".wav"));
	document.body.appendChild(keySound);	
}

