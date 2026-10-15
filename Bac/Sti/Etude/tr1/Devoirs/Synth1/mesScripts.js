function Enregistrer(){
    let Nc = document.getElementById("Nc").value;
    if (! (Nc.length == 8 && (Nc[0] == "0" || Nc[0] == "1") && isNaN(Nc) == false)){
        alert("Ncin: Yzi min Blada !")
        return false;
    }

    let Np = document.getElementById("Np").value;
    if (! (Np.length >= 7 && Np.indexOf(" ") != -1 && estAlpha(Np))){
        alert("Nom & Prénom: Yzi min Blada !")
        return false;
    }

    let Em = document.getElementById("Em").value;
    if (! (estEmail(Em))){
        alert("Email: Yzi min Blada !")
        return false;
    }
    
    let Ad = document.getElementById("Ad").value;
    let p = Ad.substring(Ad.length - 4, Ad.length);
    if (! (Ad.length >= 10 && isNaN(p) == false && p != "0000")){
        alert("Adresse: Yzi min Blada !")
        return false;
    }
    
    let Cl = document.getElementById("Cl").value;
    let p1 = Cl.substring(0, 3);
    let p2 = Cl[3];
    if (! (Cl.length == 4 && (p1 == "4SI" || p1 == "3SI") && isNaN(p2) == false && p2 != "0")){
        alert("Classe: Yzi min Blada !")
        return false;
    }

    let Et = document.getElementsByName("Et");
    let nb = 0;
    for (let i = 0; i < 3; i ++){
        if (Et[i].checked){
            nb ++;
        }
    }
    if (! (nb == 1)){
        alert("Établissement: Yzi min Blada !")
        return false;
    }

    let Clu = document.getElementById("Clu").selectedIndex;
    if (Clu <= 0){
        alert("Club: Yzi min Blada !")
        return false;
    }
}

function estAlpha(ch){
    let test = true;
    let i = 0;
    while (test && i < ch.length){
        let c = ch[i].toUpperCase();
        if ("A" <= c && c <= "Z" || c == " "){
            i ++;
        }  else{
            test = false;
        }
    }
    return test;
}

function estAlphaNum(ch){
    let test = true;
    let i = 0;
    while (test && i < ch.length){
        let c = ch[i].toUpperCase();
        if ("A" <= c && c <= "Z" || "0" <= c && c <= "9"){
            i ++;
        }  else{
            test = false;
        }
    }
    return test;
}

function estEmail(ch){
    let p1 = ch.indexOf(".");
    let p2 = ch.indexOf("@");
    let p3 = ch.indexOf(".", p1+1);
    let ch1 = ch.substring(0, p1);
    let ch2 = ch.substring(p1 + 1, p2);
    let ch3 = ch.substring(p2 + 1, p3);
    let ch4 = ch.substring(p3 + 1, ch.length);
    return est_justifier(ch1) && est_justifier(ch2) && est_justifier(ch3) && est_justifier(ch4);
}

function est_justifier(ch){
    return ch.length > 2 && estAlphaNum(ch);
}

function Converter(c){
    let ch = document.getElementById("ch").value;
    if (ch != ""){
        let ch1 = "";
        let voy = "AEYUIO";
        for (let i = 0; i < ch.length; i ++){
            if (voy.indexOf(ch[i].toUpperCase()) == -1){
                ch1 = ch1 + ch[i];
            } else{
                ch1 = ch1 + c;
            }
        }
        document.getElementById("ch").value = ch1;
    }
}