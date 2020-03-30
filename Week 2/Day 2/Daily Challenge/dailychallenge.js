let sentence = prompt("Type a sentence")

let notPosition = sentence.indexOf("not")
let badPosition = sentence.indexOf("bad")


if (notPosition < badPosition) {
let newSentence = sentence.replace(" not", "")
newSentence = newSentence.replace("bad", "good")
alert(newSentence)
} else alert(sentence)

// Daily challenge : Not Bad
// Create a string that has the word “not” and “bad” inside
// Create another variable that should find the first appearance of the substring ‘not’ and ‘bad’.
// If the ‘bad’ follows the ‘not’, then it should replace the whole ‘not’…’bad’ substring with ‘good’ than console.log the result.
// If it doesn’t find ‘not’ and ‘bad’ in the right sequence (or at all), just console.log the original sentence.
// Example:

//   Your string is : 'This dinner is not that bad!', the result is : 'This dinner is good!'
//   Your string is : 'This movie is not so bad!' the result is : 'This movie is good!'
//   Your string is : 'This dinner is bad!' the result is : 'This dinner is bad!'**