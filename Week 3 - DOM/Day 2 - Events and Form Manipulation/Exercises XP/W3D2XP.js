let article = document.querySelector("article");
let paragraphs = document.querySelectorAll("p");
paragraphs[3].remove();

function RemoveHead() { 
    h2.remove();      	
} 

function HidePara() { 
    paragraphs[0].style.visibility = "hidden";      	
} 

let h2 = document.querySelector("h2");
h2.addEventListener("click", RemoveHead);

let random = Math.floor(Math.random() * 100);
let h1 = document.querySelector("h1").style.fontSize = random + "px";

paragraphs[0].addEventListener("click", HidePara);

function FadePara() { 
    paragraphs[1].style.opacity = 0;
	paragraphs[1].style.transition = "opacity 2000ms";     	
} 

paragraphs[1].addEventListener("click", FadePara);

let answerTable = document.createElement("table");

document.body.appendChild(answerTable);

let topRow = document.createElement("tr");
answerTable.appendChild(topRow);
let answersRow = document.createElement("tr");
answerTable.appendChild(answersRow);

let colHead1 = document.createElement("th");
let colHead2 = document.createElement("th");
colHead1.innerText="Name";
colHead2.innerText="Feedback";

let userName = document.createElement("td");
let userFeedback = document.createElement("td");
userName.innerText="get input";
userFeedback.innerText="get input";


topRow.appendChild(colHead1);
topRow.appendChild(colHead2);

answersRow.appendChild(userName);
answersRow.appendChild(userFeedback);

// STUCK ON LAST BIT

let user = document.getElementById("input1");
let feedback = document.getElementById("input2");
console.log(user.value);


user.addEventListener("change", inputName);
feedback.addEventListener("input", inputFeedback);

function inputName () {
	userName.innerText= user.value;
}

function inputFeedback () {
	userFeedback.innerText= feedback.value;
}


