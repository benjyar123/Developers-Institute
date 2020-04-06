document.getElementById("navBar").setAttribute("id", "socialNetworkNavigation");

let newListItem = document.createElement("li")                // Create a <h1> element
let logoutButtonText = document.createTextNode("Logout");     // Create a text node
newListItem.appendChild(logoutButtonText);                                   // Append the text to <h1>

document.getElementById("socialNetworkNavigation").firstElementChild.setAttribute("id", "navbarList");

document.getElementById("navbarList").appendChild(newListItem);