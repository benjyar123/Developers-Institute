

let wordArr = ["Hello", "World", "In", "A", "Frame"];
let listLength = wordArr.length; 
let space = " "

function starLine () {
	console.log("*********")
}

function wordLine (words) {

	for (let i = 0; i < listLength; i++) {
		let gap = 6 - wordArr[i].length;
	 	console.log("* " + wordArr[i] + space.repeat(gap) + "*");
}
}


starLine()
wordLine(wordArr)
starLine()




