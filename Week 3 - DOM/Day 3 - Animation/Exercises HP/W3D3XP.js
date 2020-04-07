function myMove() {
	let redBox = document.getElementById("animate");
	let pos = 0;
	let id = setInterval(function(){
		if (pos == 350) {
			clearInterval(id);
		} else {
			pos++;
			redBox.style.left = pos + "px";
		}
	}, 5);
}

function dragStart(event) {
event.dataTransfer.setData("text", event.target.id);
}

function allowDrop(event) {
event.preventDefault(); 
}

function dragDrop(event) {
let data = event.dataTransfer.getData("text");  
let box = document.getElementById(data)
event.target.appendChild(box);
}