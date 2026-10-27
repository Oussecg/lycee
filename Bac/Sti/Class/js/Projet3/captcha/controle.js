function GenererCaptcha(){
    let ch = "";
    for (let i = 0; i < 10; i++) {
        let x = randint(1, 26);
        if (x % 2 == 0){
            ch += String.fromCharCode(x + 64);
        } else{
            ch += String.fromCharCode(x + 64).toLowerCase();
        }
    }
    document.getElementById("cap").value = ch;
}

function randint(a, b){
    return Math.trunc(Math.random() * b + a);
}

function verif1(){
    let mail = document.getElementById("mail").value;
    if (! verifMail(mail)){
        alert("Faux d'Email !");
        return false;
    }

    let motPass = document.getElementById("pw").value;
    if (! est_Mp(motPass)){
        alert("Faux de mote de passe !");
        return false;
    }

    let capt = document.getElementById("cap").value;
    let ck = document.getElementById("nb").value;
    let nbr = 0;
    for (let i = 0; i < capt; i++) {
        if ("A" <= capt[i] <= "Z"){
            nbr ++;
        } 
    }
    if (Number(ck) == capt){
        alert("Réponse Fausse !");
        return false;
    }
}

function verifMail(ch){
    let p = ch.indexOf("@");
    let p1 = ch.indexOf(".", p);
    return p1 != -1 && 1 <= p - p1 && p - p1 <= 4
}

function est_Mp(ch){
    let nb1 = 0;
    let nb2 = 0;
    let nb3 = 0;
    for (let i = 0; i < ch.length; i++) {
        if ("A" <= ch[i] && ch[i] <= "Z"){
            nb1 ++;
        } else if ("a" <= ch[i] <= "z"){
            nb2 ++;
        } else if ("0" <= ch[i] <= "9"){
            nb3 ++;
        }
    }
    return ch.length >= 6 && nb1 > 0 && nb2 > 0 && nb3 > 0;
}