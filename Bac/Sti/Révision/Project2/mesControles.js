function Accepter(id) {
	let ch = document.getElementById(id).value;
	let test = true;
	let i = 0;
	do {
		if (
			("A" <= ch[i].toUpperCase() && ch[i].toUpperCase() <= "Z") ||
			ch[i] == " "
		) {
			i = i + 1;
		} else {
			test = false;
		}
	} while (test == true && i < ch.length);
	if (!test) {
		ch = ch.substring(0, i) + ch.substring(i + 1, ch.length);
		document.getElementById(id).value = ch;
	}
}

function Enregistrement() {
	let tel = document.getElementById("presentationTel").value;
	if (!(tel.length == 8 && (tel[0] == "9" || tel[0] == "5" || tel[0] == "2"))) {
		alert("Saisir Votre numéro de Téléphone");
		return false;
	}

	let nomWPrenom = document.getElementById("nomWprenom").value;
	if (
		!(
			7 <= nomWPrenom.length &&
			nomWPrenom.length <= 40 &&
			nomWPrenom.indexOf("  ") == -1
		)
	) {
		alert(
			"Modifier Le champ de nom et prénom de façon qu'il n'ya a pas deux espace",
		);
		return false;
	}

	let adresse = document.getElementById("reclamationAdresse").value;
	if (!(adresse != "" && adresse.length <= 50 && verifierAdresse(adresse))) {
        alert("Saisir votre adresse !!!");
        return false;
	}

    let typePanne = document.getElementsByName("typePanne");
    if (! (typePanne[0].checked || typePanne[1].checked || typePanne[2].checked)){
        alert("Veuillez de choisir une panne !!!");
        return false;
    }
    
    let description = document.getElementById("description").value;
    if (description == "" || !("A" <= description[0].toUpperCase() && description[0].toUpperCase() <= "Z" && description[description.length-1] == "." && description.indexOf("*") == -1 && description.indexOf("#") == -1)){
        alert("Saisir une description qui termine avec Point et ne contient ces symboles *  #");
        return false;
    }
}

function activer(){
    document.getElementById("textAutre").disabled = false;
}

function desactiver(){
    document.getElementById("textAutre").disabled = true;
}

function affiche(){
    let description = document.getElementById("description").value;
    document.getElementById("a100").value = String(100 - description.length);
}

function change(){
    let input = document.getElementById("inputrange").value;
    document.getElementById("range").innerHTML = input;
}

function verifierAdresse(ch){
    ch = ch.substring(ch.length - 4, ch.length);
    return isNaN(ch) == false && ch!="0000";
}