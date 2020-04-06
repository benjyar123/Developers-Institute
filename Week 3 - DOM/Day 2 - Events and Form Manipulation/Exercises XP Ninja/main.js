function calculateTip () {

	let billAmt = document.getElementById("billamt");
	let serviceQual = document.getElementById("serviceQual");
	let numOfPeople = document.getElementById("peopleamt");

	if (serviceQual.value == 0) {
		alert("Please rate the service quality");
		return
	}

	if (numOfPeople.value == 0) {
		numOfPeople.value = 1;
		HideEach ();
	}

	let total = (billAmt.value * serviceQual.value) / numOfPeople.value;
	let fixedTotal = total.toFixed(2);
	let totalIncTip = document.getElementById("tip");
	totalIncTip.innerHTML = fixedTotal

}


let calculateButton = document.getElementById("calculate");

calculateButton.addEventListener("click", calculateTip);


function HideEach() { 
	let each = document.getElementById("each");
    each.style.visibility = "hidden";      	
} 



