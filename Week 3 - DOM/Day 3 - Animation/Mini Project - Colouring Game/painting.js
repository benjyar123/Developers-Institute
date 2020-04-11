let colour;

for (i = 0; i <375; i++) {
	let newpixel = document.createElement("div");
	newpixel.classList.add("pixel");
	canvas.appendChild(newpixel);
	// newpixel.onclick = function() { applyColour(event); };
	newpixel.onmousedown = function() { applyColour(event); };
	// newpixel.onmouseout = function() { applyColour(event); };
	newpixel.ondragover = function() { applyColour(event); };
}

function selectColour (event) {
	colour = event.target.id;
}

function applyColour(event) {
	event.target.style.background = colour; 
}

function clearAlert(event) {
	let allPixels = document.getElementsByClassName("pixel");
	for (i = 0; i < allPixels.length; i++) {
		allPixels[i].style.background = "white";
	}
}


