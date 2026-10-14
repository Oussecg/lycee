function Enregistrer(){
    let Nom = document.getElementById("N").value;
    if (! (Nom.length >= 3 && Nom.indexOf("  ") == -1 && est_alpha(Nom) && "A" <= Nom[Nom.length-1].toUpperCase() && Nom[Nom.length-1].toUpperCase() <= "Z")){
        alert("Nom: Yzi min Blada");
        return false;
    }

    let Pr = document.getElementById("P").value;
    if (! (Pr.length >= 3 && Pr.indexOf("  ") == -1 && est_alpha(Pr) && "A" <= Pr[Pr.length-1].toUpperCase() && Pr[Pr.length-1].toUpperCase() <= "Z")){
        alert("Prénom: Yzi min Blada");
        return false;
    }

    let Ad = document.getElementById("Ad").value;
    let p = Ad.substring(Ad.length - 4, Ad.length);
    if (Ad == "" || isNaN(p)){
        alert("Adresse: Yzi min Blada");
        return false;
    }

    let Dn = document.getElementById("Dn").value;
    let D = new Date(Dn);
    if (Dn == "" || D.getFullYear() > 2007){
        alert("Date de naissance: Yzi min Blada");
        return false;
    }

    let Em = document.getElementById("Em").value;
    let p1 = Em.substring(0, Em.indexOf("@"));
    let p2 = Em.substring(Em.indexOf("@")+1, Em.indexOf("."));
    if (! (est_alphaNum(p1 + p2))){
        alert("Email: Yzi min Blada");
        return false;
    }

    let Mp = document.getElementById("Mp").value;
    if (! (Mp.length == 10 && est_Fort(Mp))){
        alert("Mot de passe: Yzi min Blada");
        return false;
    }

    let Tel = document.getElementById("Tel").value;
    if (! (Tel.length == 8 && Tel[0] != "0")){
        alert("Téléphone: Yzi min Blada");
        return false;
    }

    let For = document.getElementsByName("For");
    let nb = 0;
    for (let i = 0; i < 3; i++){
        if (For[i].checked){
            nb ++;
        }
    }
    if (! (nb == 1)){
        alert("Formation: Yzi min Blada");
        return false;
    }
}

function est_alpha(ch){
    let test = true;
    let i = 0;
    while (test && i < ch.length){
        let c = ch[i].toUpperCase();
        if ("A" <= c && c <= "Z" || c == " "){
            i ++;
        } else{
            test = false;
        }
    }
    return test;
}

function est_alphaNum(ch){
    let test = true;
    let i = 0;
    while (test && i < ch.length){
        let c = ch[i].toUpperCase();
        if ("A" <= c && c <= "Z" || "0" <= c && c <= "9"){
            i ++;
        } else{
            test = false;
        }
    }
    return test;
}

function est_Fort(ch){
    let nb1 = 0;
    let nb2 = 0;
    let nb3 = 0;
    for (let i = 0; i < ch.length; i ++){
        if ("0" <= ch[i] && ch[i] <= "9"){
            nb1 ++;
        } else if ("a" <= ch[i] <= "b"){
            nb2 ++;
        } else if ("A" <= ch[i] <= "Z"){
            nb3 ++;
        }
    }
    return nb1 == 0 || nb2 == 0 || nb3 == 0;
}

function Change(ch){
    document.getElementById("out").innerHTML = ch;
}