// Had a nightmare with this and still really not understanding it very well. 

// Obviously the attempt below is insane.
 // and there are more efficient ways to do it with loops etc,
  // but just getting basics of DOM is really tricky right now 
  // so I've got every step done manually.



let allBooks = [
{title: "1984", author: "George Orwell", image: "1984.jpg", alreadyRead: true},
{title: "Pride and Prejudice",author: "Jane Austen",image: "pride.jpg",alreadyRead: false}
];

let bookTable = document.createElement("table");
bookTable.setAttribute("id", "myBookTable");
document.body.appendChild(bookTable);

let headRow = document.createElement("tr");
headRow.setAttribute("id", "myTopRow");
bookTable.appendChild(headRow);

let firstRow = document.createElement("tr");
firstRow.setAttribute("id", "myFirstRow");
bookTable.appendChild(firstRow);

let secondRow = document.createElement("tr");
secondRow.setAttribute("id", "mySecondRow");
bookTable.appendChild(secondRow);

let firstColHead = document.createElement("th");
firstColHead.setAttribute("id", "myFirstColHead");

let secondColHead = document.createElement("th");
secondColHead.setAttribute("id", "mySecondColHead");

headRow.appendChild(firstColHead);
headRow.appendChild(secondColHead);


let R1C1 = document.createElement("td");
R1C1.setAttribute("id", "myR1C1");

let R1C2 = document.createElement("td");
R1C2.setAttribute("id", "myR1C2");

firstRow.appendChild(R1C1);
firstRow.appendChild(R1C2);

let image1 = document.createElement("img");
image1.setAttribute("id", "myImage1");
image1.setAttribute("width", "100px");
R1C2.appendChild(image1);


let R2C1 = document.createElement("td");
R2C1.setAttribute("id", "myR2C1");

let R2C2 = document.createElement("td");
R2C2.setAttribute("id", "myR2C2");

secondRow.appendChild(R2C1);
secondRow.appendChild(R2C2);

let image2 = document.createElement("img");
image2.setAttribute("id", "myImage2");
image2.setAttribute("width", "100px");
R2C2.appendChild(image2);














document.getElementById("myFirstColHead").innerHTML = "Book";
document.getElementById("mySecondColHead").innerHTML = "Cover";



document.getElementById("myR1C1").innerHTML = allBooks[0]['title'] + ", written by " + allBooks[0]['author'];
document.getElementById("myImage1").src = allBooks[0]['image'];

document.getElementById("myR2C1").innerHTML = allBooks[1]['title'] + ", written by " + allBooks[1]['author'];
document.getElementById("myImage2").src = allBooks[1]['image'];
















