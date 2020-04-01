let originalList = [1,2,3,3,3,3,4,5];
let newList = [];

function uniqueElementsList (list) {
	for (let i = 0; i < list.length; i++) {
		if (newList.includes(list[i]) == false) {
			newList.push(list[i]);
		}
	}
	return newList
}
console.log(uniqueElementsList(originalList))
		



