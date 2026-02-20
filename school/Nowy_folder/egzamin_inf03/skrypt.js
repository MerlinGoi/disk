function dalej1() {
    document.getElementById("karta1").style.display = "none";
    document.getElementById("karta2").style.display = "block";
}

function dalej2() {
    document.getElementById("karta2").style.display = "none";
    document.getElementById("karta3").style.display = "block";
}

function zatwierdz() {
    let h1 = document.getElementById("haslo1").value;
    let h2 = document.getElementById("haslo2").value;

    if (h1 !== h2) {
        alert("Podane hasła różnią się");
    }

    let imie = document.getElementById("imie").value;
    let nazwisko = document.getElementById("nazwisko").value;

    console.log("Witaj " + imie + " " + nazwisko);
}
