const list = document.getElementsByTagName("li");


console.log("Pierwszy element:", lista.firstElementChild.textContent);
console.log("Ostatni element:", lista.lastElementChild.textContent);

const srodkowy = document.getElementById("p2");


srodkowy.previousElementSibling.textContent = "Poprzedni";
srodkowy.nextElementSibling.textContent = "Następny";

const wewnetrznyP = document.getElementById("wewnetrzny");
console.log("Element nadrzędny:", wewnetrznyP.parentNode);