function alpha(ch) {
  b = true;
  i = 0;
  while (b == true && i < ch.length) {
    c = ch.charAt(i);
    c = c.toUpperCase();
    if ((c >= "A" && c <= "Z") || ch.charAt(i) == " ") i++;
    else b = false;
  }
  return b;
}


function calcul() {

  nom = document.getElementById("nom").value;
  c1 = nom.charAt(0);

  if (nom == "" || c1 < "A" || c1 > "Z" || alpha(nom) == false) {
    alert("nom invalide");
    return false;
  }
  tel = document.getElementById("tel").value;

  if (isNaN(tel) || tel.length != 8) {
    alert("Numéro de telephone invalide");
    return false;
  }

  mail = document.getElementById("mail").value;
  p1 = mail.indexOf("@");
  p2 = mail.indexOf(".", p1);

  if (p1 <= 0 || p2 == -1 || p2 == mail.length - 1) {
    alert("Email non invalide");
    return false;
  }
  dn = document.getElementById("dn").value;
  dn = new Date(dn);
  ds = new Date();

  if (dn === "" || ds <= dn) {
    alert("Date naissance invalide");
    return false;
  }

  prix = 0
  if (document.getElementById("m1").checked) {
    prix = Number(document.getElementById("m1").value)
  } else if (document.getElementById("m2").checked) {
    prix = Number(document.getElementById("m2").value)
  } else if (document.getElementById("m3").checked) {
    prix = Number(document.getElementById("m3").value)
  }
  if (prix === 0) {
    alert("Erreur Quantité !")
    return false;
  }

  Rem = document.getElementById("rem").selectedIndex;
  if (Rem <= 0) {
    alert("Erreur remise !");
    return false;
  }
  Rem = Number(document.getElementById("rem")[Rem].value)
  console.log(Rem)

  Qte = Number(document.getElementById("qte").value)
  if (Qte < 2) {
    alert("Erreur Quantité !");
    return false;
  } else {
    console.log(Qte, prix, Qte);
    document.getElementById("tot").html = Qte * prix - (Rem * prix * Qte)
  }

}
