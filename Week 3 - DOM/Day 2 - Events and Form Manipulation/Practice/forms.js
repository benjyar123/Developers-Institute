// EXERCISE 1 - accessing and modifying form elements

let form = document.forms.form1;
let firstName = form.elements.fname; 
let lastName = form.elements.lname; 

console.log(firstName.value);
console.log(lastName.value);

lastName.value = "Hasselhof";

console.log(firstName.value);
console.log(lastName.value);


// EXERCISE 2

let selectForm = document.getElementById('select1');





  // all three lines do the same thing
  // select.options[2].selected = true; //Banana selected
  // select.value = 'banana'; //Banana selected
  // select.selectedIndex = 2; //Banana selected

    // // To check which option is selected
    // console.log(select.selectedIndex) // "2"
    // console.log(select.value) // "Banana"



