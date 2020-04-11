alert("hello")
let div = document.createElement("div");
div.style.border = "1px solid black";
div.style.height = "100px";
div.style.width = "100px";
div.innerHTML = "Hello";
div.setAttribute("id", "div1");
document.body.appendChild(div);

div.addEventListener("click", function (event) {
	console.log(event);
	console.log(event.clientX);
	console.log(event.clientY);

})
