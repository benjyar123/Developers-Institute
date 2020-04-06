// Made a menu generator as a variation on the madlibs idea

let dinnerButton = document.getElementById('dinner-button');

let userProtein = document.getElementById("protein");
let userVegetable = document.getElementById("vegetable");
let userFruit = document.getElementById("fruit");

let cookingAdjective = ["deep-fried", "roasted", "boiled", "barbecued", "raw", "chopped", "pickled", "microwaved", "frozen", "curried", "sauteed", "battered"];
let cookingNoun = ["sandwich", "pancake", "risotto", "salad", "fajita", "curry", "kebab", "omelette", "lasagne", "pizza", "burger", "stir-fry"];
let dessertType = ["ice cream", "cake", "sorbet", "juice", "smoothie", "tart", "crumble", "pie", "pancake", "muffin", "waffle", "lollipop"];

let myDinner = function() {
            let menuDiv = document.getElementById("menu");
            let r1 = Math.floor(Math.random() * cookingAdjective.length);
            let r2 = Math.floor(Math.random() * cookingNoun.length);
            let r3 = Math.floor(Math.random() * dessertType.length);
            let r4 = Math.floor(Math.random() * cookingAdjective.length);

            let main = cookingAdjective[r1] + " " + userProtein.value + " " + cookingNoun[r2];
            let side = ", with a side-serving of " + cookingAdjective[r4] + " " + userVegetable.value;
            let dessert = ", and a tasty " + userFruit.value + " " + dessertType[r3] + " for dessert. Enjoy!!";

            menuDiv.innerHTML = main + side + dessert;
        };

dinnerButton.addEventListener('click', myDinner);








// cookingAdj + userProtein + cookingNoun, "with a side-serving of" cookingAdj + userVegetable + ", and" + userFruit 