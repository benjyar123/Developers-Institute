let array = ["Banana", "Apples", "Oranges", "Blueberries"];
let bad_banana = array.indexOf("Banana");
array.splice(bad_banana, 1)

array.sort();
array.push("Kiwi")

let bad_apples = array.indexOf("Apples");
array.splice(bad_apples, 1)

array.reverse()


document.write(array)

let array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let nested_array = array2[1];

document.write(nested_array[1])
