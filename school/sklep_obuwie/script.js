// To jest poprawny zapis JSON (jako tekst)
const productJson = `{
  "name": "Air Max 720",
  "brand": "Nike",
  "description": "Mają największą, jak dotąd, poduszkę gazową Air...",
  "size": 45,
  "imageUrl": "https://example.pl/path/to/airmax.png",
  "price": "649.99",
  "currency": "PLN"
}`;

// Próba parsowania (zamiana tekstu na obiekt)
try {
  const product = JSON.parse(productJson);
  console.log("Sukces! Produkt to:", product.name);
  console.log(product);
} catch (error) {
  console.error("Błąd w formacie JSON:", error);
}



let obj = {};
const obj2 = obj;

obj.name = "Alek"; 

console.log(obj.name);  // Alek
console.log(obj2.name); // Alek (bo obj2 wskazuje na ten sam obiekt co obj)

const obj3 = { name: obj.name };
console.log(obj3); // {name: "Alek"}

// Kluczowy moment: przypisanie nowego obiektu do zmiennej obj
obj = { size: "S" };

console.log(obj.name);  // undefined (bo "obj" to teraz nowy obiekt, który nie ma pola name)
console.log(obj.size);  // S
console.log(obj2.name); // Alek (bo obj2 wciąż wskazuje na "stary" obiekt)


const user = {
  name: "Kuba",
  surname: "Wędrowycz",
  address: {
    country: "Polska",
    city: "Stary Majdan",
    postal: "22-120",
    street: null
  }
};

const book = {
  title: "Karpie bijem",
  releaseYear: 2019
};

// Użycie:
console.log(user.surname); // Wędrowycz
user.name = "Jakub";
console.log(user.address.city); // Stary Majdan
user.address.street = "Bagnowska";
console.log(book.releaseYear); // 2019