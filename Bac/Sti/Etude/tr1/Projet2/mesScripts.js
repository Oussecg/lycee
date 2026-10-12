function verif1(){
    let Cc = document.getElementById("cdc").value;
    if (! (Cc.length == 10 && verif(Cc))){
        alert("Code Client: Yzi min Blada !!!");
        return false;
    }

    let Np = document.getElementById("np").value;
    if (! (Np.length >= 7 && "A" <= Np[0].toUpperCase() && Np[0].toUpperCase() <= "Z" && est_alpha(Np))){
        alert("Nom: Yzi min Blada !!!");
        return false;
    } 

    let Em = document.getElementById("em").value;
    if (Em.length > 50 || Em.indexOf("@") == -1){
        alert("Email: Yzi min Blada !!!");
        return false;
    } 
    
    let gen = document.getElementsByName("G");
    if (!(gen[0].checked || gen[1].checked)){
        alert("Genre: Yzi min Blada !!!");
        return false;
    }

    let adr = document.getElementById("adr").value;
    if (adr == "" || isNan(adr.subString(adr.length - 5, adr.length))){
        alert("Adresse: Yzi min Blada !!!");
        return false;
    }
}

function est_alpha(ch){
    let test = true;
    let i = 0;
    while (test && i < ch.length){
        if ("A" <= ch[i].toUpperCase() && ch[i].toUpperCase() <= "Z" || ch[i] == " "){
            i ++;
        } else{
            test = false;
        }
    } 
    console.log(test);
    return test
}

function verif(ch){
    let test = true;
    let i = 0;
    while (test && i < ch.length){
        if (i == 0 || i == 1 || i == 8 || i == 9){
            if (isNaN(ch[i])){
                test = false;
            } else{
                i ++;
            }
        } else {
            if (! ("A" <= ch[i].toUpperCase() && ch[i].toUpperCase() <= "Z")){
                test = false;
            } else{
                i ++;
            }
        }
    }
    return test;
}

function verif2(){
    let Cc = document.getElementById("cdc").value;
    if (! (Cc.length == 10 && verif(Cc))){
        alert("Code Client: Yzi min Blada !!!");
        return false;
    }

    let dn = new Date();

    let dd = document.getElementById("dd").value;
    if (dd == "" || new Date(dd) < dn){
        alert("Date début: Yzi min Blada !!!");
        return false;
    }


    let df = document.getElementById("df").value;
    if (df == "" || new Date(df) < dn){
        alert("Date Fin: Yzi min Blada !!!");
        return false;
    };

    let Ta = document.getElementById("Ta").selectedIndex;
    if (Ta <= 0){
        alert("Type Abonnement: Yzi min Blada !!!");
        return false;
    } else{
        var prix = 120;
        if (Ta == 2){
            prix == 150;
        } else if (Ta == 3){
            prix = 200;
        }
        document.getElementById("out").innerText = "Prix: " + prix + "DT";
    }
}

function Prix(){
    let Ta = document.getElementById("Ta");
    if (Ta.selectedIndex > 0){
        document.getElementById("out").innerHTML = "Prix: " + Ta.value + "DT";
    }
} 