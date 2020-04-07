let banner = document.getElementById('banner');

// banner.style.visibility = "hidden";  

// banner.innerHTML = "Hello";

// function sayHi() {
  banner.style.visibility = "visible";
  banner.style.color = "red";
  banner.style.background = "black";
  banner.style.fontSize = "50px";
// }

// setTimeout(sayHi, 3000)



let myVar = setInterval(myTimer, 1000);

let seconds = 11;

function myTimer() {
  seconds = seconds-1;
  if (seconds == 0) {
  	banner.innerHTML = "The sale is now CLOSED!!!!"
  	clearInterval(myVar);
  } else {
  	banner.innerHTML = "The sale closes in " + seconds + " seconds!!!";
  }
}


