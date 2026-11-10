function Generer(){
    let nom = document.getElementById("nom").value;
    nom = nom.substring(nom.length - 3, nom.length);

    let chf = document.getElementById("tel").value;
    chf = chf.substring(0, 4);

    let email = document.getElementById("ema").value;
    let p = email.indexOf("@") + 1;
    email = email.substring(p, p + 2).toUpperCase();

    document.getElementById("pass").value = chf + "#" + nom + "#" + email;
}

function Verif(){
    let np = document.getElementById("nom").value;
    let pp = document.getElementById("pre1").value;
    let pj = document.getElementById("pre2").value;

    let ch = np + pp + pj;
    if (! (9 <= ch.length && ch.length <= 60 && ch.indexOf("  ") == -1 && est_alpha(ch))){
        alert("Error Nom ou Prénom !!!");
        return false;
    }

    let adr = document.getElementById("adr").value;
    if (! (adr.length > 0 && adr.indexOf("Sfax"))){
        alert("Error adresse !!!");
        return false;
    }

    let ema = document.getElementById("ema").value;
    if (!(ema.length < 45)){
        alert("Error email !!!");
        return false;
    }

    let tel = document.getElementById("tel").value;
    if (!(tel[0] != 0 && tel.length == 8)){
        alert("Error tel !!!");
        return false;
    }

}

function est_alpha(ch){
    let test = true;
    let i = 0;
    while (test && i < ch.length){
        if ("A" <= ch[i].toUpperCase() && ch[i].toUpperCase() <= "Z" || ch[i] == " "){
            i += 1;
        } else{
            test = false;
        }
    }
    return test;
}