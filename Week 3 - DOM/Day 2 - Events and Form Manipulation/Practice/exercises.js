// function insert_Row() {

// let newRow = document.createElement("row");
// document.getElementById("sampleTable").appendChild(newRow);

// let newRowCell1 = document.createElement("td");
// let newRowCell2 = document.createElement("td");
// newRowCell1.innerText="blah";
// newRowCell2.innerText="blah";

// newRow.appendChild(newRowCell1);
// newRow.appendChild(newRowCell2);


// document.getElementById("newRow").appendChild(newRowCell1);
// document.getElementById("newRow").appendChild(newRowCell2);


// }


 var x = document.getElementById("btn")
        var y = document.getElementById("btn1")

    
        x.addEventListener("click", RespondClick); 

        y.addEventListener("click", RespondClick2); 


         function RespondClick(e) { 

         	e.target.style = "background-color: yellow; color: blue; font-weight: bold;";
         	e.target.innerText ="blue in yellow!";
         	// alert(e.screenX);
        } 

        function RespondClick2(e) { 

         	e.target.style = "background-color: blue; color: yellow; font-weight: bold;";
         	e.target.innerText ="yellow in blue!";
        	
        } 


        var z = document.getElementById("jsstyle")

        z.addEventListener("click", RespondClick3); 

        function RespondClick3(e) { 

         	e.target.style = "background-color: black; color: pink; font-weight: bold;";
         	e.target.innerText ="pink in black!";
        	
        } 






